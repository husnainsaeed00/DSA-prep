class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        is_col = False

        # Mark rows and columns to be zeroed out
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update matrix based on marked rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row and column if necessary
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        if is_col:
            for i in range(rows):
                matrix[i][0] = 0

# Example usage
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

solution = Solution()
solution.setZeroes(matrix1)
solution.setZeroes(matrix2)

print(matrix1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(matrix2)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
