# Question

# Given a sorted array \(A\) of \(n\) integers, consider all values of

# $$ A[i]+A[j], \qquad i<j $$

# Design an efficient algorithm to find the element of rank \(k\) among these sums.

# Convention: Rank 1 is the largest sum.

def count_ge(arr, x):
    n = len(arr)

    i = 0
    j = n - 1
    count = 0

    while i < j:
        if arr[i] + arr[j] >= x:
            
            count += j - i
            j -= 1
        else:
            i += 1

    return count


def solve(arr, k):
    n = len(arr)

    low = arr[0] + arr[1]
    high = arr[n - 2] + arr[n - 1]

    while low <= high:
        mid = (low + high) // 2

        count = count_ge(arr, mid)

        if count >= k:
            
            low = mid + 1
        else:
            high = mid - 1

    return high


A = [1, 3, 5, 8]
k = 3

print(solve(A, k))