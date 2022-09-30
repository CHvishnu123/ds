arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
size = len(arr)
for i in range(1,size):
    j = i-1
    current_element = arr[i]
    while j>=0 and arr[j]>current_element:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = current_element  
print("The sorted list is: ",arr)
