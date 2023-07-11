# a = "Hello"

# for i in range(0,len(a)):
#     print( f"{a[i]}_", end="")

# upper , lower 는 새로운 값에 담아줘야함.
# 1. 문자열 대문자로 변경하는 함수 (string.upper)
s1 = "rich"
s1 = s1.upper()
print('s1 :' +s1)
# 2. 문자열 소문자로 변경하는 함수 (string.lower)
s1 = "RICH"
s1 = s1.lower()
print('s1 :' +s1)
# 3. 문자가 대문자인지 확인하는 함수 (string.isupper)
s1 = "RICh"
s1 = s1.isupper()
print(s1)
# 4. 문자가 소문자인지 확인하는 함수 (string.islower)
s1 = "RIch"
s1 = s1.islower()
print(s1)
# 5. 단어의 첫문자를 대문자로 바꿔주는 함수(string.title)
s1 = "rich"
s1 = s1.title()
print(s1)
# 대문자는 소문자로 소문자는 대문자로 바꿔주는 함수(string.swapcase)
s1 = "RicH"
s1 = s1.swapcase()
print(s1)

# count() : 문자열의 개수 출력
# find() : 문자열 앞부터 시작하여 처음으로 나온 위치를 출력
# index() : find와 같이 위치를 출력하지만 찾는 단어가 없을 시 에러
# 발생
# a = “Hello world”
# a.count(“o”)
# a.find(“r”)
# a.index(“r”)
# a.index(“a”) #a 라는 문자열이 없어서 에러 발생

# lstrip() : 문자열 왼쪽의 공백을 지운다.
# rstrip() : 문자열 오른쪽의 공백을 지운다. 
# strip() : 문자열 양쪽의 공백을 지운다.

# replace() : 문자열 안의 특정한 값을 다른 값으로 치환한다. 
# split() : 문자열을 괄호 안에 값으로 구분하여 나누어준다.(괄호 안에 값을 넣지 않으면 공백을 기준으로 한다.)

a = "H e l l o W o r l d"
a1 = a.replace("Hello" , "Bye")
print(a1)

a2 = a1.split("  ") #"  "안에 공백이 2칸이면 2칸 공백의 문자열이 없기때문에 변화 없음. 
a2 = a1.split(sep=" " , maxsplit=2) # sep 구분할 기준 , maxsplit 최대로 구분할 수 / 공백을 기준으로 max가 2 H,E, l l o w o l r d 출력 
a2 = a1.split(sep=" ", maxsplit= -1 ) # maxsplit -1 은 제한없이 전체 
print(a2)

#splitlines() 한줄씩 분리 하는 방법.
str =  '''
안녕하세요.
반갑습니다.
어서오세요~
'''
result = str.splitlines()
print(result)