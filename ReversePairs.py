class Solution:
    def reversePairs(self, nums):
        def merger(nums,l,h,mid,ans):
            temp = []
            i = l
            j = mid+1
            while(i<=mid and j<=h):
                if(nums[i]>2*nums[j]):
                    ans[0]+=(mid-i+1)
                    j+=1
                else:
                    i+=1
            i = l
            j = mid+1   
            while(i<=mid and j<=h):
                if(nums[i]<nums[j]):
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while(i<=mid):
                temp.append(nums[i])
                i+=1
            while(j<=h):
                temp.append(nums[j])
                j+=1
            for t in range(0,h-l+1):
                nums[t+l] = temp[t]
        def merge(nums,l,h,ans):
            if(l<h):
                mid = (l+h)//2

                merge(nums,l,mid,ans)
                merge(nums,mid+1,h,ans)
                merger(nums,l,h,mid,ans)

            else:
                return 
        ans = [0]
        l = 0
        n =len(nums)
        h = n-1
        merge(nums,l,h,ans)
        print(nums)
        return ans[0]