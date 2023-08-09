def arithmetic_arranger(problems, show_answers=False):
    """Arranges up to 5 arithmetic problems vertically and side-by-side, with
    answer or not.

    Args:
        problems (list[str]): List of arithmetic problems to be arranged. Each
        problem is a string of the form "num1 op num2", where num1 and num2
        are integers and op is either "+" or "-". The length of the list must
        be less than or equal to 5.

        show_answers (bool, optional): Display answer below each problem if
        True. Defaults to False.

    Returns:
        str: String of the arranged problems, each separated by 4 spaces. Empty
        string if an error occurs.
    """
    # Check if the format of the problems is valid
    if not problems_format_checker(problems):
        return ""

    return arranged_problems_string(problems, show_answers)


def problems_format_checker(problems):
    """Checks if the format of the problems is valid.

    Args:
        problems (list[str]): List of arithmetic problems to be arranged. Each
        problem is a string of the form "num1 op num2", where num1 and num2
        are integers and op is either "+" or "-". The length of the list must
        be less than or equal to 5.

    Returns:
        bool: True if the format is valid, False otherwise.
    """
    # Check if problem list is empty
    if len(problems) == 0:
        print("Error: Problem list is empty.")
        return False

    # Check if the number of problems is valid
    if len(problems) > 5:
        print("Error: Too many problems.")
        return False
    
    # Check if the operator is valid
    for problem in problems:
        if problem.split()[1] not in ["+", "-"]:
            print("Error: Operator must be '+' or '-'.")
            return False

    # Check if the operands are digits
    for problem in problems:
        if not problem.split()[0].isdigit() or not problem.split()[2].isdigit():
            print("Error: Numbers must only contain digits.")
            return False

    # Check if the operands are less than 5 digits
    for problem in problems:
        if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return False

    return True


def arranged_problems_string(problems, show_answers=False):
    """Returns the string of the arranged problems.

    Args:
        problems (list[str]): List of arithmetic problems to be arranged. Each
        problem is a string of the form "num1 op num2", where num1 and num2
        are integers and op is either "+" or "-". The length of the list must
        be less than or equal to 5.

        show_answers (bool, optional): Display answer below each problem if
        True. Defaults to False.

    Returns:
        str: String of the arranged problems, each separated by 4 spaces. Empty
        string if an error occurs.
    """
    # Check if the format of the problems is valid
    if not problems_format_checker(problems):
        return ""

    # Build arranged problems string
    arranged_problems = ""
    first_operands = []
    second_operands = []
    operators = []
    max_lengths = []

    # Iterate through the problems for getting the operands and operators
    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Determine the length of the longer operand
        length = max(len(operand1), len(operand2))

        # Add 2 to the length to account for the operator and the space
        length += 2

        # Add everything to the lists
        first_operands.append(operand1)
        second_operands.append(operand2)
        operators.append(operator)
        max_lengths.append(length)

    # Build line 1
    for i in range(len(problems)):
        # Add the first operand to the string
        arranged_problems += f"{first_operands[i]:>{max_lengths[i]}}"

        # Add the space between the operands
        if i < len(problems) - 1:
            arranged_problems += "    "
        else:
            arranged_problems += "\n"

    # Build line 2
    for i in range(len(problems)):
        # Add the space between the operands
        arranged_problems += f"{operators[i]} {second_operands[i]:>{max_lengths[i] - 2}}"

        # Add the space between the operands and the dashes
        if i < len(problems) - 1:
            arranged_problems += "    "
        else:
            arranged_problems += "\n"

    # Build line 3
    for i in range(len(problems)):
        # Determine the number of dashes to be printed
        dashes = "-" * max_lengths[i]

        # Add the dashes to the string
        arranged_problems += f"{dashes}"

        # Add the space between the problems
        if i < len(problems) - 1:
            arranged_problems += "    "
        else:
            arranged_problems += "\n"

    # Build line 4 if show_answers is True
    if show_answers:
        # Get the results of the problems
        results = resolve_problems(problems)

        # Build line 4
        for i in range(len(problems)):
            # Add the result to the string
            arranged_problems += f"{results[i]:>{max_lengths[i]}}"

            # Add the space between the problems
            if i < len(problems) - 1:
                arranged_problems += "    "
    
    return arranged_problems


def resolve_problems(problems):
    """Resolves the arithmetic problems.

    Args:
        problems (list[str]): List of arithmetic problems to be arranged. Each
        problem is a string of the form "num1 op num2", where num1 and num2
        are integers and op is either "+" or "-". The length of the list must
        be less than or equal to 5.

    Returns:
        list[str]: List of the results of the arithmetic problems, where index
        i corresponds to the result of problem i. Empty list if an error occurs.
    """
    # Check if the format of the problems is valid
    if not problems_format_checker(problems):
        return []

    # Resolve the problems
    results = []
    for problem in problems:
        operand1, operator, operand2 = problem.split()
        if operator == "+":
            results.append(int(operand1) + int(operand2))
        else:
            results.append(int(operand1) - int(operand2))

    return results
