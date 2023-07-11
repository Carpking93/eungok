# [ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ]
list = [ 1,2,3,4,5,6,7,8,9,10]
list = [ num * 3 for num in list]
print(list)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30] 출력 결과값.

# 리스트 안에서 for 문 사용하기 2: if 문 사용 
list = [ num * 3 for num in list if num % 2 == 1 ]
print(list)
# [9, 27, 45, 63, 81] - 위에 3곱해진 list값에서 홀수만 *3을한 출력값