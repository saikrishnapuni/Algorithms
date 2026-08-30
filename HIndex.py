class Solution:
    def hIndex(self, cit):
        l = 0
        h = max(cit)
        ans = 1
        while(l<=h):
            mid = (l+h)//2
            sumi = 0
            for i in cit:
                if(i>=mid):
                    sumi+=1
            if(sumi>=mid):
                ans = mid
                l = mid+1
            else:
                h = mid-1
        return ans