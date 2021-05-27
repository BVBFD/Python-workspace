class SoldOutError(Exception):
    def __init__(self):
        pass

chicken = 10 
waiting = 0

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))

        if order <= chicken:
            chicken -= order
            waiting += 1
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다."\
                .format(waiting, order))
        
        elif order <= 0:
            raise ValueError
        
        elif order >= chicken:
            print("재고가 부족하여 주문하실 수 없습니다.")

        if chicken == 0:
            raise SoldOutError
    
    except ValueError:
        print("입력값을 다시 입력해주세요.")

    except SoldOutError:
        print("재고가 부족하여 주문하실 수 없습니다.")
        break