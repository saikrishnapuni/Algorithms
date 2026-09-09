def bottomup(arr,i):
    
    while((i-1)//2>=0 and arr[i]<arr[(i-1)//2]):
        arr[i],arr[(i-1)//2] = arr[(i-1)//2],arr[i]
        i = (i-1)//2
    return 
def topdown(arr,i,n):
    while(2*i+2<n and arr[i]>min(arr[2*i+1],arr[2*i+2])):
        if(arr[2*i+1]>arr[2*i+2]):
            arr[i],arr[2*i+2] = arr[2*i+2],arr[i]
            i = 2*i+2
        else:
            arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
            i = 2*i+1
    if(2*i+1<n and arr[i]>arr[2*i+1]):
        arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
        i = 2*i+1 
def add(arr,n,val):
    if(n == 0):
        arr.append(val)
        n[0]+=1
    else:
        arr.append(val)
        n[0]+=1
        bottomup(arr,n[0]-1)
arr = [6,2,7,1,9,5,8]

#nlogn
n = [0]
heap = []

for i in arr:
    add(heap,n,i)
print(heap)
    
#floyd heap construction
 
n = len(arr)
i = n//2 - 1

while i >= 0:
    topdown(arr,i,n)
    i -= 1

print(arr)