# 튜플
# 내용변경이나 삭제가 불가능한 자료형
# 리스트와 거의 비슷하지만, ()로 감싸서 표현한다.
# 튜플은 리스트보다 메모리를 적게 사용한다.
# 튜플은 리스트보다 속도가 빠르다.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") # 튜플은 내용 변경이 불가능하다. 에러 발생 

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
name, age, hobby = "김종국", 20, "코딩" # 튜플을 이용한 여러 변수에 값을 한꺼번에 할당하는 방법
print(name, age, hobby)