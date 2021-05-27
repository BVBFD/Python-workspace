from random import *

#일반 유닛
class unit :
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))
        

#공격 유닛
class attackunit(unit): #self는 메모리에 저장되는 주소값이라고 생각하면 편함.
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# 마린
class Marine(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도 증가, 체력 10 감소
    def steampack(self):
        if self.hp > 10 :
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".\
                format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".\
                format(self.name))

# 탱크
class Tank(attackunit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        attackunit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#드랍쉽
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛    
class flyableattackunit(attackunit, flyable):
    def __init__ (self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, damage, 0) #지상 스피드 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        # print("[공중 유닛 이동]")
        self.fly(self.name, location)
 

class Wraith(flyableattackunit):
    def __init__(self):
        flyableattackunit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다".format(self.name))
            self.clocked = False
        
        else: # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

Wraith_1 = Wraith()

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append 처리)
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

# 전군 이동
for unit in attack_unit:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다")

# 공격 모드 준비 (탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_unit:
    if isinstance(unit, Marine):
        unit.steampack()
    
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    
    elif isinstance(unit, Wraith):
        unit.clocking()
    

# 전군 공격
for unit in attack_unit:
    unit.attack("1시")

# 전군 피해
for unit in attack_unit:
    unit.damaged(randint(5, 21))  #공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()

# #메딕 : 의무병 (상속)

# #파이어 뱃
# firebat1 = attackunit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


# #드랍쉽
# class flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
    
# #공중 공격 유닛    
# class flyableattackunit(attackunit, flyable):
#     def __init__ (self, name, hp, damage, speed, flying_speed):
#         attackunit.__init__(self, name, hp, damage, 0) #지상 스피드 0
#         flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
 
# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = attackunit("벌쳐", 80, 10, 20)

# # 배틀크루져 
# battlecruiser = flyableattackunit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# class BuildingUnit(unit):
#     def __init__(self, name, hp, location):
#         # unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) 
#         # 위에 꺼라 비교해서 super(). 포함해서 self는 쓰지 않는다.
#         # 결과는 위에꺼랑 똑같음
#         self.location = location

#     def build(self):
#         print("{0} 건물이 {1}에 지어졌습니다.\n"\
#             .format(self.name, self.location))    

# # 서플라이 디폿 : 건물 1개 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
# supply_depot.build()