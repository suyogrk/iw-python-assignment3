# a7 - interpolation search
def interpolation_search(input_list, item):
    start = 0
    end = len(input_list) - 1
    found = False

    while start <= end and found == False:
        if start == end:
            if input_list[start] == item:
                return start
            return -1

        pos = start + ((end - start) // (input_list[end] - input_list[start])) * (item - input_list[start])

        if input_list[pos] == item:
            return pos

        if input_list[pos] < item:
            start = pos + 1
        else:
            end = pos - 1
    return -1

input_list = [17, 20, 26, 31, 44, 54, 55, 77, 93]
print(interpolation_search(input_list, 31))
