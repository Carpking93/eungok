from abc import *

class StudentBase(metaclass=ABCMeta):
    
    @abstractmethod
    def study(self):        
        pass

    @abstractmethod
    def go_to_school(self):
        print("학교에 가다")
        pass

class Student(StudentBase):
    def study(self):        
        print("공부하기")
    
    def go_to_school(self):
        super().go_to_school()
        print("출석")

james = Student()
james.go_to_school()
james.study()