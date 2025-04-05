# 3. Longest Substring Without Repeating Characters
# MEDIUM
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = {"substring": ""}
        for char in s:
            if char not in seen:
                seen[char] = None
                seen["substring"] = char + seen["substring"]
            else:
                print(f"char: {char}")
                print(f"subs: {seen['substring']}")                
                last_occurrence = seen["substring"].index(char)
                for dup_char in seen["substring"][last_occurrence:]:
                    seen.pop(dup_char)
                seen["substring"] = char + seen["substring"][:last_occurrence]
                seen[char] = None
            max_length = max(len(seen["substring"]), max_length)
        return max_length