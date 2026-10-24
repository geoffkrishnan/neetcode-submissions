"""
input:
    int array - prereqs
output:
    return list of ANY valid order of courses you can take if you can finish all courses else empty list

prereqs[i] - [a, b]
where must take b first if you want to take a

courses numbered 0 - (n - 1)


"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_prereq = defaultdict(list)
        for course, prereq in prerequisites:
            course_to_prereq[course].append(prereq)
        
        order = []

        visited, cycle = set(),set()
        def dfs(course: int) -> bool:
            if course in cycle:
                return False

            if course in visited:
                return True
            
            cycle.add(course)
            
            for prereq in course_to_prereq[course]:
                if dfs(prereq) == False:
                    return False
            
            cycle.remove(course)

            visited.add(course)
            order.append(course)

            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return order
            
            
            



            
        