# a6- binary search
def binary_search(input_list, item):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        middle = (low + high) // 2

        if input_list[middle] == item:
            return middle
        elif input_list[middle] > item:
            high = middle - 1
        else:
            low = middle + 1

    return -1


input_list = [17, 20, 26, 31, 44, 54, 55, 77, 93]
print(binary_search(input_list, 44))


