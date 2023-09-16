class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        left, right = 0, 10**6

        # Helper function to check if there is a path with max_diff <= mid
        def dfs(x, y, max_diff, visited):
            if x == rows - 1 and y == cols - 1:
                return True

            visited[x][y] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                    new_diff = abs(heights[new_x][new_y] - heights[x][y])
                    if new_diff <= max_diff:
                        if dfs(new_x, new_y, max_diff, visited):
                            return True

            return False

        while left < right:
            mid = (left + right) // 2
            visited = [[False] * cols for _ in range(rows)]

            if dfs(0, 0, mid, visited):
                right = mid
            else:
                left = mid + 1

        return left
