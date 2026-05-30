from typing import List
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        stud_preferred_type = Counter(students) # Counter({1: 2, 0: 2})
        students_count = len(students)
        for s in sandwiches:
            if stud_preferred_type[s] > 0:
                stud_preferred_type[s] -= 1
                students_count -= 1
            else:
                break        
        return students_count