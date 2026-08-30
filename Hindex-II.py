class Solution:
    def hIndex(self, citations) :
        n = len(citations)

        l = 0
        h = n - 1

        while l <= h:
            mid = (l + h) // 2

            papers = n - mid

            if citations[mid] >= papers:
                # This h is possible.
                # Try to find a larger h.
                h = mid - 1
            else:
                # Not enough citations.
                l = mid + 1

        return n - l