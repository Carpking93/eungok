s1 = set([1, 1,1,1,1,1,1,1,1,1,1,1, 2, 3])
print(s1)
s2 = set("Hello World")
print(s2)
# set은 중복을 허용하지 않음. 순서도 없음

s3 = list("Hello World")
print(s3)
s4 = tuple("Hello World")
print(s4)
# 공백도 문자열로 받아서 출력

s5 = set(tuple(list(set("Hello World"))))
print(s5)

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 ( & , intersection) 2가지 방법이 있다.
s3 = (s1 & s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

#합집합 (| , union ) 2가지 방법이 있다.

s3 = s1 | s2
print(s3)

s4 = s1.union(s2)
print(s4)

#차집합 ( - , difference ) 2가지 방법이 있다.
s3 = (s1-s2)
print(s3)
s4 = s2.difference(s1)
print(s4)

# 값 1개 추가하기 - add
# 이미 만들어진 set 자료형에 값을 추가할 수 있다. 1개의 값만 추가add할 때는 다음과 같이 하면 된다.

s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러 개 추가하기 - update
# 여러 개의 값을 한꺼번에 추가(update)할 때는 다음과 같이 하면 된다.

s1 = set([1, 2, 3])
s1.update([1, 2, 4, 5, 6])
print(s1)

# 특정 값 제거하기 - remove
# 특정 값을 제거하고 싶을 때는 다음과 같이 하면 된다.
# remove뒤에는 elem값 인덱스값이 아님.

s1 = set([1, 2, 3, 5])
s1.remove(3)
print(s1)

# list , dictionry , tuple , set 