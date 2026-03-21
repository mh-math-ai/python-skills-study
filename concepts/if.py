# 분기 (if 문) 
# 조건에 따라 실행할 명령을 선택하는 제어문
# if 조건식:
#    실행 명령문
# else:
#    실행 명령문

# weather = "비"
# if weather == "비":
#     print("우산을 챙기세요")

# weather = "맑음"
# if weather == "비":
#     print("우산을 챙기세요")
# # 조건이 참이 아니면 아무것도 실행되지 않음

# weather = "맑아요"
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요") # elif는 여러 조건을 추가할 때 사용, else if 의 줄임말
# else:
#     print("준비물이 필요 없어요")

# weather = input("오늘 날씨는 어때요?") # 사용자로부터 입력을 받는 함수
# if weather == "비" or weather == "눈": # or 연산자를 사용하여 여러 조건을 하나로 묶을 수 있음
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

temp = int(input("오늘 기온은 어때요?")) # 입력받은 값을 정수로 변환
if temp >= 30:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # and 연산자를 사용하여 여러 조건을 모두 만족해야 하는 경우
    print("날씨가 괜찮아요")
elif 0 <= temp <10: # 비교 연산자를 사용하여 범위를 지정할 수 있음
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")



