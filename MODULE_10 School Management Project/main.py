from classroom import ClassRoom
from persion import Teacher,Student
from school import School
from subject import Subject

scholl= School('ABC','Dhaka')

#adding classroom
eight=ClassRoom('Eight')
nine=ClassRoom('Nine')
ten=ClassRoom('Ten')

scholl.add_classroom(eight)
scholl.add_classroom(nine)
scholl.add_classroom(ten)

#addng student
rahim=Student('Rahim',eight)
karim=Student('Karim',nine)
fahim=Student('Fahim',ten)
hamim=Student('Hamim',ten)

scholl.student_admission(rahim)
scholl.student_admission(karim)
scholl.student_admission(fahim)
scholl.student_admission(hamim)

#adding Teacher
abul=Teacher('Abul Khan')
babul=Teacher('Babul Khan')
kabul=Teacher('Kabul Khan')

# Registering Teachers to School
scholl.add_teacher('Bangla',abul)
scholl.add_teacher('Physics',babul) 
scholl.add_teacher('Chemistry',kabul)
scholl.add_teacher('Biology',kabul)

#adding subject
bangla=Subject('Bangla',abul)
physics=Subject('Physics',babul)
chemistry=Subject('Chemistry',kabul)
biology=Subject('Biology',kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)

nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(biology)

ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(scholl)

