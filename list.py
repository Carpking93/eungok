# list

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ('Life', 'is')]

# 리스트는 원소를 모으는것.

ab = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(ab[3][1])

# 리스트 더하기 , 곱하기
#  tuple 이랑 같음 리스트를 하나 더생성
#  곱하기 역시 정수값으로 반복할뿐 리스트끼리 곱하지 않음

# list 값 수정하기
# a = [1, 2, 3]
# a[2] = 4
# a
# [1, 2, 4]


# list 값 del 함수를 사용하여 삭제하기
# del 같이 앞에 나오는 애들은 키워드라고 한다.

# a = [1, 2, 3]
# del a[1]
# a
# [1, 3]


# list 요소 제거 - remove  //remove(elem) = 인덱스가 아닌 원소!
# remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.

# a = [1, 2, 3, 1, 2, 3]
# a.remove(3)
# list 는 객체라서 remove라는 메소드를 사용할수 있음. 메소드를 사용하기위해 . 사용 
# print(a)
# [1, 2, 1, 2, 3]


# 리스트 요소 끄집어 내기 - pop
# pop()은 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제한다.

# abc = [1, 2, "ㅁ"]
# abc.pop()
# 3
# a
# [1, 2]

abc = [1, 2, "ㅁ"]
print(abc.pop())
print(abc)

# a = [1, 2, 3]
# a.pop(1)
# 2
# a
# [1, 3]
# a.pop(1)은 a[1]의 값을 끄집어 내어 리턴한다. 다시 a를 출력해 보면 끄집어 낸 값이 삭제된 것을 확인할 수 있다.


#list에 요소 추가하기 - append
# append(x)는 리스트의 맨 마지막에 x를 추가하는 함수이다.

# a = [1, 2, 3]
# a.append(4)
# print(a)
# [1, 2, 3, 4]


# list에 요소 삽입 - insert
# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수이다.

# a = [1, 2, 3]
# a.insert(0, 4)
# print(a)
# [4, 1, 2, 3]


# list에 요소 삽입 - extend()
# append와 다른점은 ()안에 iterable 만 올 수 있음.

nums = [1,2,3]
nums.extend([4,5,"ㅁ",6,7])
print(nums)


# sort(*, key=None, reverse=False)
# sorted([1,4,5,2,3]) -> sorted 는 리스트 자체를 다 넣어서 사용하는 경우
# @.sort -> list를 정령하는 것. str+int 는 크기값을 비교하지 못해서 사용불가 / int or str 한가지 원소만 있을때 sort실행

aa = [5,2,3,4,1]
bb = ["a","c","b"]
cc = sorted(["b","c","a"])
aa.sort()
bb.sort()
print(aa)
print(bb)
print(cc)

aa.sort(reverse=True)
print(aa)
dd = sorted(bb , reverse=True)
print(dd)


# key
# 정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
# key 값을 기준으로 정렬되고 기본값은 오름차순이다.
# key 값이 len = 길이 였기때문에 3글자인 굿모닝부터 가장 많은 글자인 good_morning 순으로 출력

str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))


# 리스트 뒤집기 - reverse
# reverse 함수는 리스트를 역순으로 뒤집어 준다. (정렬 없이 그저 역순)

ee = ["e","a","c","f","d","b"]
ee.reverse()
print(ee)

ff=[1,2,3,"a","c","b"]
ff.reverse()
print(ff)


# 인덱스 반환 - index
# index(x) 함수는 리스트에 x 값이 있으면 x의 인덱스 값(위칫값)을 리턴한다.
# >>> a = [1, 2, 3]
# >>> a.index(3)
# 2
# >>> a.index(1)
# 0
# a.index(3) 숫자 3이란 값의 인덱스를 알려주는것.


#count 함수
# 변수. count(찾는 요소) -> 함수를 사용한 변수 안에서 해당 값의 개수를 숫자로 반환한다. 

ab = [ 1,1,1,2,3,3,1]
print(ab.count(1))


#clear 함수
ab.clear()
print(ab)

ab.append(5)
print(ab)

ab.extend([2,1])
print(ab)

ab.append([3,4])
print(ab)
