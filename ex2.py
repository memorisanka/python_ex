numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]


def sum_first_ten(lst) -> list:
    return sum(lst[4:14])


print(f"Sum of first ten elements starting from element number 5: {sum_first_ten(numbers)}")
