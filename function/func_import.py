import func_kwargs
from func_args import 함수
from func_kwargs import *

# from은 원하는 꾸러미에서 몇개의 함수만 가지고 오고 싶을때 사용
# as는 가져온 함수의 이름을 변경해서 사용할때 사용
from func_kwargs import name_hello_함수 as nh

# python에서 공식문서를 가져다 사용하는 방법 pip(pip install numpy 인스톨하는 방법)
import numpy as np

# import func_kwargs
# func_kwargs.name_hello_함수(a="kim",b="park",c="lee") 7,8번째줄은 세트.

data = 함수(1,2,3,4,5,6,7,100)
print(data)
# name_hello_함수(a="kim",b="park",c="lee")
nh(a="kim",b="park",c="lee")

# 상위 경로 import

import sys, os
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import hello

file_path = "c:\apps\test"
sys.path.append(file_path)


list_1 = [ 1,2,3,4,5]
list_2 = [2,5,1,2,10]
a = np.array(list_1)
b = np.array(list_2)
print(a+b)