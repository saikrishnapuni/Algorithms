import sys

class Segment:
    def __init__(self, arr, n):
        self.n = n
        self.k = 1

        while self.k < n:
            self.k *= 2

        size = 2 * self.k - 1

        self.mx = [float("-inf")] * size
        self.lazy = [0] * size

        for i in range(n):
            self.mx[self.k - 1 + i] = arr[i]

        for i in range(self.k - 2, -1, -1):
            self.mx[i] = max(self.mx[2*i+1], self.mx[2*i+2])

    def apply(self, i, v):
        self.mx[i] += v
        self.lazy[i] += v

    def push(self, i):
        v = self.lazy[i]

        if v != 0:
            self.apply(2*i+1, v)
            self.apply(2*i+2, v)
            self.lazy[i] = 0

    def update(self, i, ss, se, l, r, v):
        if l > se or r < ss:
            return

        if l <= ss and se <= r:
            self.apply(i, v)
            return

        self.push(i)

        mid = (ss + se) // 2

        self.update(2*i+1, ss, mid, l, r, v)
        self.update(2*i+2, mid+1, se, l, r, v)

        self.mx[i] = max(self.mx[2*i+1], self.mx[2*i+2])

    def query(self, i, ss, se, l, r):
        if l > se or r < ss:
            return float("-inf")

        if l <= ss and se <= r:
            return self.mx[i]

        self.push(i)

        mid = (ss + se) // 2

        return max(
            self.query(2*i+1, ss, mid, l, r),
            self.query(2*i+2, mid+1, se, l, r)
        )

    def find(self, i, ss, se, l, r, v):
        if l > se or r < ss or self.mx[i] < v:
            return self.n

        if ss == se:
            return ss

        self.push(i)

        mid = (ss + se) // 2

        ans = self.find(2*i+1, ss, mid, l, r, v)

        if ans != self.n:
            return ans

        return self.find(2*i+2, mid+1, se, l, r, v)


data = iter(map(int, sys.stdin.buffer.read().split()))

n = next(data)
q = next(data)

arr = [next(data) for _ in range(n)]

s = Segment(arr, n)

ans = []

for _ in range(q):
    typ = next(data)
    l = next(data) - 1
    r = next(data) - 1

    if typ == 1:
        v = next(data)
        s.update(0, 0, s.k-1, l, r, v)

    elif typ == 2:
        v = next(data)
        a = s.find(0, 0, s.k-1, l, r, v)

        ans.append(str(-1 if a == n else a+1))

    else:
        ans.append(str(s.query(0, 0, s.k-1, l, r)))

sys.stdout.write("\n".join(ans))