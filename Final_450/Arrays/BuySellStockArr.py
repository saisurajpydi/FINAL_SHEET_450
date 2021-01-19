"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
arr = []
n = int(input("enter the size of the array"))
print("enter the prices of the stocks ")
for i in range(n):
    arr.append(int(input()))
profit = 0 
for i in range(n):
    for j in range(i+1,n):
        if( arr[i] < arr[j]):
            profit = max( profit,arr[j]-arr[i])
print("the max is profit : ",profit )
