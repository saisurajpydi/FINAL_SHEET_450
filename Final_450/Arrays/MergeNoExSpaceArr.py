"""
def merge(ar1, ar2, m, n): 
    # Iterate through all 
    # elements of ar2[] starting from 
    # the last element 
    for i in range(n-1, -1, -1): 
        # Find the smallest element 
        # greater than ar2[i]. Move all 
        # elements one position ahead 
        # till the smallest greater 
        # element is not found  
        last = ar1[m-1] 
        j=m-2
        while(j >= 0 and ar1[j] > ar2[i]): 
            ar1[j+1] = ar1[j] 
            j-=1
   
        # If there was a greater element 
        if (j != m-2 or last > ar2[i]): 
          
            ar1[j+1] = ar2[i] 
            ar2[i] = last 
   
# Driver program 
  
ar1 = [1, 5, 9, 10, 15, 20] 
ar2 = [2, 3, 8, 13] 
m = len(ar1) 
n = len(ar2) 
  
merge(ar1, ar2, m, n) 
   
print("After Merging \nFirst Array:", end="") 
for i in range(m): 
    print(ar1[i] , " ", end="") 
  
print("\nSecond Array: ", end="") 
for i in range(n): 
    print(ar2[i] , " ", end="") 
  """
# method 2 using gap
ar1 = [1, 5, 9, 10, 15, 20] 
ar2 = [2, 3, 8, 13] 
m = len(ar1) 
n = len(ar2) 

def nextGap( gap):
    if(gap <= 1):
        return 0
    return (gap // 2) + (gap % 2)
    
gap = m + n
gap = nextGap(gap)
while gap > 0:
    i = 0
    while i + gap < m:
        if( arr1[i] > arr1[i + gap]):
            arr1[i],arr1[i+gap] = arr1[i+gap],arr1[i]
        i += 1

    j = gap - m if gap > m else 0
    while i < m and j < n :
        if( arr1[i] > arr2[j]):
            arr1[i],arr2[j] = arr2[j],arr1[i]    
        j += 1
        i += 1


    if(j<n):
        j = 0
        while j + gap < n:
            if( arr2[j] > arr2[j + gap]):
                arr2[j],arr2[j+gap] = arr2[j+gap],arr2[j]
            j += 1
        
    gap = nextGap(gap)