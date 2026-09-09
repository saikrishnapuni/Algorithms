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
def getmin(arr):
    return arr[0]
def delmin(arr,n):
    if(n[0]<1):
        return "delete not possible"
    arr[0],arr[n[0]-1] = arr[n[0]-1],arr[0]
    arr.pop()
    n[0]-=1
    topdown(arr,0,n[0])
    
n = [0]
arr = []
add(arr,n,10)
add(arr,n,6)
add(arr,n,7)
add(arr,n,5)
add(arr,n,2)

print(arr)
print(getmin(arr))
delmin(arr,n)
print(arr)