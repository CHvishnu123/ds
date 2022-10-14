def binarysearch(arr,x):
    low=0
    high=len(arr-1)
    mid=0
    while low<=high:
       mid=(high+low)/2
       if arr[mid]<x:
           low=mid+1
       elif arr[mid]>x:
           high=mid-1
       else:
           return mid
    return -1
arr=list[i for i in int(input('enter the elements:')).split()]
x=int(input('enter the element to search:'))
result=binarysearch(arr,x)
if result!=-1:
    print('element is present at index:',str(resutl))
else:
    print('element is not present in the array')