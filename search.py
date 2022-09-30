l=[]
n=int(input('enter no of elements:'))
print('enter element')
for i in range(n):
    e=int(input())
    l.append(e)
x=int(input('enter the element to be found:'))
f=0
for i in range(n):
    if x==l[i]:
        f=1
        print('element found at:',i+1)
        break
    else:
        i=i+1
if f==0:
    print('element not present in the list')
        