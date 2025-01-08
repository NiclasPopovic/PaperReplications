import numpy as np
from unittest import TestCase
from src.aksen_et_al_2003_european_journal_of_operational_research.source.dynamic_program import (
    DynamicProgram,
)


class TestAlgorithm(TestCase):
    """
    Unit tests for the `DynamicProgram` class.

    This test class verifies the correctness of the dynamic programming algorithm
    implemented in the `DynamicProgram` class. It includes setup for a predefined
    lot-sizing problem and a test case to validate the computed results.

    Attributes:
        DPAlgorithm (DynamicProgram): An instance of the `DynamicProgram` class
                                      initialized with predefined inputs for testing.

    Methods:
        - setUp: Initializes the `DynamicProgram` instance before each test.
        - testAlgorithm: Verifies that the computed minimum cost matches the expected value.
    """

    def setUp(self):
        """
        Initializes the `DynamicProgram` instance for testing.

        The `DynamicProgram` instance is created with predefined demand, interest charge,
        and ordering costs to test the correctness of the dynamic programming algorithm.

        Attributes Initialized:
            - demand: A list of demand values for 12 periods.
            - interest_charge: Per-unit holding cost.
            - ordering_cost: A list of fixed ordering costs for 12 periods.
        """
        self.DPAlgorithm = DynamicProgram(
            demand=[3000, 11750, 2000, 4000],
            unit_holding_cost=[3, 3, 3, 3],
            unit_ordering_cost=[10, 10, 10, 10],
            fixed_ordering_cost=[25000, 25000, 25000, 25000],
            unit_revenue=[15, 21, 12, 18],
        )

    def test_holding_costs(self):
        """
        Tests the `DynamicProgram` algorithm for correctness of marginal cost computations.

        This method runs the `DynamicProgram._precompute_holding_costs()` method and verifies
        that the computed marginal costs between specific periods match the expected values.
        """
        self.DPAlgorithm._precompute_holding_and_marginal_costs()
        assert self.DPAlgorithm._marginal_costs[1, 3] == 16
        assert self.DPAlgorithm._marginal_costs[2, 3] == 13

    def test_algorithm(self):
        """
        Tests the `DynamicProgram` algorithm for correctness of total costs and production periods.

        This method runs the `DynamicProgram.run()` method and verifies that the computed
        total costs and production periods match the expected values.
        """
        total_costs, production_periods = self.DPAlgorithm.run()
        expected_total_costs = np.array([0, 45000.0, 187500.0, 211500.0, 275500.0])
        assert np.array_equal(
            total_costs, expected_total_costs
        ), f"Expected {expected_total_costs}, but got {total_costs}"
        expected_production_periods = [0, 2, 2, 2]
        assert np.array_equal(
            expected_production_periods, production_periods
        ), f"Expected{expected_production_periods}, but got {production_periods}"
