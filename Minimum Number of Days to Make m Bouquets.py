class Solution:
    def minDays(self, b, m, k) :
        n = len(b)
        if(k>n):
            return -1
        l = min(b)
        h = max(b)
        ans = -1
        while(l<=h):
            mid = (l+h)//2
            sumi = 0
            c= 0
            for i in b:
                if(i<=mid):
                    c+=1
                else:
                    if(c>=k):
                        sumi+=1
                    c = 0
                    
                if(c>=k):
                    sumi+=1
                    c = 0
            if(c >=k):
                sumi+=1
            if(sumi>=m):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans