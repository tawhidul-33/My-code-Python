class StudentDatabase:
    student_list=[]
    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)
class Student:
    def __init__(self,student_id,name,department,is_enrolled=False):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=is_enrolled
        StudentDatabase.add_student(self) #self mane student er protita attribute er obj pathaylam
    def enroll_student(self):
        if self.__is_enrolled:
            print('student already enrolled')
        else:
            self.__is_enrolled=True
            print('student enrolled successfully')
    def drop_student(self):
        if self.__is_enrolled==False:
            print('student already dropped')
        else:
            self.__is_enrolled=False
            print('student dropped successfully')
    def view_student_info(self):
        print(f'student_id:{self.__student_id} name:{self.__name} department:{self.__department}  enrollment status:{self.__is_enrolled}')
    
    #for private __student_id 
    def get_id(self):
        return self.__student_id 

std1=Student(1,'Siyam','CST')
std2=Student(2,'Sakib','EEE')
std3=Student(3,'Tipu','CV')


def menu():
    while True:
        
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        #StudentDatabase ai class er object creat
        stdbs=StudentDatabase()
        choice = int(input("Enter your choice into 1/2/3/4:"))


        if choice==1:
            for student_item in stdbs.student_list:
                student_item.view_student_info()


        elif choice==2:
            sid=int(input('Enter your id to enrolled'))
            flag=0
            for student_item in stdbs.student_list:
                if sid==student_item.get_id():
                    student_item.enroll_student()
                    flag=1
            if flag==0:
                print('Student id not found')


        elif choice==3:
            sid=int(input('Enter your id to dropped'))
            flag=0
            for student_item in stdbs.student_list:
                if sid==student_item.get_id():
                    student_item.drop_student()
                    flag=1
            if flag==0:
                    print('Student id not found')
        elif choice==4:
            print("Exiting Program")
            break
        else:
            print("Invalid choice. Please enter into 1 and 4.")
menu()
            

        

        
