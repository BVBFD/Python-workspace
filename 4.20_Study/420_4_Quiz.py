def std_weight(height, gender):

    if gender == "남자":
        return round(height/100*height/100*22, 2)

    elif gender == "여자":
        return round(height/100*height/100*21, 2)

    else:
        return "오류입니다."


height = 175
gender = "남자"
weight = std_weight(height, gender)

print("키 {0}cm {1}의 표준 체중은 {2}Kg 입니다."
      .format(height, gender, weight))


# def std_weight(height, gender):

#     if gender == "남자":
#         return round(height * height * 22, 2)

#     elif gender == "여자":
#         return round(height * height * 21, 2)

#     else:
#         return "오류입니다."

# height = 175
# gender = "남자"
# weight = std_weight(height / 100, gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다."\
#     .format(height, gender,weight))
