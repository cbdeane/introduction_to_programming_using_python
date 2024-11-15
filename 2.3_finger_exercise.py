import numpy as np

def largestOdd(arr):
    odds = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            odds.append(arr[i])
    if len(odds) == 0:
        print("No odd numbers in the list")
        return None
    else:
        max = odds[0]
        for i in range(len(odds)):
            if odds[i] > max:
                max = odds[i]
        print("The largest odd number in the list is: ", max)
        return max

arr = []
user_input = 0
for i in range(10):
    user_input = int(input("Enter a number: "))
    arr.append(user_input)
print("The list is: ", arr)
largestOdd(arr)
