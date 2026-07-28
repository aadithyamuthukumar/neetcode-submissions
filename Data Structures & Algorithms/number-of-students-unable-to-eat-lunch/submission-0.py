class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotations = 0
        
        while rotations < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0
            else:
                temp = students.pop(0)
                students.append(temp)
                rotations+=1
        if sandwiches:
            return rotations
        return 0
        