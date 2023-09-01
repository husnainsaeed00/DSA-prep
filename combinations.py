class Solution:
    def combine(self, n, k):
        def backtrack(start, path):
            if len(path) == k:
                combinations.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        combinations = []
        backtrack(1, [])
        return combinations

# Example usage
solution = Solution()

n1, k1 = 4, 2
result1 = solution.combine(n1, k1)
print(result1)

n2, k2 = 1, 1
result2 = solution.combine(n2, k2)
print(result2)
