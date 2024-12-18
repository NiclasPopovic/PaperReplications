import sys
import os
import numpy as np
from collections import defaultdict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class DynamicProgram:

    def __init__(self, demand, interest_charge, ordering_cost):
        self._demand = demand
        self._interest_charge = interest_charge
        self._ordering_cost = ordering_cost
        self._periods = len(self._demand)
        self.period_costs = defaultdict(int)

    def _precompute_holding_costs(self):
        n = len(self._demand)
        holding_costs = np.zeros((n + 1, n + 1))  # Matrix to store holding costs

        # Precompute cumulative demand
        cumulative_demand = np.zeros(n + 1)
        for t in range(1, n + 1):
            cumulative_demand[t] = cumulative_demand[t - 1] + self._demand[t - 1]

        # Calculate holding costs using cumulative sums
        for j in range(1, n + 1):  # Start period
            for t in range(j, n + 1):  # End period
                holding_costs[j][t] = self._interest_charge * (cumulative_demand[t] - cumulative_demand[j - 1])



    def run(self):
        self.period_costs = defaultdict(int)
        first_term = defaultdict(int)
        second_term = defaultdict(int)
        self.period_costs[0] = 0
        optimal_policy = {}

        for period, _ in enumerate(self._demand, start=1):

            # period 0 is period 1 in the algorithm description in the paper
            if period == 1:
                # Optimal cost for the first period: just order the demand for the first period
                self.period_costs[period] = self._ordering_cost[period-1]
                optimal_policy[period] = f'{period}|{period}'
                continue

            min_first_term = float('inf')
            for j in range(1, period):
                holding_costs = 0
                for h in range(j, period):
                    for k in range(h + 1, period+1):
                        holding_costs += self._interest_charge * self._demand[k-1] # Adjust for 0-based indexing

                current_first_term = self._ordering_cost[j-1] + holding_costs + self.period_costs[j-1]
                first_term[(period, j)]  = current_first_term
                min_first_term = min(min_first_term, current_first_term)

            second_term[period] = self._ordering_cost[period-1] + self.period_costs[period - 1]
            self.period_costs[period] = min(min_first_term, second_term[period])

        print(self.period_costs)