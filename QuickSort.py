from random import randrange, shuffle


def quicksort(list, start, end):
    if start >= end:
        return

    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    list[pivot_idx], list[end] = list[end], list[pivot_idx]
    lesser_than_pointer = start
    for idx in range(start, end):
        if list[idx] < pivot_element:
            list[idx], list[lesser_than_pointer] = list[lesser_than_pointer], list[idx]
            lesser_than_pointer += 1
    list[lesser_than_pointer], list[end] = list[end], list[lesser_than_pointer]
    quicksort(list, start, lesser_than_pointer - 1)
    quicksort(list, lesser_than_pointer + 1, end)


unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)


