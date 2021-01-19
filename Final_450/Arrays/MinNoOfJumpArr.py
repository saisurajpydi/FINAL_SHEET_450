# Given an array of integers where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
arr = []
n = int(input("enter the size of the array  : "))
for i in range(n):
    arr.append(int(input()))
jump = 0
i = 0
while (n >= 0):
    if(arr[i] > 0):
        n = n-arr[i]-1
        jump = jump + 1
    elif(arr[i] == 0):
        print("sry can't move ")
    i = i + 1
print("the number of jumps is ",jump)