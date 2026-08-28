# Given an array of integers, design a Θ(n²) algorithm to decide if there exist \(i,j,k\) such that:

# A[i]+A[j]=A[k]
def solve(arr):
    n = len(arr)
    arr.sort()
    for k in range(n-1,-1,-1):
        target = arr[k]
        i = 0
        j = n-1
        while(i<j):
            if(i == k):
                i+=1
                continue
            if(j == k):
                j-=1
                continue
            if(arr[i]+arr[j] == target):
                return True
            elif(arr[i]+arr[j]>target):
                j-=1
            else:
                i+=1
    return False
print(solve([-3, 1, 2, 5]))