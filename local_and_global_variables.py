# 지역 변수와 전역 변수 (local variable and global variable)
# 지역 변수는 함수 안에서만 사용할 수 있고, 전역 변수는 프로그램 전체에서 사용할 수 있다.
# 지역 변수는 함수가 종료되면 사라진다.
# 전역 변수는 프로그램이 종료될 때까지 살아있다.

# 11

# def checkpoint(soldiers): # 경계근무 나가는 군인들 
#     gun = 20 # 함수 내에서 gun을 사용하기 위해서는 지역변수로 선언한다.
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감 
# print("남은 총 : {0}".format(gun))

# def checkpoint(soldiers): # 경계근무 나가는 군인들 
#     global gun # 전역 공간에 있는 gun 사용하기 위해서 global을 선언한다.
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감 
# print("남은 총 : {0}".format(gun))

# 전역변수를 많이 쓰게 되면 코드관리가 어려워지므로 일반적으로 권장되는 방법은 아님
# 가급적 함수의 전달값으로 계산하고 반환값을 받아 사용하는 게 좋음

# def checkpoint(soldiers): 
#     global gun 
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun # return을 사용해서 값을 반환한다. 하지 않으면 반환값이 None이다.

# print("전체 총: {0}".format(gun))
# gun = checkpoint_ret(gun, 2)

# print("남은 총 : {0}".format(gun))


# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#        * 함수명 : std_weight
#        * 전달값: 키(height), 성별(gender)

# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

height = input("키를 입력하세요(cm)")
gender = input("성별을 입력하세요. ex) 남자 or 여자")

def std_weight(height, gender):
    height = float(height)
    if gender == "남자":
        std_weight = height * height * 22 / 10000
    else:
        std_weight = height * height * 21 / 10000
    return std_weight 

weight_result = std_weight(height, gender)

print(f"키 {height}cm {gender}의 표준 체중은 {weight_result:.2f}kg 입니다.")


# 정답

def std_weight(height, gender): # 키 m 단위(실수), 성별 "남자" / "여자"abs
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))