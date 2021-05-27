from random import *

ID = []
for i in range(1, 101):
    ID.append(i)

shuffle(ID)
# print(sample(ID,1))
# print(sample(ID,3))

print("--------당첨자 발표-------")
print("치킨 당첨자 : " + str(sample(ID, 1)))
shuffle(ID)
print("커피 당첨자 : " + str(sample(ID, 3)))
print("---------축하합니다-------")

# Chicken = randint(1,101)
# print(Chicken)

# Coffee = sample(range(1,101),3)
# print(Coffee)

# print("--------당첨자 발표-------")
# print("치킨 당첨자 : " + str(Chicken))
# print("커피 당첨자 : " + str(Coffee))
# print("---------축하합니다-------")

print("로또 번호는 다음과 같습니다 : " + str(sample(range(1, 101), 7)))
