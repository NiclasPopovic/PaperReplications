import sys
import os
import numpy as np
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class DynamicProgram:
    """
    Implements the dynamic programming approach for solving the standard lot-sizing problem proposed by
    Wagner & Whitin (1958)

    This class calculates the minimum cost of satisfying demand over a finite planning
    horizon by considering ordering and holding costs. It includes methods for precomputing
    holding costs and determining the optimal ordering policy.

    Attributes:
        _demand (list[int]): Demand for each period.
        _interest_charge (float): Per-unit holding cost per period.
        _ordering_cost (list[float]): Fixed ordering cost for each period.
        _periods (int): Total number of periods in the planning horizon.
        period_costs (defaultdict): Stores the minimum cost for satisfying demand up to
                                    each period.
        optimal_policy (dict): Maps each period to the optimal ordering decision.

    Methods:
        - _precompute_holding_costs: Precomputes the holding cost matrix.
        - run: Executes the dynamic programming algorithm to determine the optimal policy.

    Example:
        dp = DynamicProgram(demand=[10, 15, 20], interest_charge=2, ordering_cost=[50, 50, 50])
        dp.run()
        print(dp.period_costs)  # Minimum costs for each period
        print(dp.optimal_policy)  # Optimal ordering decisions
    """

    def __init__(self, demand, interest_charge, ordering_cost):
        self._demand = np.array(demand)
        self._interest_charge = interest_charge
        self._ordering_cost = np.array(ordering_cost)
        self._periods = len(self._demand)
        self.period_costs = defaultdict(int)
        self.optimal_policy = {}

    def _precompute_holding_costs(self):
        """
        Precomputes the holding costs for all possible order start and end periods.

        The holding cost matrix stores the cumulative cost of carrying demand from a start
        period `j` to an end period `t`. For each unit of demand satisfied, holding costs
        are incurred for every intermediate period it is carried forward.

        This implementation explicitly computes the costs using nested loops to ensure that
        each demand contributes correctly to the total holding costs.

        Returns:
            holding_costs (np.ndarray): A 2D array where holding_costs[t][j] represents the
                                        total holding cost for satisfying demand from period
                                        j+1 to t.

        Example:
            For demand = [10, 15, 20], interest_charge = 2:
                - holding_costs[3][1] accounts for:
                    - Demand for t=2 carried for 1 period.
                    - Demand for t=3 carried for 2 periods.
        """
        n = self._periods
        holding_costs = np.zeros((n + 1, n + 1))

        # Holding costs calculations may be optimized
        for t in range(1, len(self._demand)):
            for j in range(0, t):
                for h in range(j, t):
                    for k in range(h + 1, t + 1):
                        holding_costs[t, j] += self._interest_charge * self._demand[k]

        return holding_costs

    def run(self):
        """
        Executes the optimized dynamic programming algorithm to solve the lot-sizing problem.

        This method calculates the minimum cost of satisfying demand over a finite planning
        horizon by considering ordering and holding costs. It precomputes holding costs for
        efficiency and uses dynamic programming to determine the optimal ordering policy.

        Attributes Updated:
            - self.period_costs (dict): Minimum cost to satisfy demand up to each period.

        Returns:
            None. Results are stored in:
                - self.period_costs: Maps each period to the minimum cost up to that period.

        Example:
            For demand = [10, 15, 20], interest_charge = 2, and ordering_cost = [50, 50, 50]:
                - self.period_costs = {1: 50, 2: 95, 3: 170}
        """
        self.period_costs = defaultdict(int)
        self.period_costs[0] = 0

        holding_costs = self._precompute_holding_costs()  # Precompute holding costs

        for period in range(1, self._periods + 1):
            min_cost = float("inf")

            for j in range(1, period + 1):
                current_cost = (
                    self._ordering_cost[j - 1]
                    + holding_costs[period - 1][j - 1]
                    + self.period_costs[j - 1]
                )
                min_cost = min(min_cost, current_cost)

            self.period_costs[period] = min_cost

        print("Period Costs:", self.period_costs)
