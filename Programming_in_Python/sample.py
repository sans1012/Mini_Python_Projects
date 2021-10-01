from array import *
from random import randint

# function to display the arrya
def display(arr,n):
    for i in range(0,n):
        print(a[i], end =" ")
 
#helper function for merge sort- will merge the array
def mergeSort(a, l,m,h):
    #number of elements in first subarray
    n1=m-l+1
    #number of element in second subarray
    n2=h-m
    
    #Create 2 temp array left, right with all element =0
    L=[0]*(n1)
    R=[0]*(n2)
    
    #left subarray
    for i in range(0, n1):
        L[i]=a[l+i]
        
    for j  in range(0,n2):
        R[j]=a[m+1+j]
        
    #initial indexes    
    i=0
    j=0
    k=l
    while(i<n1 and j<n2):
        if (L[i]<=R[j]):
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1
        
        #inserting the remaining elements to the array
    while i<n1:
          a[k]=L[i]
          i+=1
          k+=1

    while j<n2:
          a[k]=R[j]
          j+=1
          k+=1
 
#function for dividing the array.
def merge(a,low,high):
    if (low<high):
        mid=(low+(high-1))//2
        merge(a, low, mid)
        merge(a, mid+1, high)
        mergeSort(a, low, mid, high)
    return a     

a=array("i",[])

#randomly inserting 10 elements to the array
i=0
while(i<10):
    a.insert(i,randint(0,100))
    i+=1
    
print("Array before merge sort: ")
display(a,10)

print("\n Array after merge sort: ")
display(merge(a,0,9),len(a))
