class Unit: 
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()
        # Unit.__init__(self)
        # Flyable.__init__(self) # 슈퍼를 끄고 이렇게 정의하면 두 클래스가 같이 호출이 된다 

# 드랍쉽
dropship = FlyableUnit()

# 이 경우 먼저 상속을 받은 클래스로 호출이 된다 
# 슈퍼를 쓰면 순서상 맨 처음 상속을 받는 클래스로 호출이 된다


