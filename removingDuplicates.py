class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)  # No need to remove duplicates for arrays with 0 to 2 elements
        
        k = 2  # Initialize the counter for the result length
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:  # Check if the current element is not equal to the element at k - 2
                nums[k] = nums[i]  # If not equal, place the current element at position k
                k += 1  # Increment the counter
            
        return k  # Return the final result length

# Example usage
solution = Solution()

nums1 = [1, 1, 1, 2, 2, 3]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 5 [1, 1, 2, 2, 3]

nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 7 [0, 0, 1, 1, 2, 3, 3]
