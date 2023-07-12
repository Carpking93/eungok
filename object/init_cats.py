class Cat:
    def __init__(self , name , color="흰색"):
        self.name = name
        self.color = color

    def meow(self,sound):
        print(f'내 이름은 {self.name} , 색은 {self.color} 이야 {sound} ')

nabi = Cat("나비")
nabi.meow("야옹~야옹~")

nero = Cat("네로" ,"검은색")
print(nero.name)    #속성값
print(nero.color)   #속성값

nero.name = "뇌로!" # 외부에서 바꾸는것은 매우 안좋은것
nero.color = "보라색"
nero.meow("검은 고양이 네로~네로~")