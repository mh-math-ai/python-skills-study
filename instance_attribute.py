# 멤버 변수 (Instance/Data Attribute)

class Unit:
    def __init__(self, name, hp, damage): # __init__ 함수는 생성자이다 
        self.name = name
        self.hp = hp
        self.damage = damage # 이것들이 멤버 변수이다 
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력  {0}, 공격력 {1}\n".format(self.hp, self.damage))


# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}\n공격력 : {1}".format(wraith1.name, wraith1.damage))
# 이런 식으로 멤버 변수를 불러올 수 있다

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 객체에 추가로 변수를 만들어서 쓸 수 있다 

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

if wraith1.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 확장된 변수는 기존의 인스탄스에는 추가가 되지 않는다. 