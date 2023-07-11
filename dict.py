# dictionary(딕셔너리)
# 딕셔너리 타입은 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합
# 일반적인 딕셔너리 타입. 중괄호로 되어 있고 키와 값이 있습니다.
# 키로는 immutable한 값은 사용할 수 있지만, mutable한 객체는 사용할 수 없습니다.

# a = {"a" : 1, "b":2}
# print(a)

# immutable 예
# a1 = {1: 5, 2: 3}   # int 사용
# print(a1)
# {1: 5, 2: 3}

# a2 = {(1,5): 5, (3,3): 3} # tuple사용
# print(a2)
# {(1, 5): 5, (3, 3): 3}

# a3 = { 3.6: 5, "abc": 3} # float 사용
# print(a3)
# {3.6: 5, 'abc': 3}

# a4 = { True: 5, "abc": 3} # bool 사용
# print(a4)
# {True: 5, 'abc': 3}

# 값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워집니다.
# {"a" : 1, "a":2}
# print({"a" : 1, "a":2})

# 순서가 없기 때문에 인덱스로는 접근할수 없고, 키로 접근 할 수 있습니다.
d = {'abc' : 1, 'def' : 2}
d['abc'] = 5
# d['abc'] += 5
print(d)

# 새로운 키와 값을 아래와 같이 추가할 수 있습니다.
# d = {'abc' : 1, 'def' : 2}
# d['ghi'] = 999
# print(d)
# {'abc': 5, 'def': 2, 'ghi': 999}

# keys(), values(), items()
# print(d.keys())
# print(d.values())
# print(d.items())

# dict 만들기

# Result = dict([('a',1),('b',2),('c',3)])
# print(Result)

# dict constructor를 통해서 바로 키와 값을 할당하며 선언할 수 있습니다.
# newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
# print(newdict)
# {'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}


# dictionary(딕셔너리) 변환
# 리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 키와 value를 나란히 입력하면, dict로 변형할 수 있습니다.
# name_and_ages = [['alice', 5], ['Bob', 13]]
# print(dict(name_and_ages))
# {'alice': 5, 'Bob': 13}
# name_and_ages = [('alice', 5), ('Bob', 13)]
# print(dict(name_and_ages))
# {'alice': 5, 'Bob': 13}
# name_and_ages = (('alice', 5), ('Bob', 13))
# print(dict(name_and_ages))
# {'alice': 5, 'Bob': 13}
# name_and_ages = (['alice', 5], ['Bob', 13])
# print(dict(name_and_ages))
# {'alice': 5, 'Bob': 13}


# 여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.
# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# a.update({'bob':99, 'tony':99, 'kim': 30})
# print(a)
# {'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}


# ictionary(딕셔너리) 복사
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# b =a.copy()
# print(a)
# b['alice'].append(5)
# print(b)
# print(a)

# dictionary(딕셔너리) for문
# for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
# 순서는 임의적이다.같은 순서를 보장할 수 없다.
# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# for key in a:
#     print(key)


# value값으로 for문을 반복하기 위해서는 values() 를 사용
# for val in a.values():
#     print(val)


# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용
# for key, val in a.items():
    # print("key = {key}, value={value}".format(key=key,value=val))
    # print(a)

key_list=[]
value_list=[]

for key,value in a.items():
    key_list.append(key)
    value_list.append(value)

print(key_list)
print(value_list)