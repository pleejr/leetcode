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