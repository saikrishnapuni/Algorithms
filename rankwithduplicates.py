def solve(a, x):
    n = len(a)

    if x < 1 or x > n:
        return -1

    def quick_select(r):
        l = 0
        h = n - 1

        while l <= h:
            p = a[(l + h) // 2]
            i = l
            j = l
            k = h

            while i <= k:
                if a[i] > p:
                    a[i], a[j] = a[j], a[i]
                    i += 1
                    j += 1
                elif a[i] < p:
                    a[i], a[k] = a[k], a[i]
                    k -= 1
                else:
                    i += 1

            if r < j:
                h = j - 1
            elif r > k:
                l = k + 1
            else:
                return p

        return -1

    p = quick_select(x - 1)

    g = 0
    for v in a:
        if v > p:
            g += 1

    if g + 1 == x:
        return p

    return -1