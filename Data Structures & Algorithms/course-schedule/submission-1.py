from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Cycle detection question
        '''
        visiting = set()
        visited = set()

        # build graph
        courses = defaultdict(list) # course -> [prerequisites]
        for prerequisite in prerequisites: 
            course, p = prerequisite
            courses[course].append(p)

        def dfs(course: int) -> bool:
            # returns whether one can finish this course or ont

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
            if course not in visited:
                if not dfs(course):
                    return False

        return True