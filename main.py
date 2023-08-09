"""Script to demonstrate the functionality of the arithmetic_arranger function."""

from arithmetic_arranger import arithmetic_arranger


def main():
    # Example 1
    problems1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print("Problems 1:", problems1, "without answers.\n")
    print(arithmetic_arranger(problems1))

    # Example 2
    problems2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    print("Problems 2:", problems2, "with answers.\n")
    print(arithmetic_arranger(problems2, True))

    # A few more examples can be added here for demonstration purposes


if __name__ == "__main__":
    main()
