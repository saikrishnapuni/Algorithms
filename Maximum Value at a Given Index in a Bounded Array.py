class Solution:
    def maxValue(self, n, index, maxsum) :

        def reduction(mid, k):
            if k < mid:
                return k * (k + 1) // 2
            else:
                return (mid - 1) * mid // 2 + (k - mid + 1) * (mid - 1)

        l = 1
        h = maxsum
        ans = 1

        while l <= h:
            mid = (l + h) // 2

            nums = mid * n

            left = reduction(mid, index)
            right = reduction(mid, n - index - 1)

            nums -= left + right

            if nums <= maxsum:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1

        return ans