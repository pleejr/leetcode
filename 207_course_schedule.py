# 207. Course Schedule
# MEDIUM
# https://leetcode.com/problems/course-schedule/description/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false. 

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

tests = [
    {
        "numCourses": 2,
        "prerequisites": [[1,0]],
        "answer": True,
    },
    {
        "numCourses": 2,
        "prerequisites": [[1,0],[0,1]],
        "answer": False,
    },
    {
        "numCourses": 3,
        "prerequisites": [[2,1],[1,0]],
        "answer": True,
    },
    {
        "numCourses": 4,
        "prerequisites": [[1,3],[2,0],[1,0],[3,1],[3,2]],
        "answer": False,
    },
]

def main():
    sol = Solution()
    results = []
    for test in tests:
        results.append(sol.canFinish(test["numCourses"], test["prerequisites"]))
    for i in range(len(results)):
        if results[i] == tests[i]["answer"]:
            print(f"Correct: {results[i]}")
        else:
            print(f"Incorrect: {results[i]}")
    return

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        walkable = True
        courses = self.getCourses(prerequisites)
        walked = set()
        for prereqs in courses.values():
            walkable &= self.walkCourses(courses, prereqs, numCourses, walked)
        return walkable

    def getCourses(self, prerequisites: list[list[int]]) -> dict:
        courses = {}
        for target, prereq in prerequisites:
            if target not in courses:
                courses[target] = {prereq}
            else:
                courses[target].add(prereq)
            if prereq not in courses:
                courses[prereq] = set()
        return courses
    
    def walkCourses(self, courses: dict, prereqs: dict, numCourses: int, walked: set) -> bool:
        walkable = True
        for prereq in prereqs:
            hops = numCourses
            if hops < 0:
                return False
            else:
                hops -= 1
                if not prereq in walked:
                    walkable &= self.walkCourses(courses, courses[prereq], hops, walked)
                    walked.add(prereq)
        return walkable

if __name__ == "__main__":
    main()