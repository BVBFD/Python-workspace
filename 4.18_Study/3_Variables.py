# 애완동물을 소개해 주세요~

print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# 수정 전
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# 수정 후
print("우리집 강아지의 이름은 해피에요")
print("해피는 4살이며, 산책을 아주 좋아해요")
print("해피는 어른일까요? True")

name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3 # age 값이 3 이상이면 True, 미만이면 False

name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 연탄이에요")
print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

animal = "고양이"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
name = "해피"
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))


