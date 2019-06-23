def binary_search(sorted_list, target):
    if not sorted_list:
        return "value not found"
    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    elif mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)
    elif mid_val < target:
        right_half = sorted_list[mid_idx + 1:]
        result = binary_search(right_half, target)
        if result == "value not found":
            return result
        return result + mid_idx + 1


def binary_search_pointers(sorted_list, left_pointer, right_pointer, target):
    if left_pointer >= right_pointer:
        return "value not found"
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        return binary_search_pointers(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        return binary_search_pointers(sorted_list, mid_idx + 1, right_pointer, target)


def binary_search_iter(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)
    while(left_pointer < right_pointer):
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = sorted_list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
            right_pointer = mid_idx
        if target > mid_val:
            left_pointer = mid_idx + 1
    return "value not in list"
