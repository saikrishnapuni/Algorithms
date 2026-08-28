# Question 10

# Given an array of sorted integers and an integer \(X>0\), design a linear-time algorithm to count the number of pairs of elements in the array such that:

# A[j]−A[i]>X

def solve(arr,x):
    n = len(arr)
    c = 0
    i=0
    j = 1
    while(j<n):
        if(arr[j]-arr[i]>x):
            c+=(n-j)
            i+=1
        else:
            j+=1
    return c
print(solve([1, 3, 5, 8, 10, 14],5))
        