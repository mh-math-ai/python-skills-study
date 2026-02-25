print("백문이 불여일견
백견이 불여일타")

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")


# print("저는 "나도코딩"입니다.")
print('저는 "나도코딩"입니다.')
# \", \' : 문장 내 따옴표 사용
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \ 사용
print("~\\Documents\\Python\\PythonPractice")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") #PineApple이 출력됨

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple") #RedApple이 출력됨

# # \t : 탭 (4칸 띄어쓰기)
# print("Red\tApple") #Red    Apple이 출력됨

# Quiz : 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 개수 + "!"로 구성
# 예) 생성된 비밀번호 : nav51!

#url = "http://naver.com"
url = "http://daum.net"
password = url.replace("http://", "") 
#print(password) # naver.com이 출력됨
password = password[:password.index(".")]
#password = password[:5] -> 0부터 5미만까지의 문자열 출격, (0, 1, 2, 3, 4)
#print(password) # naver가 출력됨 
password = password[:3] + str(len(password)) + str(password.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))
print(f"{url}의 비밀번호는 {password}입니다.")

# url = "http://google.com"
# password = url.replace("http://", "") 
# password = password[:password.index(".")]
# password = password[:3] + str(len(password)) + str(password.count("e")) + "!" 
# print(f"{url}의 비밀번호는 {password}입니다.")
