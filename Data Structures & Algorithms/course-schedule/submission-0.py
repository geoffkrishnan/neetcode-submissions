"""
input:
    int - num courses
    int array - prerequisites
        prerequisites[i] = [a,b]
        all pairs distinct

output:
    True if possible to finish all courses else return False

must take b first if you want to take a


num courses is 0 indexed number of courses you are required to take 

can represent as directed graph
where we order the courses by prereqs b -> a 

so given [0, 1]

1 -> 0

course to prereqs

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            course_prereqs[course].append(prereq)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            if course_prereqs[node] == []:
                return True
            
            visited.add(node)

            for prereq in course_prereqs[node]:
                if not dfs(prereq):
                    return False
            
            visited.remove(node)
            course_prereqs[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

            


        