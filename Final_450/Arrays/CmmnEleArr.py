"""
a1 = [1, 5, 10, 20, 40, 80]
a2 = [6, 7, 20, 80, 100]
a3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(a1)
n2 = len(a2)
n3 = len(a3)
com = []
for i in range(n1):
    for j in range(n2):
        if(a1[i] == a2[j]):
            com.append(a1[i])
c = len(com)
for i in range(c):
    for j in range(n3):
        if(com[i] == a3[j]):
            print(com[i],end = " ")

"""
a1 = [1, 5, 10, 20, 40, 80]
a2 = [6, 7, 20, 80, 100]
a3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(a1)
n2 = len(a2)
n3 = len(a3)
x = 0
y = 0
z = 0
while ( x < n1 and y < n2 and z < n3):
    if( a1[x] == a2[y] and a2[y] == a3[z]):
        print ( a1[x] ," ")
        x += 1
        y += 1
        z += 1
    elif (a1[x] < a2[y]):
        x += 1
    elif (a2[y] < a3[z]):
        y += 1
    else:
        z += 1