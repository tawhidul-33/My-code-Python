# from persion import Student
from school import School
class Subject:
    def __init__(self,name,teacher): 
        self.name=name
        self.teacher=teacher # teacher er object thake
        self.max_marks=100
        self.pas_marks=33
    def exam(self,students):#students er list
        for student in students:
            mark=self.teacher.evaluate_exam()

            student.subject_marks[self.name]=mark
            student.subject_grade[self.name]=School.calculate_grade(mark)
