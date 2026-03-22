# 상속 (inheritance)
# 상속은 기존 클래스(부모 클래스)의 속성과 메소드를 새로운 클래스(자식 클래스)가 물려받는 것입니다. 

# # 일반 유닛 

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         print("{0} 유닛이 생성되었습니다.".format(self.name))

# # 공격 유닛

# class AttackUnit:
#     def __init__(self, name, hp, damage): 
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location): 
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage): 
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# 이 클래스들은 __init__메소드의 self.name과 self.hp 멤버변수를 공유합니다
# 이 경우 상속을 사용하면 코드의 중복을 피할 수 있습니다.

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 이 일반유닛 클래스가 부모 클래스가 됩니다 

class AttackUnit(Unit): # Unit 클래스를 부모 클래스로 지정합니다
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location): 
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage): 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16) # __init__ 메소드를 실행합니다 
firebat1.attack("5시") # attack 메소드를 실행합니다

firebat1.damaged(25) # damaged 메소드를 실행합니다
firebat1.damaged(25)
