# 상속 클래스

class Family:
    def __init__(self) :
        self.lastname = "김"
    def lname(self):
        print(f'성은 {self.lastname}')    #{Family.lastname}대신 {self.lastname} 해도 됩니다
        
class Person(Family):
    def __init__(self) :
        super().__init__()  #init을 가져오기 위해 super().__init__() 을 사용 상속받는 클래스가 적어야함 #super()클래스는 전에 있던 값에서 가져올때 사용
        self.firstname = "태경"    
    def fname(self):
        print(f'이름은 {self.firstname} 입니다.')

family = Family()
person = Person()

family.lname()
person.fname()
# person.lname()  #상속받아서 사용가능
print(person.lastname)