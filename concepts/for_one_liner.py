# 한 줄로 for 문 활용법
# for문에서 반복할 것을 한 줄로 나타내기
# 출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104, 
# student = [1, 2, 3, 4, 5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# 학생 이름을 길이로 변환
# students = ["Iron Man", "Thor", "I am Groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron Man", "Thor", "I am Groot"]
# students = [i.upper() for i in students]
# print(students)

# students = [students.upper(i) for i in students]
# print(students)
# list object는 upper method를 가지고 있지 않다.


# Quiz) 당신은 Cocoa 서비스를 이용하는 택시기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객: 2 분

from random import *
customer = range(1, 51)
customer = list(customer)
customer = [randint(5, 50) for i in customer] 
x = 0

for i in range(0, 50):
    if customer[i] <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i+1, customer[i]))
        x += 1
    else:
        print("[X] {0}번째 손님 (소요시간 : {1}분)".format(i+1, customer[i]))
        
print("총 탑승 승객: {} 분".format(x))


from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[X] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객: {} 분".format(cnt)) 
