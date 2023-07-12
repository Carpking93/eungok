#  캡슐화. 캡슐화를 하면 외부에서 속성값을 변경할 수 없다.
class Cat:
    def __init__(self , name , age ):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Cat(name={self.__name},age={self.__age})' 
    

nabi = Cat("나비",10)
nero = Cat("네로",20)

print(nabi)
# print(nero)
print("==================================================")
nabi.__age = 100
print(nabi)