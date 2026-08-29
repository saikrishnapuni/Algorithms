class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        ans = [-1,-1]
        l = 0
        h = n-1
        while(l<=h):
            mid = (l+h)//2
            if(nums[mid] == target):
                ans[0] = mid
                h = mid-1
            elif(nums[mid]<target):
                l = mid+1
            else:
                h = mid-1
        l = 0
        h = n-1
        while(l<=h):
            mid = (l+h)//2
            if(nums[mid] == target):
                ans[1] = mid
                l = mid+1
            elif(nums[mid]<target):
                l = mid+1
            else:
                h = mid-1
        return ans
        