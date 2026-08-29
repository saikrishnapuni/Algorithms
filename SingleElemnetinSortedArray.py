class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        if(n == 1):
            return nums[0]
        if(nums[0]!=nums[1]):
            return nums[0]
        if(nums[-1]!=nums[-2]):
            return nums[-1]
        l = 1
        h = n-2
        while(l<=h):
            mid = (l+h)//2
            if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
                return nums[mid]
            elif(nums[mid] == nums[mid-1]):
                if(mid%2 == 0):
                    h = mid-1
                else:
                    l = mid+1
            else:
                if(mid%2 == 0):
                    l = mid+1
                else:
                    h = mid-1
        return -1