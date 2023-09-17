class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        if n == 1:
            return 0

        # Initialize a DP table with dimensions (1 << n) x n
        dp = [[float('inf')] * n for _ in range(1 << n)]

        # Initialize the starting state
        for i in range(n):
            dp[1 << i][i] = 0

        # Iterate through all possible states
        for mask in range(1 << n):
            for u in range(n):
                if (mask >> u) & 1:
                    for v in graph[u]:
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + 1)

        # Find the minimum length of the path that visits all nodes
        ans = min(dp[-1])

        return ans

# Example usage:
graph1 = [[1, 2, 3], [0], [0], [0]]
graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]

solution = Solution()
print(solution.shortestPathLength(graph1))  # Output: 4
print(solution.shortestPathLength(graph2))  # Output: 4
