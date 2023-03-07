import Student
class Library:
    def __init__(self,id,name):
        self.usedid=id
        self.uname=name
l=Library(1234,"Vishnu")
print("User-id : "+str(l.usedid))
print("Name : "+str(l.uname))

import Student as obj

s=obj.students(12345,"Vishnu")
t=obj.Teacher(1234,"Raja")
b=obj.Teacher(6789,"Chandru")
print(obj.Teacher.teachers_count)
def changeStudentName(obj):
    obj.rollnumber=5000             #Duck Typing
print(s.getrollnumber())
changeStudentName(s)
print(s.getrollnumber())