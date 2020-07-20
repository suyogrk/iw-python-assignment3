# a5 - linear search
def linear_search(input_list, item):
    for i in range(len(input_list)):
        if input_list[i] == item:
            return i
    return -1

input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(linear_search(input_list, 93))
print(linear_search(input_list, 100))
