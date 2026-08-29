import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k) :
        heap = []
        i = 0
        j = 0
        ans = set()
        heapq.heappush(heap,(nums1[i]+nums2[j],i,j))
        n = len(nums1)
        m = len(nums2)
        while(k>0 and heap):
            v,i,j = heapq.heappop(heap)
            if((nums1[i],nums2[j]) not in ans):
                ans.add((nums1[i],nums2[j]))
                k-=1
            if(i+1<n):
                heapq.heappush(heap,[nums1[i+1]+nums2[j],i+1,j])
            if(j+1<m):
                heapq.heappush(heap,[nums1[i]+nums2[j+1],i,j+1])
        print(ans)
        ans1 = []
        for i in ans:
            ans1.append(list(i))
        ans.sort()
        return ans