# 가변 인자 (arbitrary argument)
# 가변 인자에는 가변 위치 인자(Arbitrary positional argument)와 
# 가변 키워드 인자(Arbitrary keyword argument)가 있다.
# 가변 인자에는 *(asterisk) 기호가 붙어서 나타난다.
# 가변 위치 인자는 함수의 마지막 인자이고, 가변 키워드 인자는 중간에 나타난다.
# 가변 위치 인자는 리스트나 튜플로 만들어서 전달하고, 가변 키워드 인자는 딕셔너리로 만들어서 전달한다.
# 가변 위치 인자에서 리스트나 튜플로 만들어서 전달하는 값은 인자의 순서대로 전달된다.


# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end = " ") # end = ""은 줄바꿈을 하지 않는다.
#     print(lang1, lang2, lang3, lang4, lang5)

# 만약 계속해서 빈칸을 남겨두어야 한다면 데이터입력에 시간이 많이 걸리고
# 더 많은 언어를 사용하는 사람이 있다면 함수 자체를 변경해야한다.
# 이럴 때 가변인자를 사용한다 


def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
