# These three exercises were given in a live coding interview for an unnamed employer in 2024.

# 1. Given a string of characters as input, output the number of times a character appears in the string followed by the character itself.
#   AAABBCDDD -> 3A2B1C3D

from collections import Counter

def countChars(s):
    result = ""
    counts = Counter(s)
    for char, count in counts.items():
        result += str(count) + char
    return result

print(countChars("AAABBCDDD"))

# 2. Given a string of opening and closing parenthesis types, validate the string.
#   {[()]} -> valid; {[()]}} -> invalid

def isValidParenthesis(s):
    stack = []
    pairs = { ")": "(", "]": "[", "}": "{" }
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            continue
    return not stack

print(isValidParenthesis("{[()]}"))
print(isValidParenthesis("{[()]}}"))

# 3. Given a set of stairs, how many different combinations of steps can be taken if you can take one or two stair steps per step.
#   4 steps, 1 or 2 at a time:
#       (1 1 1 1), (1 1 2), (1 2 1), (2 1 1), (2, 2) -> 5
#       (0) 1 1 2 3 5 8 13 21 ... (Fibonnaci)
#   4 steps, 1 to 3 at a time:
#       (1 1 1 1), (1 1 2), (1 2 1), (2 1 1), (2 2), (1 3), (3 1) -> 7
#       (0) (0) 1 1 1 3 5 9 17 ... (Tribonacci)

def fibonacciSteps(steps):
    a, b = 0, 1
    for _ in range(steps):
        a, b = b, a+b
    return b

print(fibonacciSteps(4))
