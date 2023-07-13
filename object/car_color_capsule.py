class Car:

  def __init__(self, name, price,color):
    self.__name = name
    self.__price = price

    if price <= 100000000:
      raise ValueError('차 값이 1억보다 커야 합니다.')
    self.__color = color

  def __str__(self):
    return(f'Car(name={self.__name}, 가격={self.__price},색상={self.__color})')

  @property
  def color(self):    #property 변수값이 abc이면 @abc.setter가 되야함
    return self.__color

  @color.setter
  def setcolor(self, color):
    if self.__color == "노랑":
      raise ValueError('노랑은 안돼요')
    self.__color = color

car = Car("아반뗴",1000000000,"파랑")
print(car)
print("=============================")
# cat.__age=10
car.setcolor = "블랙"
car.price = 10000000
print(car)
print(car.color)