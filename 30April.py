# QUESTION 
#published by Daily Coding Problem #1706 

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

def findLongestStreak(arr):
    
    #I have "cheated" and pre-sorted the array
    arr.sort()
    length = len(arr)
    streakCounter = 1
    longestStreak = 1

    for i in range(length - 1):
        
        if arr[i] == arr[i+1]:
            continue
        if arr[i+1] == arr[i] + 1:  # Check if the next element is one more than the current element
            streakCounter += 1  # Increment streak counter
        else:
            streakCounter = 1  # Reset streak counter if not part of the streak
        
        if streakCounter > longestStreak:
            longestStreak = streakCounter

    return longestStreak

# the example they gave:
arr = [100, 4, 200, 1, 3, 2]
longest_streak = findLongestStreak(arr)
print("Longest streak length:", longest_streak)


