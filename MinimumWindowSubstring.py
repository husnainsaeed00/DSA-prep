from collections import Counter

class Solution:
    def minWindow(self, s, t):
        target_count = Counter(t)
        window_count = Counter()
        required_chars = len(target_count)
        
        left, right = 0, 0
        min_len = float('inf')
        result = ""
        
        while right < len(s):
            char = s[right]
            window_count[char] += 1
            
            while left <= right and all(window_count[c] >= target_count[c] for c in target_count):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]
                
                window_count[s[left]] -= 1
                if window_count[s[left]] < target_count[s[left]]:
                    required_chars += 1
                
                left += 1
            
            right += 1
        
        return result

# Example usage
solution = Solution()

s1 = "ADOBECODEBANC"
t1 = "ABC"
print(solution.minWindow(s1, t1))  # Output: "BANC"

s2 = "a"
t2 = "a"
print(solution.minWindow(s2, t2))  # Output: "a"

s3 = "a"
t3 = "aa"
print(solution.minWindow(s3, t3))  # Output: ""
