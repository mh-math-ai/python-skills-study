# 메소드 (Method)
# 메소드는 클래스에 종속된 함수 입니다 (__init__ 등)
# 메소드는 첫 번째 매개변수로 항상 self를 받습니다(객체 자신을 참조)
# 객체이름.메소드이름() 형태로 호출합니다 

class Unit:
    def __init__(self, name, hp, damage): # __init__ 메소드는 생성자입니다
        self.name = name
        self.hp = hp
        self.damage = damage # 이것들은 멤버 변수입니다 
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력  {0}, 공격력 {1}\n".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 유닛이 공격하는 동작을 정의한 메소드입니다 
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage): # 유닛이 피해를 입는 동작을 정의한 메소드입니다 
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염 방사기
firebat1 = AttackUnit("파이어뱃", 50, 16) # __init__ 메소드를 실행합니다 
firebat1.attack("5시") # attack 메소드를 실행합니다

firebat1.damaged(25) # damaged 메소드를 실행합니다
firebat1.damaged(25)
