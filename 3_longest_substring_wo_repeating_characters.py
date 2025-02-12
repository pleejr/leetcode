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