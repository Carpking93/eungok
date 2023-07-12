def odd_sum():
    num = 0
    for i in range(11):
        if i % 2 == 0:
            continue
        num = num + i
    
    return num
    print(f'0부터 10까지 짝수의 합 합 합 합 합 : {num} ') # 뒤에 있는 코드를 더이상 실행하지 않는 종료의 역할도함.

result = odd_sum()
# print(f'1부터 10까지 홀수의 합 : {result} ') #return 의 첫번째 기능 반환하는역할.