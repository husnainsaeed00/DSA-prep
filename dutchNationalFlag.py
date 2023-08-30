class Solution:
    def sortColors(self, nums):
        low = 0
        high = len(nums) - 1
        current = 0
        
        while current <= high:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                low += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
            else:
                current += 1

# Example usage
solution = Solution()

nums1 = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
solution.sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]
