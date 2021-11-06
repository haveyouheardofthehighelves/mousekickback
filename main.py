import pytesseract as tess
import pyautogui
from PIL import Image
import time
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Page segmentation modes:
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR.
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line,
#                         bypassing hacks that are Tesseract-specific.
# list of primary weapons smg,rifles, machine guns,
primary_weapons_list = [["stinger", "spectre"],
                        ["bulldog", "guardian", "phantom", "vandal"],
                        ["marshal", "operator"],
                        ["ares", "odin"],
                        ["bucky", "judge"]]

holding = ""

def stuffs():
    global holding
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\sethy\PycharmProjects\mousekickback\valorant.png')
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
                print(primary_weapons_list[i][j])
                holding = primary_weapons_list[i][j]
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

while True:
    stuffs()
    time.sleep(.01)
