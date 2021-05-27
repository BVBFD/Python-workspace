score_file = open("score.txt", "w", encoding = "utf8")
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8") 
print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")

score_file = open("score.txt", "w", encoding = "utf8")
score_file.write("과학 :80")
score_file.write("\n코딩 : 100")
score_file.write("\n수학 : 0")
score_file.write("\n영어 : 50")

score_file = open("score.txt", "r", encoding = "utf8")
while True :
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()

# Point_file = open("Point.txt", "w", encoding = "utf8")
# Point_file.write("수학 : 95")
# Point_file.write("\n영어 : 100")
# Point_file.write("\n국어 : 85")
# Point_file.write("\n코딩 : 90")
# Point_file.close()

# Point_file = open("Point.txt", "r", encoding = "utf8")
# print(Point_file.readline(), end = "")
# print(Point_file.readline(), end = "")
# print(Point_file.readline(), end = "")
# print(Point_file.readline(), end = "")
# Point_file.close()

# Score_file = open("Score.txt", "w", encoding = "utf8")
# Score_file.write("코딩 : 100점")
# Score_file.write("\n영어 : 95점")
# Score_file.write("\n국어 : 90점")
# Score_file.write("\n스페인어 : 95점")

# Score_file = open("Score.txt", "r", encoding = "utf8")
# print(Score_file.read())
# Score_file.close()
