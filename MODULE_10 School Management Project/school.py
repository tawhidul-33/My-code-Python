class School:
    sm=10
    @classmethod
    def siyam(cls,name):
        print(name,cls.sm)

    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.teachers={} #{'bangla','rahim_sir'}
        self.classrooms={}#{'eight','classroom'}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher

    def student_admission(self,student):
        classname=student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(mark):
        if mark>=80 and  mark<=100:
            return 'A+'
        elif mark>=70 and  mark<80:
            return 'A'
        elif mark>=60 and  mark<70:
            return 'A-'
        elif mark>=50 and  mark<60:
            return 'B'
        elif mark>=40 and  mark<50:
            return 'C'
        elif mark>=33 and  mark<40:
            return 'D'
        else: 
            return 'F'
    @staticmethod
    def grade_to_valu(grade):
        grade_map={
            'A+':5.00,
            'A':4.00,
            'A-':3.50,
            'B':3.00,
            'C':2.00,
            'D':1.00,
            'F':0.00
        }
        return grade_map[grade]
    @staticmethod
    def overAll_valu_to_grade(valu): #for final grade
        if valu>=4.5 and valu<=5.0:
            return 'A+'
        elif valu>=3.5 and valu<4.5:
            return 'A'
        elif valu>=3.0 and valu<3.5:
            return 'A-'
        elif valu>=2.5 and valu<3.0:
            return 'B'
        elif valu>=2.0 and valu<2.5:
            return 'C'
        elif valu>=1.0 and valu<2.0:
            return 'D'
        else:
            return 'F'
    def __repr__(self):
        #all class room
        for key in self.classrooms.keys():
            print(key)
        #all students
        print('All Student')
        result=''
        for key,value in self.classrooms.items():#prottekta classroom a gelam
            result+=f'--{key.upper()} Classroom students\n'
            for student in value.students:
                result+=f'{student.name}\n'
        print(result)
        #all subject
        subject=''
        for key,value in self.classrooms.items():#prottekta classroom a gelam
            subject+=f'--{key.upper()} Classroom subjects\n'
            for sub in value.subjects:
                subject+=f'{sub.name}\n'
        print(subject)
        
        #all teachers
        print('ALL Teacher and Subject')
        for key,value in self.teachers.items():
         print(f'{value.name} subject: {key}')

        #all student results
        print("Student Result")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.subject_marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.final_grade())

        return ''
School.siyam('siyam')
