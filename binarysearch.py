def binarysearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
n=int(input('enter the size of the list:'))
l=[]
low=0
high=n-1
for i in range(0,n):
    ele=int(input('enter the elements:'))
    l.append(ele)
l.sort()
print(l)
key=int(input('enter the value to search:'))
result=binarysearch(l,low,high,key)
if result==-1:
    print('element is not found')
else:
    print('element is found at',result)
        