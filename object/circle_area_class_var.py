# 원의 넓이

class Circle:
    pi = 3.14
    def __init__(self,radius) :
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * Circle.pi
    
    @property
    def radius (self):
        return self.__radius
    
circle = Circle(5)
print(circle.radius)
area = circle.area()
print(Circle.pi)
print(f'반지름이 {circle.radius}인 원의 넓이는 {area} 입니다.')
