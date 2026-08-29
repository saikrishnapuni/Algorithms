class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        h = n*m - 1
        while(l<=h):
            mid = (l+h)//2
            r = mid//m
            c = mid%m
            if(matrix[r][c] == target):
                return True
            elif(matrix[r][c]>target):
                h = mid-1
            else:
                l = mid+1
        return False