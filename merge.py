def merge_lists(x,y):
    l=[]
    l.extend(x)
    l.extend(y)
    l.sort()
    return(l)
x=[]
y=[]
print('enter first list elements:')
for i in range(4):
    j=int(input())
    x.append(j)
print('enter second list elements:')
for i in range(4):
    j=int(input())
    y.append(j)
res=merge_lists(x,y)
print('after merging lists is:',res)
