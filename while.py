# 반복문 (while)
# while문은 조건이 True일 동안 실행하는 반복문이다.
# 조건이 False가 될 때까지 무한히 반복해서 실행된다.
# 반복문을 벗어나기 위해서는 break를 사용하면 된다.

# customer = "토르"
# index = 5
# while index >= 1: # 조건이 True일 동안 무한히 반복해서 실행한다.
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1 # index를 감소시킨다.
#     if index == 0: # index가 0일 경우
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1 # break 조건 없이 실행하면 무한히 실행된다.

customer = "토르"
person = "Unknown"

while person != customer : # != Not Equal To 조건이 False일 동안 무한히 반복해서 실행한다. 
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


