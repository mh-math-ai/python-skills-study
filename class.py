# 클래스 (Class)
# 클래스는 객체를 만들기 위한 틀이다.
# 클래스에서 정의한 변수나 함수는 모두 인스턴스(객체)가 공유하는 멤버로 사용된다.
# 클래스의 이름은 대문자로 시작한다.
# 인스턴스(객체)를 만들기 위해서는 클래스명을 사용하면 된다.


# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쓸 수 있는데, 일반 모드와 시즈모드가 있다

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다 [공격력 {2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# # 만약 탱크 하나가 더 생긴다면

# tank2_name = "탱크2"
# tank_hp = 150
# tank_damage = 35

# # 현실적으로 수백개의 유닛이 만들어지는 게임에서 이런 식으로 진행하기는 어렵다
# # 이럴 때 클래스를 사용한다

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력  {0}, 공격력 {1}\n".format(self.hp, self.damage))

marin1 = Unit("마린", 40, 5)
marin2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
