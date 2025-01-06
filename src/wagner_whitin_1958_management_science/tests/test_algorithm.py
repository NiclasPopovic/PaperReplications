from unittest import TestCase
from src.wagner_whitin_1958_management_science.source.dynamic_program import (
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
            demand=[69, 29, 36, 61, 61, 26, 34, 67, 45, 67, 79, 56],
            interest_charge=1,
            ordering_cost=[85, 102, 102, 101, 98, 114, 105, 86, 119, 110, 98, 114],
        )

    def testAlgorithm(self):
        """
        Tests the `DynamicProgram` algorithm for correctness.

        This method runs the `DynamicProgram.run()` method and verifies that the computed
        minimum cost for the last period matches the expected value.

        Assertions:
            - Asserts that the computed cost for period 12 equals the expected value of the final period (864).

        Example:
            After running `self.DPAlgorithm.run()`, `self.DPAlgorithm.period_costs[12]`
            should equal 864, as calculated from the predefined inputs in the paper.
        """
        self.DPAlgorithm.run()
        self.assertEqual(864, self.DPAlgorithm.period_costs[12])
