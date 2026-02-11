## 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))


## 애완동물을 소개해주세요
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + " 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요")
## 정수형을 넣을 떄는 str()로 감싸줘야함
print(name + "는 어른일까요? " + str(is_adult))
## bool형도 str()로 감싸줘야함 
