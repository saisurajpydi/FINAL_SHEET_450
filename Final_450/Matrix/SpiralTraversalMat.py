def spirallyTraverse(matrix, r, c): 
    # code here 
    top = 0
    down = r - 1
    left = 0 
    right = c - 1
    dir = 0
    while ( top <= down and left <= right):
        if(dir == 0):
            for i in range( left , right+1):
                print(matrix[top][i],end = " ")
            top += 1
        elif(dir == 1):
            for i in range( top , down+1):
                print(matrix[i][right], end = " ")
            right -= 1
        elif(dir == 2):
            for i in range( right , left+1,-1):
                print(matrix[down][i],end = " ")
            down -= 1
        elif(dir == 3):
            for i in range( down , top+1§§§§§§, -1):
                print(matrix[i][left],end = " ")
            left += 1
        dir = (dir + 1) % 4

r = int( input ("enter the row"))
c = int(input("enter the col"))
matrix = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
print(matrix)
spirallyTraverse(matrix, r, c) 