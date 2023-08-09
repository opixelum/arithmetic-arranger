"""Script to demonstrate the functionality of the arithmetic_arranger function."""

from arithmetic_arranger import arithmetic_arranger


def main():
    # Example 1
    problems1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print("Problems 1:", problems1, "without answers.\n")
    print(arithmetic_arranger(problems1))

    # Example 2
    problems2 = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
    print("Problems 2:", problems2, "with answers.\n")
    print(arithmetic_arranger(problems2, True))

    # Example 3
    problems3 = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
    print("Problems 3:", problems3, "without answers.\n")
    print(arithmetic_arranger(problems3))

    # A few more examples can be added here for demonstration purposes


if __name__ == "__main__":
    main()
