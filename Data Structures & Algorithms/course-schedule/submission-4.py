from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for prerequisite, course in prerequisites: 
            courses[course].append(prerequisite) 

        visiting = set()
        safe = set()

        def dfs(course: int) -> bool:
            '''
            Returns whether a course can be completed or not
            '''
            if course in visiting:
                return False

            if course in safe:
                return True

            visiting.add(course)
            for prerequisite in courses[course]:
                if not dfs(prerequisite):
                    visiting.remove(course)
                    return False

            visiting.remove(course)
            safe.add(course)

            return True

             
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True