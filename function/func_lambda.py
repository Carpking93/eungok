# 람다 표현식에 조건부 표현식 사용하기

# 먼저 람다 표현식에서 조건부 표현식을 사용하는 방법을 알아보겠습니다.

# lambda 매개변수들: 식1 if 조건식 else 식2
# 다음은 map을 사용하여 리스트 a에서 3의 배수를 문자열로 변환합니다.

a = [ 1,2,3,4,5,6,7,8,9,10]
list_data = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(list_data)

list_data_1 = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(list_data_1)
#a 가 1 = str 변함 2는 1이 아니기에 else float 소수점변경 그다음3 if x==2 이미 2는 else에서 지나가고 3이기에 
# flase +10 을 추가해서 13 14 15 출력...


# map에 객체를 여러 개 넣기
# map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수도 있습니다. 다음은 두 리스트의 요소를 곱해서 새 리스트를 만듭니다.
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list_data_2 = list(map(lambda x, y: x * y, a, b))
print(list_data_2)


#  filter 사용하기
# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, # filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져옵니다.
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list_data_3 = list(filter(lambda x: x > 5 and x < 10))
print(list_data_3)

# # reduce 사용하기
#reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수입니다
# (reduce는 파이썬 3부터 내장 함수가 아닙니다. 따라서 functools 모듈에서 reduce 함수를 가져와야 합니다)

a = [1,2,3,4,5]
from functools import reduce
list_data_4 = reduce(lambda x,y : x+y,a)
print(list_data_4)