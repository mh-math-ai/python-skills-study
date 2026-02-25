# __init__ 함수
# init의 역할은 생성자(constructor)이다 
# 클래스로부터 객체(인스턴스)를 생성할 때 가장 먼저 자동으로 실행되는 함수이다
# 주로 객체의 초기 상태(속성)을 설정하는 데 사용한다

class Unit:
    def __init__(self, name, hp, damage): # __init__ 함수는 생성자이다 
        self.name = name
        self.hp = hp
        self.damage = damage 
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력  {0}, 공격력 {1}\n".format(self.hp, self.damage))

# marine3 = Unit("마린", 40) 
# 이 경우 오류가 난다. init에 들어간 모든 인자를 넣어주어야만 생성된다. 