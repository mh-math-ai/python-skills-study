
# random module provides functions for generating random numbers
from random import *

print(random()) # 0.0 <= x < 1.0 
print(random()*10) # 0.0 <= x < 10.0
print(int(random() * 10)) # 0 <= x < 10
print(int(random() * 10) +1) # 1 <= x < 11
print(int(random() * 10) +1) # 1 <= x < 11
print(int(random() * 10) +1) # 1 <= x < 11
print(int(random() * 10) +1) # 1 <= x < 11
print(int(random() * 10) +1) # 1 <= x < 11
print(int(random() * 10) +1) # 1 <= x < 11

print(int(random() * 45) + 1) # 1 <= x < 46
print(int(random() * 45) + 1) # 1 <= x < 46
print(int(random() * 45) + 1) # 1 <= x < 46
print(int(random() * 45) + 1) # 1 <= x < 46
print(int(random() * 45) + 1) # 1 <= x < 46
print(int(random() * 45) + 1) # 1 <= x < 46

print(randrange(1,46)) # 1 <= x < 46 # randrange(start, stop) : start <= x < stop
print(randrange(1,46)) # 1 <= x < 46
print(randrange(1,46)) # 1 <= x < 46
print(randrange(1,46)) # 1 <= x < 46
print(randrange(1,46)) # 1 <= x < 46
print(randrange(1,46)) # 1 <= x < 46

print(randint(1, 45)) # 1 <= x <= 45 # randint(start, stop) : start <= x <= stop
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))


# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데, 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비로 제외

#(출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

from random import *

# date = randint(4, 28)
# date = int(random() * 25 + 4) # 다양한 표현방식을 쓸 수 있다
date = randrange(4, 29) 
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")
