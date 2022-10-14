def insertionsort(a):
    for i in range(1,n):
        key=a[i]
        j=i-1
    while j==0 and key<a[j]:
        a[j+1]=a[i]
        j=i-1
        a[j+1]=key
    return a
n=int(input('enter no of elements:'))
a=[]
print('enter elements:')
for i in range(n):
    a.append(i)
print(a)
print('resultant list is:',insertionsort(a))