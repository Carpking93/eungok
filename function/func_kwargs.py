# 키워드 매개변수, kwargs
#키워드 매개변수를 사용할 때는 매개변수 앞에 별 2개(**)를 붙인다.
# **kwargs는 dict 타입 . key값이 for문이 돌아가기에 values 값을따로 뽑아서 출력 -> list로 변하기에 계산가능
def keyword_함수(**kwargs):
    print(type(kwargs))
    num = 0
    print(kwargs.values())
    for i in kwargs.values():
        num = num + i
    return num 
result = keyword_함수(a=1,b=2,c=3)
print(result)

def name_hello_함수(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # for i in kwargs:
    #     print(type(i))
    #     print(f'{kwargs[i]} 님 안녕하세요!')
    for i in kwargs.values():
        # print(type(i))
        print(f'{i} 님 안녕하세요!!')

     
name_hello_함수(a="김태경",b="김태뽕",c="김태발")
