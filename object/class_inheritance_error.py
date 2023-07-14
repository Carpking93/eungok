# 상속 클래스

class Family:
    lastname = '김'
    def lname(self):
        print(f'성은 {Family.lastname}')    #{Family.lastname}대신 {self.lastname} 해도 됩니다

class Person(Family):
    firstname = "태경"
    def fname(self):
        print(f'이름은 {self.firstname} 입니다.')

family = Family()
person = Person()

# family.lname()
person.fname()
person.lname()  #상속받아서 사용가능

#오류를 확인하자
print(family.firstname)