import pytesseract as tess
import pyautogui
from PIL import Image

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# list of primary weapons smg,rifles, machine guns,
primary_weapons_list = [["stinger", "spectre"],
                        ["bulldog", "guardian", "phantom", "vandal"],
                        ["marshal", "operator"],
                        ["ares", "odin"],
                        ["bucky", "judge"]]


def stuffs():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\sethy\PycharmProjects\Valorantshooting\valorant.png')
    img = Image.open('valorant.png')
    width, height = img.size
    left = 1700
    top = height / 1.3
    right = 1850
    bottom = 925
    primary_weapon = img.crop((left, top, right, bottom))
    data = [tess.image_to_string(primary_weapon, lang='eng', config='--psm 6')]
    print(data[0])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

stuffs()
