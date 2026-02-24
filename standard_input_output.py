# 표준 입출력 (Standard Input/Output)
# 줄여서 stdio라고도 한다.
# 표준 입력은 stdin, 표준 출력은 stdout, 표준 에러는 stderr

# print("Python", "Java", sep = ",") # print() 함수의 sep 인자를 사용하여 구분자를 지정한다.

# print("Python", "Java", "JavaScript", sep = " vs ")

# print("Python", "Java", sep = ",", end="?")
# print("무엇이 더 재밌을까요?") # end 인자는 마지막에 출력할 문자열을 지정한다. 기본값은 줄바꿈 

# import sys # sys 모듈은 파일의 시스템 상태를 나타내는 정보를 제공한다.
# # sys.stdin : 표준 입력을 나타내는 객체
# # sys.stdout : 표준 출력을 나타내는 객체
# # sys.stderr : 표준 에러를 나타내는 객체

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #.items는 키와 밸류를 튜플로 묶어서 리스트에 담아주는 역할을 한다.
#    # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # .ljust(%d)  : %d 자리수만큼 왼쪽에서 공백을 넣어주는 역할을 한다.
#    # print(subject.rjust(8), score) # .rjust(%d) : %d 자리수만큼 오른쪽에서 공백을 넣어주는 역할을 한다.
#    # print(subject.center(8), score) # .center(%d) : %d 자리수만큼 가운데에서 공백을 넣어주는 역할을 한다.

# 은행 대기 순번표
# # 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) #/zfill(%d) : %d 자리수만큼 왼쪽에서 공백을 넣어주는 역할을 한다.

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 숫자를 입력해도 문자열로 인식한다.
print("입력하신 겂은 " + answer + "입니다.")

# 사용자 입력값을 받게 되면 항상 문자열로 인식한다. 숫자로 인식하게 만드려면 int()를 사용해야 한다
