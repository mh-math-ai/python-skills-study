# 파일 입출력 (File Input and Output)
# 파일을 읽어오거나, 파일에 내용을 쓰는 방법이다.
# 파일은 바이트 단위로 읽어오거나, 쓸 수 있다.
# 파일을 열고, 닫아주어야 한다.

# score_file = open("score.txt", "w", encoding="utf8") 
# # # open("파일 이름", "모드", encoding="인코딩 방식")
# # # 모드 : w는 쓰기, r은 읽기, a는 추가, x는 새로 만들기

# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 파일을 닫아주어야 한다.

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end = "")
# print(score_file.readline(), end = "")
# print(score_file.readline(), end="")
# score_file.close()


# 파일이 총 몇줄인지 모른다면

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()


# 파일의 내용을 전부 가져와서 리스트 형태로 저장하는 방법

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # 파일의 내용을 전부 가져오고, 리스트로 저장한다. 
for line in lines:
    print(line, end="")
score_file.close()