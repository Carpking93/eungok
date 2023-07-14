# 상속 클래스

class Family:
    def __init__(self) :
        self.lastname = "김"
    def lname(self):
        print(f'성은 {self.lastname}')    #{Family.lastname}대신 {self.lastname} 해도 됩니다
        
class Person(Family):
    def __init__(self) :
        self.firstname = "태경"    
    def fname(self):
        print(f'이름은 {self.firstname} 입니다.')

family = Family()
person = Person()

family.lname()
person.fname()
# person.lname()  #상속받아서 사용가능

#오류를 확인하자 , person 에는 lastname이 없다. init을 해서 발생한 오류
# AttributeError: 'Person' object has no attribute 'lastname'. Did you mean: 'firstname'?
print(person.lastname)