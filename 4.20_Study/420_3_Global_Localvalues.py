gun = 10  # 전역 변수

# def checkpoint(soldiers):
#     global gun # global 전역 공간에 있느 gun을 사용
#     gun = gun - soldiers  #2 번째 gun 지역변수
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
