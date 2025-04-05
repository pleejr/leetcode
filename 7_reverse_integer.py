# 7. Reverse Integer
# MEDIUM
# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned). 

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21 

# Constraints:
# -231 <= x <= 231 - 1

import copy

class Solution:
    def __init__(self) -> None:
        # track overflow as two's compliment bit limit
        self.limit = 31

    def reverse(self, x: int) -> int:
        # denote negative or positive
        sign = -1 if x != abs(x) else 1
        # restrict to positive values
        x = abs(x)
        # separate the digits of x into a list
        # order: little endian
        digits = self.separateBaseTen(x)
        # reverse the digits for the exercise
        # order: little endian
        digits.reverse()
        # convert each digit to binary
        binary_digits = []
        for digit in digits:
            binary_digits.append(self.baseTenToTwo(digit))
        # calculate full value for each binary digit
        valuesBaseTwo = []
        coefficient = [1]
        tenBaseTwo = self.baseTenToTwo(10)
        for i in range(len(binary_digits)):
            val = self.multiplyBaseTwo(binary_digits[i], coefficient)
            valuesBaseTwo.append(val)
            coefficient = self.multiplyBaseTwo(coefficient, tenBaseTwo)
        # add up calculated values
        resultBaseTwo = []
        for val in valuesBaseTwo:
            resultBaseTwo = self.addBaseTwo(resultBaseTwo, val)
        # return final sum or zero if overflow detected
        if len(resultBaseTwo) > self.limit:
            return 0
        else:
            return self.baseTwoToTen(resultBaseTwo) * sign

    # separate the digits of a base-10 int
    # order: little endian
    def separateBaseTen(self, num: int) -> list[int]:
        result = []
        while num:
            result.append(num % 10)
            num //= 10
        return result

    # convert base-10 to base-2
    # order: little endian
    def baseTenToTwo(self, num: int) -> list[list[int]]:
        baseTwo = []
        while num:
            baseTwo.append(num % 2)
            num //= 2
        return baseTwo

    # multiply two base-2 values
    # order: little endian
    def multiplyBaseTwo(self, a: list, b: list) -> list[int]:
        result = []
        for i in range(len(a)):
            addend = [0] * i + copy.deepcopy(b)
            if a[i]:
                result = self.addBaseTwo(result, addend)
        return result
    
    # add two base-2 values
    # order: little endian
    def addBaseTwo(self, a: list, b: list) -> list[int]:
        result = []
        if len(b) > len(a):
            a, b = b, a
        c = 0
        for i in range(len(a)):
            s = self.get(a, i) + self.get(b, i) + c
            w = s % 2
            c = s // 2
            result.append(w)
        if c:
            result.append(1)
        return result

    # helper to adjust lists of unmatched length
    # returns 0 if index error is caught
    def get(self, a: list, i: int) -> int:
        try:
            return a[i]
        except IndexError:
            return 0
    
    # convert base-2 to base-10
    # order: big endian
    def baseTwoToTen(self, resultBaseTwo: list[int]) -> int:
        result = 0
        for i in range(len(resultBaseTwo)):
            result += 2 ** i * resultBaseTwo[i]
        return result