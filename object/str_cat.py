class Cat:
    def __init__(self , name , color ):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Cat(name={self.name},color={self.color})' 
    
    def lotto(self):
        print(f'내이름은{self.name},색은 {self.color} 당첨 당첨!')


nabi = Cat("나비","흰색")
nabi.lotto()
nero = Cat("네로","검은색")

print(nabi)
print(nero)