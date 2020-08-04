from itertools import repeat
from typing import List, Union


def selection_sort(arr: List[int]) -> List[int]:
    smallest = 0
    while smallest < len(arr) - 1:
        index = smallest + 1
        while index < len(arr):
            if arr[index] < arr[smallest]:
                arr[smallest], arr[index] = arr[index], arr[smallest]

            index += 1
        smallest += 1
    return arr


def bubble_sort(arr: List[int]) -> List[int]:
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True

    return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr: List[int], maximum: int = 0) -> Union[str, List[int]]:
    if len(arr) > 0:
        buckets = [0] * (maximum + 1)
        for number in arr:
            if number < 0:
                return "Error, negative numbers not allowed in Count Sort"
            buckets[number] = arr.count(number)

        arr.clear()
        for index, number in enumerate(buckets):
            arr.extend(repeat(index, number))

    return arr
