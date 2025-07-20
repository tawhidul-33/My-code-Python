class student:
    def __init__(self,name,cur_class,id):
        self.name=name
        self.cur_class=cur_class
        self.id=id
    def __repr__(self):
        return f'name:{self.name} class:{self.cur_class} id:{self.id}'
    
class techer:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id
    def __repr__(self) ->str: 
        return f'name:{self.name} subject:{self.subject} id:{self.id}'
    
class school:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
        self.students=[]

    def add_teacher(self,name,subject):
        id=len(self.teachers)+1
        tchr=techer(name,subject,id)
        self.teachers.append(tchr)
        print(f'teacher name:{name} id:{id} He/She joiend at {subject}')

    def add_student_enroll(self,name,fee):
        if fee<6500:
            print('not enrollrd not enough fee for enroll')
        else:
            id=len(self.students)+1
            stnt=student(name,'C++',id)
            self.students.append(stnt)
            print(f'name:{name} id:{id} is enrolled extra mony {fee-6500}')


# sakib=student('sakib',9,648433)
# pias=techer('Pias','Algorithm',101)
# print(sakib)
# print(pias)

phitron=school('phitron')
phitron.add_student_enroll('siyam',6500)
phitron.add_student_enroll('sakib',8500)
phitron.add_student_enroll('rohul',6000)
        
phitron.add_teacher('pias mahmud','algo')
phitron.add_teacher('Hasan mahmud','DS')
phitron.add_teacher('Ratin','mentor')


        