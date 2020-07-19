# A3 - quick sort
def quick_sort(input_list):
    quick_sort_helper(input_list, 0, len(input_list) - 1)

def quick_sort_helper(input_list, first, last):
    if first < last:
        split = partition(input_list, first, last)
        quick_sort_helper(input_list, first, split - 1)
        quick_sort_helper(input_list, split + 1, last)

def partition(input_list, first, last):
    pivot = input_list[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and input_list[left] <= pivot:
            left = left + 1

        while right >= left and input_list[right] >= pivot:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = input_list[left]
            input_list[left] = input_list[right]
            input_list[right] = temp

    temp = input_list[first]
    input_list[first] = input_list[right]
    input_list[right] = temp

    return right



input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(input_list)
print(input_list)
