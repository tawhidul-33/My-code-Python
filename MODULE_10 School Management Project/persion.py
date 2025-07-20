import random
from school import School
class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def evaluate_exam(self):
        return random.randint(50,100) #random mark 50 theke 100 er moddeh dibe
        
class Student(Person):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom=classroom #classroom object
        self.__id=None
        self.subject_marks={} #{'Eng':75,'ict':80}
        self.subject_grade={}  #{'eng':'A','bng':'C'}
        self.overAll_grade=None  #Final grade
    def final_grade(self):
        sum=0
        

        for grade in self.subject_grade.values():
            point= School.grade_to_valu(grade)
            sum+=point
        if sum==0:
            gpa=0.00
            self.overAll_grade='F'
        else:
             gpa=sum/len(self.subject_grade) # subject_grade a koyti subject ace ta len diye ber kora
             self.overAll_grade=School.overAll_valu_to_grade(gpa)
        return (f'{self.name} Final Grade: {self.overAll_grade}  with GPA: {gpa}')
    @property    #for getter
    def id(self):
        return self.__id
    @id.setter
    def id(self,valu):
        self.__id=valu
