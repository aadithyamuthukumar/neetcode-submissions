from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        count_0 = counts[0]
        count_1 = counts[1]


        final_count = len(students)
        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                final_count -= 1
                counts[sandwich] -=1
            else:
                break
        
        return final_count


        