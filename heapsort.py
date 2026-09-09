
def topdown(arr,i,n):
    while(2*i+2<n and arr[i]<max(arr[2*i+1],arr[2*i+2])):
        if(arr[2*i+1]<arr[2*i+2]):
            arr[i],arr[2*i+2] = arr[2*i+2],arr[i]
            i = 2*i+2
        else:
            arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
            i = 2*i+1
    if(2*i+1<n and arr[i]<arr[2*i+1]):
        arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
        i = 2*i+1 

arr = [6,2,7,1,9,5,8,3,3,3,3,3,3]


    

 
n = len(arr)
i = n//2 - 1

while i >= 0:
    topdown(arr,i,n)
    i -= 1

print(arr)
n = len(arr)
def heapsort(arr,n):
    while(n>0):
        arr[0],arr[n-1] = arr[n-1],arr[0]
        n-=1
        topdown(arr,0,n)
heapsort(arr,n)
print(arr)