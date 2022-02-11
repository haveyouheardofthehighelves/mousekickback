import pytesseract as tess
import pyautogui
from PIL import Image, ImageFile
import time

ImageFile.LOAD_TRUNCATED_IMAGES = True

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# list of primary weapons smg,rifles, machine guns,
primary_weapons_list = [["stinger", "spectre"],
                        ["bulldog", "guardian", "phantom", "vandal"],
                        ["marshal", "operator"],
                        ["ares", "odin"],
                        ["bucky", "judge"]]

holding = ""
writing = False


def stuffs():
    global holding
    global writing
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'valorant.png')
    img = Image.open('valorant.png')
    width, height = img.size
    left = 1700
    top = height / 1.3
    right = 1850
    bottom = 925
    primary_weapon = img.crop((left, top, right, bottom))
    data = [tess.image_to_string(primary_weapon, lang='eng', config='--psm 6')]
    for i in range(len(primary_weapons_list)):
        for j in range(len(primary_weapons_list[i])):
            if primary_weapons_list[i][j] in data[0].strip().lower():
                #print(primary_weapons_list[i][j])
                holding = primary_weapons_list[i][j]
                writing = True
                file1 = open("weapon.txt", "w+")  # write mode
                file1.write(holding)
                file1.close()
                writing = False


while True:
    try:
        stuffs()
    except:
        print("yikes")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
