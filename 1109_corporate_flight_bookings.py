# 1109. Corporate Flight Bookings
# MEDIUM
# https://leetcode.com/problems/corporate-flight-bookings/description/

# There are n flights that are labeled from 1 to n.
# You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.
# Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

# Example 1:
# Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# Output: [10,55,45,25,25]
# Explanation:
# Flight labels:        1   2   3   4   5
# Booking 1 reserved:  10  10
# Booking 2 reserved:      20  20
# Booking 3 reserved:      25  25  25  25
# Total seats:         10  55  45  25  25
# Hence, answer = [10,55,45,25,25]

# Example 2:
# Input: bookings = [[1,2,10],[2,2,15]], n = 2
# Output: [10,25]
# Explanation:
# Flight labels:        1   2
# Booking 1 reserved:  10  10
# Booking 2 reserved:      15
# Total seats:         10  25
# Hence, answer = [10,25] 

# Constraints:
# 1 <= n <= 2 * 104
# 1 <= bookings.length <= 2 * 104
# bookings[i].length == 3
# 1 <= firsti <= lasti <= n
# 1 <= seatsi <= 104

from itertools import accumulate

tests = [
    {
        "bookings": [[1,2,10],[2,3,20],[2,5,25]],
        "n": 5,
        "answer": [10,55,45,25,25],
    },
    {
        "bookings": [[1,2,10],[2,2,15]],
        "n": 2,
        "answer": [10,25],
    },
]

class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        answer = [0] * (n + 1)

        # inefficient solution
        # bookings = self.simplify(bookings)
        # for first, last, seats in bookings:
        #     for i in range(first, last + 1):
        #         answer[i] += seats

        for first, last, seat in bookings:
            answer[first-1] += seat
            answer[last] -= seat
        answer = list(accumulate(answer[:-1]))

        return answer
    
    # inefficient solution helper
    # def simplify(self, bookings: list[list[int]]) -> list[list[int]]:
    #     simplified = []
    #     uniques = {}
    #     for booking in bookings:
    #         t, seats = (booking[0], booking[1]), booking[2]
    #         if t not in uniques:
    #             uniques[t] = seats
    #         else:
    #             uniques[t] += seats
    #     for k, v in uniques.items():
    #         simplified.append([k[0], k[1], v])
    #     return simplified

sol = Solution()

t0 = sol.corpFlightBookings(tests[0]["bookings"], tests[0]["n"])
t1 = sol.corpFlightBookings(tests[1]["bookings"], tests[1]["n"])

# print(t0)
# print(t1)

assert t0 == tests[0]["answer"]
assert t1 == tests[1]["answer"]
