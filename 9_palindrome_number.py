class Solution:
    def isPalindrome(self, x: int) -> bool:
        elements = []

        if abs(x) != x:
            return False

        while x != 0:
            mod = x % 10
            elements.append(mod)
            x = x // 10

        for i in range(len(elements)//2):
            if elements[i] != elements[len(elements)-1-i]:
                return False

        return True
    
x = -121
tmp = Solution()
print(tmp.isPalindrome(x))