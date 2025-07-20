class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__student_id} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} has been enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__student_id} is not currently enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been dropped successfully.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Status: {status}")

    def get_student_id(self):
        return self.__student_id

    # def is_enrolled(self):
    #     return self.__is_enrolled

# কিছু Student তৈরি করি (ম্যানুয়ালি)
s1 = Student(1, "Rahim", "CSE")
s2 = Student(2, "Karim", "EEE")
s3 = Student(3, "Sakib", "BBA")

# মেনু সিস্টেম
def menu():
    while True:
        print("\n=== Student Database Menu ===")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            for student in StudentDatabase.student_list:
                student.view_student_info()

        elif choice == '2':
            try:
                sid = int(input("Enter Student ID to Enroll: "))
                found = False
                for student in StudentDatabase.student_list:
                    if student.get_student_id() == sid:
                        student.enroll_student()
                        found = True
                        break
                if not found:
                    print("Student ID not found.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            try:
                sid = int(input("Enter Student ID to Drop: "))
                found = False
                for student in StudentDatabase.student_list:
                    if student.get_student_id() == sid:
                        student.drop_student()
                        found = True
                        break
                if not found:
                    print("Student ID not found.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            print("Exiting Program...")
            break

        else:
            print("Invalid choice. Please enter between 1 and 4.")

# মেনু কল করি
menu()
