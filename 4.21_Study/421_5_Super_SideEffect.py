class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__()   
        #하지만 다중상속에서 문제가 생긴다. 
        #마지막 상속자만 표시가 됨.. -> 문제가 됨
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()