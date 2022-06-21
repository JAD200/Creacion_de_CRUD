import random


def binary_search(data, target):
    """binary_search Algorithm to search for a number in a large list

    Args:
        data (list): List of numbers
        target (int): Number to search

    Returns:
        bool: True or False whether the number is or not in the list
    """

    low_index = 0
    high_index = len(data) - 1

    while low_index <= high_index:
        # * Establishes the middle of the list
        mid = (low_index + high_index) // 2
        #   All posible cases for the algorithm
        if data[mid] == target:
            return True
        elif target < data[mid]:
            high_index = mid - 1
        else:
            low_index = mid + 1

    return False


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]

    data.sort()
    print(data)

    target = int(input('What number would you like to find? '))
    found = binary_search(data, target)

    if found:
        print(f'The number {target} is in the list!!')
    else:
        print(f'Sadly, the number {target} isn\'t in the list')
