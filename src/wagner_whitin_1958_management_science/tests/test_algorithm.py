from unittest import TestCase
from src.wagner_whitin_1958_management_science.source.dynamic_program import DynamicProgram

class TestAlgorithm(TestCase):

    def setUp(self):
        self.DPAlgorithm = DynamicProgram(demand=[69, 29, 36, 61, 61, 26,
                                                  34, 67,  45, 67, 79, 56],
                                          interest_charge=1,
                                          ordering_cost=[85, 102, 102, 101, 98, 114,
                                                  105, 86, 119, 110, 98, 114])


    def testAlgorithm(self):
        self.DPAlgorithm.run()
        self.assertEqual(864, self.DPAlgorithm.period_costs[12])


