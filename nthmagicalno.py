import math
class Solution:
    def nthMagicalNumber(self, n, a, b) :
        def lcm(a,b):
            return a*b//(math.gcd(a,b))
        def noofmultiples(val,a,b):
            l = lcm(a,b)
            return val//a + val//b - val//l
        m = 10**9 + 7
        l = 1
        h = 10**18
        ans = 0
        while(l<=h):
            mid = l + (h-l)//2
            if(noofmultiples(mid,a,b)>=n):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans%m