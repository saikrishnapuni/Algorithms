class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & (-i)

    def query(self, i):
        c = 0
        while i > 0:
            c += self.bit[i]
            i -= i & (-i)
        return c


class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)

        pos = {nums2[i]:i for i in range(n)}
        arr = []
        for i in nums1:
            arr.append(pos[i])
        left = [0 for i in range(n)]
        fen = Fenwick(n)
        for i in range(0,n):
            left[arr[i]] = fen.query(arr[i])
            fen.update(arr[i]+1,1)
        right = [0 for i in range(n)]
        fen = Fenwick(n)
        s=0
        for i in range(n-1,-1,-1):
            right[arr[i]] = s-fen.query(arr[i]+1)
            fen.update(arr[i]+1,1)
            s+=1
        ans = 0
        for i in range(n):
            ans = ans+(left[i]*right[i])
        return ans
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = Solution()
print(s.goodTriplets(a,b))