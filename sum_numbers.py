from typing import List


def sum_numbers(numbers: List[float]) -> float:
    """Calculate the total from a list of numbers.

    Args:
        numbers (List[float]): the list of numbers to sum.

    Returns:
        float: summed numbers from the list.
    """
    total = 0

    for number in numbers:
        total += number

    return total
