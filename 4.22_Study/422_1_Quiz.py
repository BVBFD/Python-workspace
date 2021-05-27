# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세  5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{0} {1} {2} {3} {4}"\
            .format(self.location, self.house_type, self.deal_type,\
                self.price, self.completion_year))        

MyHouse1 = House("부산", "아파트", "전세", "10억", "2020년")
MyHouse2 = House("강남", "아파트", "매매", "10억", "2010년")
MyHouse3 = House("마포", "오피스텔", "전세", "5억", "2007년")
MyHouse4 = House("송파", "빌라", "월세", "500/50", "2000년")
MyHouse5 = House("서울", "아파트", "전세", "60억", "2021년")

Total_MyHouse = []
Total_MyHouse.append(MyHouse1)
Total_MyHouse.append(MyHouse2)
Total_MyHouse.append(MyHouse3)
Total_MyHouse.append(MyHouse4)
Total_MyHouse.append(MyHouse5)

Total_MyHouse.count(House)
c = len(Total_MyHouse)
print(c)

for i in Total_MyHouse:
    if i == MyHouse1:
        print("총 {0}대 매물이 있습니다.".format(c))
    i.show_detail()