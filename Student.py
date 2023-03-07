from abc import ABC,abstractmethod          #packages needed for Abstract class
class School(ABC):                          #Abstract class
    @abstractmethod
    def getrollnumber(self):
        pass
    @abstractmethod
    def getname(self):
        pass
class students(School):
    students_count=0
    def __init__(self,rollnumber,name):
        self.rollnumber=rollnumber
        self.name=name
        students.students_count+=1
    def getname(self):
        return self.name
    def getrollnumber(self):
        return self.rollnumber
class Teacher(School):
    teachers_count=0
    def __init__(self,rollnumber,name):
        self.rollnumber=rollnumber
        self.name=name
        Teacher.teachers_count+=1
    def getname(self):
        return self.name
    def getrollnumber(self):
        return self.rollnumber