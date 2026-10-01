
# class Segement:
#     def __init__(self,arr,n):
#         self.arr = arr
#         self.n = n
        
#         k = 1
        
#         while(k<self.n):
#             k = k*2
#         self.segment = [0 for i in range(k)]
        
#         for i in range(0,n):
#             self.segment[i] = arr[i]
        
#         self.segment = [0]*(len(self.segment)-1)+self.segment
#         i = len(self.segment)-k-1
        
#         while(i>-1):
#             self.segment[i] = self.segment[2*i+1]+self.segment[2*i+2]
#             i-=1
#         print(self.segment) 
#         self.k = k
#         self.len = len(self.segment)
#     def query(self,lower,higher):
#         i = 0
#         ans = 0
#         while()
        
# arr = [-2,5,-1]
# print(sum(arr))
# s = Segement(arr,len(arr))


import bisect


class Segment:
    def __init__(self, n):
        self.k = 1
        self.n = n

        while self.k <= n:
            self.k = self.k * 2

        self.segment = [0 for i in range(2 * self.k - 1)]

    def update(self, ind, ss, se, val, i):
        while ss <= se:
            self.segment[i] += val

            if ss == se:
                break

            mid = (ss + se) // 2

            if ind <= mid:
                i = 2 * i + 1
                se = mid
            else:
                i = 2 * i + 2
                ss = mid + 1

    def query(self, i, ss, se, l, h):
        if l <= ss and se <= h:
            return self.segment[i]

        if l > se or h < ss:
            return 0

        mid = (ss + se) // 2

        left = self.query(2 * i + 1, ss, mid, l, h)
        right = self.query(2 * i + 2, mid + 1, se, l, h)

        return left + right


class Solution:
    def lowerArray(self, arr):
        n = len(arr)

        sarr = list(set(arr))
        sarr.sort()

        d = {sarr[i]: i for i in range(len(sarr))}

        ans = [0 for i in range(n)]

        arr = arr[::-1]

        s = Segment(len(d))

        se = s.k - 1
        ss = 0

        for i in range(0, n):
            right = bisect.bisect_left(sarr, arr[i]) - 1

            ans[i] = s.query(0, ss, se, 0, right)

            s.update(d[arr[i]], ss, se, 1, 0)

        return ans[::-1]
s = Solution()
print(s.lowerArray([12, 1, 2, 3, 0, 11, 4]))