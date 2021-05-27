from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("img.png")

# C3 위치에 img.png 파일의 이미지 삽입
# pip install pillow 설치하기 (동작 안된다면) You must install Pillow to fetch image objects
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")