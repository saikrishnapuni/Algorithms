
class Solution:
    def removeKdigits(self, nums, k):
        stk = []

        for ch in nums:
            while stk and k > 0 and stk[-1] > ch:
                stk.pop()
                k -= 1
            stk.append(ch)

        while k > 0:
            stk.pop()
            k -= 1

        ans = ''.join(stk).lstrip('0')
        return ans if ans else "0"
            
s = Solution()
l = input()
k =  int(input())
print(s.removeKdigits(l,k))