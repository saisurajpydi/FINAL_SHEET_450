arr = [4,3,1,2,8,0] #431802[9,1,2,4,3,1,0]#9130124
n = len(arr)
point1 = 0
point2 = 0
for i in range( n-1,0,-1):
    if (arr[i-1] < arr[i] ):
        point1 = i
print("point 1 ",point1)
for i in range( n-1,-1,-1):    
    if(arr[i] > point1):
        point2 = i
        break
print("point 2 ",point2)
print(arr)
arr[point1],arr[point2]= arr[point2],arr[point1]
temp = []
for i in range (point1+1):
    temp.append(arr[i])
for i in range( n-1,point1,-1):
    temp.append(arr[i])
print("next permutation is : ",temp)
       