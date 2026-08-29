class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(0,n):
            if(abs(nums[i]-i)>1):
                return False
        return True