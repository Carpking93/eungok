# 상속 클래스

class Family:
    def __init__(self) :
        self.lastname = "김"
    def lname(self):
        print(f'성은 {self.lastname}')    #{Family.lastname}대신 {self.lastname} 해도 됩니다
        
class Person(Family):    
    firstname = "태경"      #자식클래스에 init이 없어서 super()를 사용하지 않아도 상속받을수 있음

    def fname(self):
        print(f'이름은 {self.firstname} 입니다.')

family = Family()
person = Person()

family.lname()
person.fname()
# person.lname()  #상속받아서 사용가능
print(person.lastname)