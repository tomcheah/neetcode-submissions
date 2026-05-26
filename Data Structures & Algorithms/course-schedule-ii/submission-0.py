from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visiting = set()
        visited = set()
        
        # build graph
        courses = defaultdict(list) # course -> [prerequisites]
        for prerequisite in prerequisites:
            course, pre = prerequisite
            courses[course].append(pre)

        def dfs(course: int) -> bool:
            # returns whether a course can be taken or not
            if course in visited:
                return True

            if course in visiting:
                return False

            # visit the course's prerequisites
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