# QUESTION 
#published by Daily Coding Problem #311 

# Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.
# An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.

def findPeak(arr):

    length = len(arr)
    start, end = 0, length - 1
    
    while start + 1 <= end:
        mid = start + (end - start) // 2

        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid] < arr[mid +1]:
            start = mid + 1
        else:
            end = mid - 1

    return arr[start]
               

# Example usage:
n = [10, 20, 30, 40, 50, 60, 70, 80, 666, 100, 90, 80]
peak = findPeak(n)
print("Peak element is:", peak)            


