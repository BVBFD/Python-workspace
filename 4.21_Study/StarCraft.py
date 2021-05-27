#일반 유닛 
class Unit:
     def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

     def move(self, location):
         print("[지상 유닛 이동]")
         print("{0} : {1}방향으로 이동합니다. [속도 {2}]\n"\
           .format(self.name, location, self.speed ))

#공격 유닛 : 배틀크루져(마법), 레이스(*), 벌쳐(*)
class AttackUnit(Unit):
     def __init__(self, name, hp, speed, attack_damage):
        Unit.__init__(self, name, hp, speed)
        self.attack_damage = attack_damage
        

#메딕 : 의무병
class HealUnit(Unit):
     def __init__(self):
        Unit.__init__(self, "메딕", 150, 3)
        self.heal_amount = 25
  
     def heal(self, heal_to_unit):
         print("{0}: 메딕이 {1}에게 {2}HP 치료했습니다.\n"\
           .format(self.name, heal_to_unit, self.heal_amount))

class DropShip(Unit):
     def __init__(self):
        Unit.__init__(self, "드랍쉽", 300, 10)
        self.amount = 15

     def Geton(self, Geton_Amount):
         print("[{0}이 {1} 유닛을 태웠습니다]\n"\
           .format(self.name, Geton_Amount))

     def Getdown(self, Getdown_Amount):
         print("[{0}이 {1} 유닛을 태웠습니다]\n"\
           .format(self.name, Getdown_Amount))

     def move(self, location):
         print("[공중 유닛 이동]")
         print("{0} : {1}방향으로 이동합니다. [속도 {2}]\n"\
           .format(self.name, location, self.speed ))      

class FireBat(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "파이어뱃", 100, 3, 5)
        self.fire_damage = 10
        self.steam_packed = str("n")
        print("파이어 뱃이 생성되었습니다.")

    def steam_pack_on(self):

        self.steam_packed = input("스팀팩을 사용하시겠습니까? (y/n) ")

        if self.steam_packed == str("y") or self.steam_packed == str("Y"):
          print("스팀팩이 발동 되었습니다.")
          self.hp -= 10
          self.attack_damage += 10
          self.fire_damage += 10
          print("{0}의 파워는 {1} 증가, 화력은 {2}증가 체력은 {3} 감소합니다.\n"\
            .format(self.name, self.attack_damage, self.fire_damage, self.hp))
        
        elif self.steam_packed == str("n") or self.steam_packed == str("N"):
             self.attack_damage -= 10
             self.fire_damage -= 10
             print("파워가 원상 복귀 됩니다. (-10)\n")
        
        else:
          print("지정이 취소 되었습니다.\n")
          

class BattleCruiser(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "배틀크루져", 800, 15, 80)
        self.missile_damage = 600

    def missile_shot(self):
        print("미사일이 발사 되었습니다. 목표타겟이 {0} 만큼의 데미지를 입었습니다.\n"\
          .format(self.missile_damage))

    def move(self, location):
         print("[공중 유닛 이동]")
         print("{0} : {1}방향으로 이동합니다. [속도 {2}]\n"\
           .format(self.name, location, self.speed ))   



# Dropship1 = DropShip()
# Dropship1.Geton(8)
# Dropship1.Getdown(10)
# Dropship1.move("3시 방향")

# medic = HealUnit()
# medic.heal("마린")
# medic.move("3시 방향")

# FireBat1 = FireBat()
# FireBat1.steam_pack_on()
# FireBat1.move("9시 방향")

BattleCruiser1 = BattleCruiser()
BattleCruiser1.move("6시 방향")
BattleCruiser1.missile_shot()


# for i in range(1, 101):
#   FireBat_100 = FireBat()
#   print("파이어뱃 {0}마리가 훈련되어졌습니다.".format(i))

# for i in range(1, 101):
#   f = FireBat()
  
# print("파이어 뱃 총 {0}기가 전투준비 완료했습니다!".format(i))



