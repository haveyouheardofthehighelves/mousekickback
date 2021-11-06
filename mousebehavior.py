from pynput.mouse import Listener
import logging
import serial

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

holding = False
ser = serial.Serial("COM6", 9600, timeout=0)
ser.xonxoff = 1

def on_move(x, y):
    file1 = open("weapon.txt", "r")  # write mode
    print(file1.read())
    file1.close()

def readin(x, y):
    global holding
    file1 = open("weapon.txt", "r")
    if str(file1.readline()).strip() != "":
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