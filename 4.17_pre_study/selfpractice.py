class animal:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def introduce(self):
        print("안녕하세요. 저의 강아지 이름은 " + self.name + "입니다.")
        print("지금 " + str(self.age) + "살이며, " + self.hobby + "를 좋아합니다.")

        if self.age >= 3:
            print("올해, " + str(self.age) + "살이며, 성견입니다.")
        else:
            print("올해, " + str(self.age) + "살이며, 아직 미성견입니다.")


myDog = animal("영춘이", 8, "공놀이")
myDog.introduce()

otherDog = animal("영웅이", 2, "축구")
otherDog.introduce()
