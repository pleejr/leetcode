# 274. H-Index
# MEDIUM
# https://leetcode.com/problems/h-index/

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1

# Constraints:
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        l = len(citations)
        h = citations[0]
        count = 0

        if l == 1:
            if h >= 1:
                return 1
            else:
                return 0

        for i in range(l):
            h = citations[i]
            if h >= l:
                print("increment")
                count += 1
            elif h > 0:
                # how many papers have at least h citations?
                has_citations = i + 1
                remaining_papers = citations[has_citations:]
                for paper in remaining_papers:
                    if paper == h:
                        has_citations += 1
                    else:
                        break
                # are there at least h citations?
                if has_citations >= h:
                    print("returning h")
                    print(f"count={count}")
                    return max(h, count)
                else:
                    count += 1
        print("returning count")
        return count