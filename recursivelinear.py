def linear(i):
    f=0
    if n==l[i]:
        return i+1
    else:
        return linear(i+1)
    
l=[1,3,2,4]
i=0
n=int(input('enter element to be searched:'))
r=linear(i)
print(r)
    
          