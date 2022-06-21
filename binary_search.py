import random


def binary_search(data, target, low_index, high_index):
    """binary_search Algorithm to search for a number in a large list

    Args:
        data (list): List of numbers
        target (int): Number to search
        low_index (int): Index with the lowest value
        high_index (int): Index with the highest value

    Returns:
        bool: True or False whether the number is or not in the list
    """
    if low_index > high_index:
        return False
# * Establishes the middle of the list
    mid = (low_index + high_index // 2)
#   All posible cases for the algorithm
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low_index, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high_index)


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]

    data.sort()
    print(data)

    target = int(input('What number would you like to find? '))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)
