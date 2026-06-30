class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if len(prerequisites) == 1:
        #    return True

        #  Course | PreReq
        #  0        1
        #  1        0  
        
        courses = {i: [] for i in range(numCourses)} 
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        
        visited_crs = set()
        def _dfs(c):
            if c in visited_crs:
                return False

            if courses[c] == []:
                return True

            visited_crs.add(c)

            for prereq in courses[c]:
                if not _dfs(prereq):
                    return False
            
            visited_crs.remove(c)
            courses[c] = []
            return True
     
        for c in range(numCourses):
            if not _dfs(c):
                return False
        
        return True


        




        

        