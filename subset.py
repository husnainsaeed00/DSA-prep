class Solution:
    def subsets(self, nums):
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result

# Example usage:
nums1 = [1, 2, 3]
nums2 = [0]

solver = Solution()
print(solver.subsets(nums1))
print(solver.subsets(nums2))
