class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        left, right = 0, len(matrix[0]) * len(matrix) - 1

        while left <= right:
            mid = (left + right ) //2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid -1

        return False