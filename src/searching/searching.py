from typing import List


def linear_search(arr: List[int], target: int) -> int:
    for index, number in enumerate(arr):
        if number is target:
            return index

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr: List[int], target: int) -> int:
    if len(arr) > 0:
        left = 0
        right = len(arr) - 1

        while left != right:
            middle = (right - left) // 2
            if arr[left] is target:
                return left

            if arr[middle] is target:
                return middle

            if arr[right] is target:
                return right

            if target < arr[middle]:
                right = middle
            else:
                left = middle

    return -1  # not found
