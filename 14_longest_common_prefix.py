# 14. Longest Common Prefix
# EASY
# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "". 

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        try:
            for i in range(len(strs[0])):
                for s in strs:
                    if strs[0][i] != s[i]:
                        return prefix
                prefix += s[i]
        except IndexError:
            return prefix

        return prefix