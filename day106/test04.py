# 모듈 module == JAVA의 라이브러리,클래스 역할
# .py 파이썬 파일
# 누군가 기능을 바로 사용할수있게 미리 구현해둔 파일

# 표준 모듈 <-> 외부 모듈(패키지,package, 설치 필요)
# 파이썬에 기본적으로 존재하는 모듈
# 별도의 설치가 필요없음
import math
print(math.pi)
print(math.pow(2,10))

from random import randrange,choice
##from random import *
print(randrange(10)) # 0~9
print(randrange(1,10)) # 1~9
print(choice([10,11,13,15,23]))

# 별명(alias)
import random as r
r.randrange(10)
from random import randrange as rr
rr(1,10)










