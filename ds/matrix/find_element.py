# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
        """
        row_count = len(matrix)
        col_count = len(matrix[0])
        total_count = row_count * col_count
        low = 0
        high = total_count - 1
        while low <= high:
            mid = (low + high) // 2
            mid_value = matrix[mid//col_count][mid % col_count]
            if mid_value == target:
                return True
            elif mid_value < target:
                low = mid + 1
            elif mid_value > target:
                high = mid -1
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))






