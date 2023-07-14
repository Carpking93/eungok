class Family:
    def __init__(self) :
        self.lastname = "김"

    def lname(self):
        print(f'성은 {self.lastname}')

    def introduce(self):
        print("가족입니다.")

class Person(Family):
    def __init__(self):
        super().__init__()
        self.firstname = "태경"

    def fname(self):
        print(f'이름은 {self.firstname} 입니다.')

    def introduce(self):
        super().introduce()
        print(" 저는 가족의 일원입니다.")

family = Family()
person = Person()

family.introduce()
person.introduce()
