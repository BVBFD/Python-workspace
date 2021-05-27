#일반 유닛
class unit :
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#공격 유닛
class attackunit(unit): #self는 메모리에 저장되는 주소값이라고 생각하면 편함.
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# #메딕 : 의무병 (상속)


# #파이어 뱃
# firebat1 = attackunit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


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
        attackunit.__init__(self, name, hp, damage)
        flyable.__init__(self, flying_speed)

#발퀴리
valkyrie = flyableattackunit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
