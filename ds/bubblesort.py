# Bubble Sort
def bubblesort(input_list):
    for passnum in range(len(input_list) - 1, 0, -1):
        for i in range(passnum):
            if input_list[i] > input_list[i + 1]:
                temp = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = temp


input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubblesort(input_list)
print(input_list)
