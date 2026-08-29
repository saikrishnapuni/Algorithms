# Question

# Given a sorted array \(A\) of \(n\) integers, consider all values

# $$ A[j]-A[i], \qquad i<j $$

# Design an efficient algorithm to find the element of rank \(k\) among these differences.

# Convention: Rank 1 is the largest difference.
def find_rank(mid, arr, n):
    c = 0
    i = 0
    j = 1

    while i < n and j < n:
        while j < n and (i == j or arr[j] - arr[i] <= mid):
            j += 1

        c += n - j
        i += 1

    return c


def solve(arr, k):
    n = len(arr)

    mini = min(arr[i + 1] - arr[i] for i in range(n - 1))
    maxi = arr[n - 1] - arr[0]

    while mini <= maxi:
        mid = (mini + maxi) // 2
        r = find_rank(mid, arr, n)

        if r >= k:
            mini = mid + 1
        else:
            maxi = mid - 1

    return mini
print(solve([1, 3, 5, 8], 3))