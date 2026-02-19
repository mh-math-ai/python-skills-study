# 반복문 (for)
# for 변수 in 반복가능한객체:
#     반복할 코드
# 반복가능한객체: 리스트, 튜플, 문자열 등

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# 이런 과정을 계속해서 반복해야 할때 쓸 수 있는 게 for 구문

# for waiting_no in [0, 1, 2, 3, 4]: 
#     print("대기번호 : {0}" .format(waiting_no)) 

# for waiting_no in range(1,6): # 1, 2, 3, 4, 5
#     print("대기번호 : {0}" .format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks: # for 구문에서 새로운 변수를 정의할 수 있다 
    print("{0}, 커피가 준비되었습니다." .format(customer)) # 그 변수를 포맷에 사용할 수 있다 