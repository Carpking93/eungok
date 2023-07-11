# tuple.
# 튜플은 요솟값을 변경할 수 없기 때문에 remove,pop,insert 등 내장함수가 없다.


t1 = ()
t2 = (1,) 
# t2 = (1) -> 이건 튜플이 아님.
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# print(type(t4))
t5[0]
#  인덱싱이라고 한다.
print(t5[0])
print(t5[2][1])

#indexing

t1 = (1,2,'a','b')
print(t1[0])

t1[1:3]
print(t1[1:3])
#  [1:3] -> 앞에 자리수는 <= 이고 뒤에 자리수는 >3 이렇게 표현 미만을 나타내는것.


# Slicing
a=(1,2,'a','b','c')
print(a[1:])

print(a[-2:])

print(a[:-1])

# 원소의 갯수
print(len(a))

#hello world

for x in range(len(a)):
    print("Hello !!!")
    print(a[x])

# tuple 더하기
a = (1,2,'a','b')
b = (3,4)
c = a+b
print(c)

# tuple 곱하기
a = (1,2,'a','b')
b = (3,4)
c = a*2
print(c)
# 곱하기는 튜플을 반복해서 곱한다. 튜플끼리 곱셈은 불가.

print(tuple([1,2,3]))
#  [] 리스트를 튜플안에 넣어서 변경해줬음.

print(type(range(10)))