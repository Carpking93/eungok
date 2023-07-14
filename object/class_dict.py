class Circle:
    pi = 3.14
    def __init__(self,name ,radius) :
        self.__radius = radius
        self.__name = name

    def area(self):
        return self.__radius * self.__radius * Circle.pi
    
c1 = Circle("C1" , 4)

print(c1.__dict__)
# print(c1.__name)
print(c1.__dict__['_Circle__name'])
print(c1.__dict__['_Circle__radius'])
