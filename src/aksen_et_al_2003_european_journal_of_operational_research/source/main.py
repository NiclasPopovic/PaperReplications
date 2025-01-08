from dynamic_program import DynamicProgram

if __name__ == "__main__":
    try:
        DP = DynamicProgram(
            demand=[3000, 11750, 2000, 4000],
            unit_holding_cost=[3, 3, 3, 3],
            unit_ordering_cost=[10, 10, 10, 10],
            fixed_ordering_cost=[25000, 25000, 25000, 25000],
            unit_revenue=[15, 21, 12, 18]
        )
        DP.run()
    except Exception as e:
        print(f"An error occurred: {e}")
