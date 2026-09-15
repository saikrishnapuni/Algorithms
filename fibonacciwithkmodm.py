def mat_mul(A, B, m):
    n = len(A)
    p = len(B)
    q = len(B[0])

    C = [[0] * q for _ in range(n)]

    for i in range(n):
        for j in range(q):
            s = 0
            for x in range(p):
                s = (s + A[i][x] * B[x][j]) % m
            C[i][j] = s

    return C


def mat_pow(A, power, m):
    n = len(A)

    R = [[0] * n for _ in range(n)]
    for i in range(n):
        R[i][i] = 1

    while power:
        if power & 1:
            R = mat_mul(R, A, m)

        A = mat_mul(A, A, m)
        power >>= 1

    return R


n, m, k = map(int, input().split())

if n <= k:
    print(n % m)
else:
    T = [[0] * k for _ in range(k)]

    T[0][0] = 1
    T[0][k - 1] = 1

    for i in range(1, k):
        T[i][i - 1] = 1

    state = [[i % m] for i in range(k, 0, -1)]

    T = mat_pow(T, n - k, m)

    ans = mat_mul(T, state, m)

    print(ans[0][0] % m)