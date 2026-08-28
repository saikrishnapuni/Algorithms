
#  Given an array of integers , design an efficient algorithm to decide if there is
# i, j, k, l such that A[i] − 2A[j] = A[k] − 3A[l].
def pairsExist(arr):
    n = len(arr)

    arr.sort()

    for i in range(n):
        for l in range(n):

            if i == l:
                continue

            k = 0
            j = n - 1

            target = arr[i] + 3 * arr[l]

            while k < j:

                if k == i or k == l:
                    k += 1
                    continue

                if j == i or j == l:
                    j -= 1
                    continue

                current_sum = arr[k] + 2 * arr[j]

                if target == current_sum:
                    return True

                elif current_sum < target:
                    k += 1

                else:
                    j -= 1

    return False


n = int(input())
arr = list(map(int, input().split()))

print(pairsExist(arr))