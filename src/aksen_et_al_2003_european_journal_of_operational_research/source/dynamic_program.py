import sys
import os
import numpy as np
from collections import defaultdict
from itertools import accumulate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class DynamicProgram:
    """
    Implements a dynamic programming approach to solve the single-item lot-sizing problem
    with immediate lost sales.

    This class computes the minimum cost of satisfying demand over a finite planning horizon
    while accounting for ordering, holding, and lost sales costs. It includes methods for
    precomputing marginal costs and determining the optimal ordering policy.

    Attributes:
        _demand (np.ndarray): Demand for each period.
        _unit_holding_cost (np.ndarray): Per-unit holding cost per period.
        _unit_ordering_cost (np.ndarray): Variable ordering cost per unit for each period.
        _fixed_ordering_cost (np.ndarray): Fixed ordering cost for each period.
        _unit_revenue (np.ndarray): Per-unit revenue for unsatisfied demand (lost sales).
        _periods (int): Total number of periods in the planning horizon.
        _marginal_costs (np.ndarray): Marginal cost matrix for satisfying demand between periods.
        _cumulative_holding_costs (np.ndarray): Cumulative holding costs for precomputations.
        period_costs (np.ndarray): Minimum cost to satisfy demand up to each period.
        last_production_period (np.ndarray): Tracks the last production period for optimal policy.

    Methods:
        - _precompute_holding_costs: Precomputes the marginal costs matrix.
        - run: Executes the dynamic programming algorithm to determine the minimum cost and
               optimal ordering policy.

    Example:
        dp = DynamicProgram(
            demand=[10, 15, 20],
            unit_holding_cost=[2, 2, 2],
            unit_ordering_cost=[3, 3, 3],
            fixed_ordering_cost=[50, 50, 50],
            unit_revenue=[100, 100, 100]
        )
        total_costs, production_periods = dp.run()
        print(total_costs)  # Minimum costs for each period
        print(production_periods)  # Optimal production policy
    """

    def __init__(self, demand, unit_holding_cost, unit_ordering_cost, fixed_ordering_cost, unit_revenue):
        self._demand = np.array(demand)
        self._periods = len(self._demand)
        self._marginal_costs = np.zeros((self._periods, self._periods))
        self._unit_holding_cost = np.array(unit_holding_cost)
        self._unit_ordering_cost = np.array(unit_ordering_cost)
        self._fixed_ordering_cost = np.array(fixed_ordering_cost)
        self._unit_revenue = np.array(unit_revenue)
        self._cumulative_holding_costs = np.zeros(self._periods + 1) # +1 to include the index at position -1

        self.period_costs = defaultdict(int)
        self.optimal_policy = {}

    def _precompute_holding_and_marginal_costs(self):
        """
        Precomputes the holding and marginal costs for all possible combinations of order start and end periods.

        The marginal cost matrix calculates the cost of fulfilling demand from a start period `j`
        to an end period `t`. This includes the variable ordering costs, cumulative holding costs,
        and lost sales penalties.

        Returns:
            None. Updates:
                - `_marginal_costs`: A 2D array where `_marginal_costs[j][t]` represents the
                  total marginal cost of satisfying demand from period `j+1` to `t`.

        Example:
            For demand = [10, 15, 20], unit_holding_cost = [2, 2, 2], and unit_revenue = [100, 100, 100]:
                - `_marginal_costs[1][3]` represents the cost of satisfying demand for period 3
                  starting from production in period 2.
        """
        self._cumulative_holding_costs[0] = 0

        self._cumulative_holding_costs = list(accumulate(
            self._unit_holding_cost,
            lambda total, current: total + current,
            initial=0))

        n = len(self._demand)
        holding_costs = np.zeros((n + 1, n + 1))
        for j in range(1, self._periods):
            for t in range(j, self._periods):
                self._marginal_costs[j-1,t]=np.min([self._unit_revenue[t],
                                            self._unit_ordering_cost[j-1] + self._cumulative_holding_costs[t] - self._cumulative_holding_costs[j-1]
                                     ])

    def run(self):
        """
        Executes the dynamic programming algorithm to solve the lot-sizing problem with immediate lost sales.

        This method calculates the minimum cost of satisfying demand for each period over the planning
        horizon. It uses precomputed marginal costs and dynamic programming to determine the optimal
        ordering policy.

        Returns:
            tuple:
                - period_costs (np.ndarray): Minimum cost to satisfy demand up to each period.
                - last_production_period (np.ndarray): Optimal production periods for each time step.

        Example:
            After running this method, `period_costs[4]` will contain the minimum cost to satisfy demand
            up to period 4, and `last_production_period[3]` will indicate the last production period
            for period 4's demand.
        """
        self.period_costs = np.zeros(self._periods + 1)
        self.last_production_period = np.zeros(self._periods, dtype=int)
        self._period_production_costs = np.zeros((self._periods + 1, self._periods + 1))

        self.period_costs[0] = 0
        self._precompute_holding_and_marginal_costs()  # Precompute holding costs

        # Step 1: Compute the total period production costs for the case when nothing is produced and each demand unit is lost
        for t in range(0, self._periods):
            if t == 0:
                self._period_production_costs[(0, t+1)] = self._unit_revenue[t] * self._demand[t]
            else:
                self._period_production_costs[(0, t+1)] = self._period_production_costs[(0, t)] + self._unit_revenue[t] * self._demand[t]

        # Step 2: The dynamic program where the total cost C(t9 and total production costs C_j(t) are calculated
        for t in range(1, self._periods+1):
            if t == 1:
                self._period_production_costs[(t, t)] = self._fixed_ordering_cost[t-1] + self._unit_ordering_cost[t-1] * self._demand[t-1]
            else:
                self._period_production_costs[(t, t)] = self.period_costs[t-1] + self._fixed_ordering_cost[t-1] + self._unit_ordering_cost[t-1] * self._demand[t-1]

            for j in range(1, t):
                self._period_production_costs[(j, t)] = self._period_production_costs[(j, t-1)] + self._marginal_costs[j-1, t-1] * self._demand[t-1]

            list_of_potential_solutions = [self._period_production_costs[j, t] for j in range (0, t+1)]
            self.period_costs[t] = np.min(list_of_potential_solutions)
            self.last_production_period[t-1] = np.argmin(list_of_potential_solutions)

        print(f"Period Costs: {self.period_costs}")
        print(f"Production periods: {self.last_production_period}")

        return self.period_costs, self.last_production_period
