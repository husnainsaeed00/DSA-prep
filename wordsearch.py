class Solution:
    def exist(self, board, word):
        def dfs(i, j, k):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            temp, board[i][j] = board[i][j], "/"
            found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False

# Example usage:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

solver = Solution()
print(solver.exist(board, word1))  # Output: True
print(solver.exist(board, word2))  # Output: True
print(solver.exist(board, word3))  # Output: False
