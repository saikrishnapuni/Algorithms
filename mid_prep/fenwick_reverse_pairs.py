from bisect import  bisect_left
class Fenwick:
    def __init__(self,n):
        self.n = n
        self.bit = [0 for i in range(self.n+1)]
    def update(self,i,val):
        while(i<self.n+1):
            self.bit[i] +=val
            i = i+(i&(-i))
    def query(self,i):
        ans = 0
        while(i>0):
            ans+=self.bit[i]
            i = i-(i&(-i))
        return ans
class Solution:
    def reversePairs(self, nums):
        d = {}
        s_nums = list(set(nums))
        s_nums.sort()
        n = len(nums)
        for i in range(0,len(s_nums)):
            d[s_nums[i]] = i+1
        c = 0
        f = Fenwick(len(d))
        for i in range(n-1,-1,-1):
            idx = bisect_left(s_nums,(nums[i]+1)//2)
            c+=f.query(idx)
            f.update(d[nums[i]],1)
        return c
s = Solution()
print(s.reversePairs([6, 4, 1, 2, 7]))