arr = []
n = int(input("Enter No. of TestCases : "))
print("enter ",n," values ")
for i in range(n):
    arr.append(int(input()))
print(arr)

def fac(arr):
    result = []
    fact = 1
    if( arr > 1):
        for j in range(1,arr):
            fact = fact + (fact*j)
        print(fact, end = " " )
    if(arr == 0 or arr == 1):
        print(1,end = " ")

for i in range(n):
    fac(arr[i])