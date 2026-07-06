from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        visiting = set()
        visited = set()

        courses = defaultdict(list)
        for course, prerequisite in prerequisites: 
            courses[course].append(prerequisite)

        def dfs(course: int) -> bool:
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)
            for prerequisite in courses[course]:
                if not dfs(prerequisite):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res


            