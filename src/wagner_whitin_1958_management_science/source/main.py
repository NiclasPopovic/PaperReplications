from dynamic_program import DynamicProgram

if __name__ == '__main__':
    try:
        DP = DynamicProgram(demand=[69, 29, 36, 61, 61, 26,
                                    34, 67, 45, 67, 79, 56],
                                    interest_charge=1,
                                    ordering_cost=[85, 102, 102, 101, 98, 114,
                                                105, 86, 119, 110, 98, 114])
        DP.run()
    except Exception as e:
        print(f"An error occurred: {e}")
