# Insertion sort
def insertion_sort(input_list):
    for index in range(1, len(input_list)):
        currentval = input_list[index]
        pos = index

        while pos > 0 and input_list[pos - 1] > currentval:
            input_list[pos] = input_list[pos - 1]
            pos = pos - 1

        input_list[pos] = currentval

input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(input_list)
print(input_list)
