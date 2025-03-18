class Solution:
    def isValid(self, s: str) -> bool:
        opener  = ["(", "{", "["]
        closer = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        fifo = []

        try:
            for char in s:
                if char in opener:
                    fifo.append(char)
                else:
                    if closer[char] != fifo.pop():
                        return False
        except IndexError:
            return False
        
        return True if len(fifo) == 0 else False