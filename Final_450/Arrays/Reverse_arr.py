"""
lst = []
n = int(input("Enter the size of the list : "))
for i in range(n):
    ele = int(input(" "))
    list.append(ele)
print(lst)
print("the reverse of the list is ")
print(lst.reverse())
"""
# creating an empty list 
lst = [] 

# number of elemetns as input 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 

	lst.append(ele) # adding the element 
lst.reverse()
print(lst) 
