#이차방정식 math.sqrt를 사용하지 않을꺼면 **0.5 사용해도 상관없음
import math
def quadratic_equation_roots(a,b,c):
    if b**2 - 4*a*c < 0 :
        print(f'실근이 없습니다.')
    else:
        x = b**2 - 4*a*c
        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)

        if b**2 - 4*a*c == 0:
            print(f'방정식의 해는 중근 {x1} 입니다.')
        else :
            print(f'x1 = {x1} or x2 = {x2} ')

# a = int(input("이차항의 계수를 넣으세요"))
# b = int(input("일차항의 계수를 넣으세요"))
# c = int(input("상수항의 계수를 넣으세요"))

# quadratic_equation_roots(a,b,c)

#원의 넓이 (반지름 * 반지름 * 3.14(math.pi))
r = float(input("원의 반지름을 입력하세요"))
print(f'원의 넓이 : {r * r * math.pi}')
print(f'원의 넓이 : {r ** 2 * math.pi}')

#원의 둘레의 길이 ( 2 * 반지름 * 3.14(math.pi))
print(f'원의 둘레 길이 : {2 * r * math.pi}')

#원의 넓이 함수
def circleArea (radius):    #원의 면적 계산 함수
    area = math.pi*radius**2 
    circumResult = math.pi*radius* 2 # 파이 * 반지름 * 2   #파이 * 반지름제곱
    return area ,circumResult            #결과를 반환      

area , circumResult = circleArea (r)

print(f"반지름의 면적 : {area}")     #면적 출력
print(f"반지름의 둘레 :  {circumResult}")   #둘레 출력