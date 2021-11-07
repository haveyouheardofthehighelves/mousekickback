from pynput.mouse import Listener
import logging
import serial

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

holding = False
ser = serial.Serial("COM7", 9600, timeout=0)
ser.xonxoff = 1
save = ""
def on_move(x, y):
    file1 = open("weapon.txt", "r")  # write mode
    print(file1.read())
    file1.close()

def readin(x, y):
    global holding
    file1 = open("weapon.txt", "r")
    a = str(file1.read()).strip()

    if a != "":
        if a == "vandal":
            ser.write(b'v')
        elif a == "phantom":
            ser.write(b'p')
        elif a == "spectre":
            ser.write(b's')
        elif a == "bulldog":
            ser.write(b'u')
        elif a == "ares":
            ser.write(b'a')
        elif a == "odin":
            ser.write(b'o')
        elif a == "stinger":
            ser.write(b'i')



        holding = True

    else:
        holding = False
    file1.close()


def firing(x, y, button, pressed):
    global holding
    if holding:
        if str(button) == "Button.left":
            if pressed:
                ser.write(b'e')
                ser.write(b'1')
                ser.write(b'e')
            else:
                ser.write(b'e')
                ser.write(b'0')
                ser.write(b'e')


with Listener(on_move=readin, on_click=firing) as listener:
    listener.join()