#repr과 str의 차이
# repr 은 eval 처리를 해준것. = eval 은 문자열을 파이썬 언어로 바꿔서 계산해준다.
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # `repr()`과 함께 사용
    def __repr__(self):
        return f'Datetime.datetime.year'    #({self.year},{self.month},{self.day})'

    # Used with `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

   
    
obj=Date(2043,7,14)
print(obj)
# print(eval(obj))