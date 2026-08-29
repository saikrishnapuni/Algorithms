def find_rank(A, B, C, la, lb, lc, ha, hb, hc, k, n, m, t):

    # Rank 1 = largest
    if k == 1:
        ans = float("-inf")

        if la <= ha:
            ans = max(ans, A[ha])

        if lb <= hb:
            ans = max(ans, B[hb])

        if lc <= hc:
            ans = max(ans, C[hc])

        return ans

    # Number of remaining elements
    na = ha - la + 1 if la <= ha else 0
    nb = hb - lb + 1 if lb <= hb else 0
    nc = hc - lc + 1 if lc <= hc else 0

    # If only one array remains
    if nb == 0 and nc == 0:
        return A[ha - k + 1]

    if na == 0 and nc == 0:
        return B[hb - k + 1]

    if na == 0 and nb == 0:
        return C[hc - k + 1]

    # If one array is empty, reduce to 2 arrays
    if na == 0:

        x = min(k // 2, nb)
        y = min(k // 2, nc)

        vb = B[hb - x + 1] if x > 0 else float("-inf")
        vc = C[hc - y + 1] if y > 0 else float("-inf")

        if vb >= vc:
            return find_rank(
                A, B, C,
                la, lb, lc,
                ha, hb - x, hc,
                k - x, n, m, t
            )
        else:
            return find_rank(
                A, B, C,
                la, lb, lc,
                ha, hb, hc - y,
                k - y, n, m, t
            )

    if nb == 0:

        x = min(k // 2, na)
        y = min(k // 2, nc)

        va = A[ha - x + 1] if x > 0 else float("-inf")
        vc = C[hc - y + 1] if y > 0 else float("-inf")

        if va >= vc:
            return find_rank(
                A, B, C,
                la, lb, lc,
                ha - x, hb, hc,
                k - x, n, m, t
            )
        else:
            return find_rank(
                A, B, C,
                la, lb, lc,
                ha, hb, hc - y,
                k - y, n, m, t
            )

    if nc == 0:

        x = min(k // 2, na)
        y = min(k // 2, nb)

        va = A[ha - x + 1] if x > 0 else float("-inf")
        vb = B[hb - y + 1] if y > 0 else float("-inf")

        if va >= vb:
            return find_rank(
                A, B, C,
                la, lb, lc,
                ha - x, hb, hc,
                k - x, n, m, t
            )
        else:
            return find_rank(
                A, B, C,
                la, lb, lc,
                ha, hb - y, hc,
                k - y, n, m, t
            )

    # ------------------------------------------------
    # All three arrays are non-empty
    # ------------------------------------------------

    x = k // 3

    if x == 0:
        # k = 2
        vals = [
            (A[ha], 'A'),
            (B[hb], 'B'),
            (C[hc], 'C')
        ]

        vals.sort(reverse=True)

        # second largest
        return vals[1][0]

    xa = min(x, na)
    xb = min(x, nb)
    xc = min(x, nc)

    va = A[ha - xa + 1]
    vb = B[hb - xb + 1]
    vc = C[hc - xc + 1]

    # Largest candidate belongs to A
    if va >= vb and va >= vc:

        return find_rank(
            A, B, C,
            la, lb, lc,
            ha - xa, hb, hc,
            k - xa,
            n, m, t
        )

    # Largest candidate belongs to B
    elif vb >= va and vb >= vc:

        return find_rank(
            A, B, C,
            la, lb, lc,
            ha, hb - xb, hc,
            k - xb,
            n, m, t
        )

    # Largest candidate belongs to C
    else:

        return find_rank(
            A, B, C,
            la, lb, lc,
            ha, hb, hc - xc,
            k - xc,
            n, m, t
        )


def solve(A, B, C, k):

    n = len(A)
    m = len(B)
    t = len(C)

    return find_rank(
        A, B, C,
        0, 0, 0,
        n - 1, m - 1, t - 1,
        k, n, m, t
    )


A = [1, 5, 9]
B = [2, 6, 10]
C = [3, 7, 11]

k = 4

print(solve(A, B, C, k))