class Cat:

  def __init__(self, name, age):
    self.__name = name
    if age <= 3:
      raise ValueError('3살 이상의 고양이만 입장 가능합니다')
    self.__age = age

  def __str__(self):
    return(f'Cat(name={self.__name}, age={self.__age})')

  @property
  def age(self):    #property 변수값이 abc이면 @abc.setter가 되야함
    return self.__age

  @age.setter
  def age(self, age):
    if age <= 10:
      raise ValueError('3살보다 많아야 나이를 바꿀수 있습니다.')
    self.__age = age

cat = Cat("나비",4)
print(cat)
print("=============================")
# cat.__age=10
cat.age = 14
print(cat)
print(cat.age)