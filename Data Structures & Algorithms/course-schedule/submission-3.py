from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for course, prerequisite in prerequisites: 
            courses[course].append(prerequisite)

        visiting = set()
        visited = set() 

        def dfs(course: int) -> bool:
            '''
            Returns whether this course can be completed or not
            '''
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

            return True



        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True