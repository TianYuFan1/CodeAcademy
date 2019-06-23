
def bubble_sort(arr):
    for el in arr:
        for idx in range(len(arr) - 1 ):
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)


def bubble_sort_optimized(arr):
    for num in range(len(arr)):
        for idx in range(len(arr) - 1 - num):
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)


def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


nums = [5, 2, 9, 1, 5, 6]
print("Pre-Sort: {0}".format(nums))
bubble_sort_optimized(nums)
print("Post-Sort: {0}".format(nums))
