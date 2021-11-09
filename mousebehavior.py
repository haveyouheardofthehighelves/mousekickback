from pynput.mouse import Listener
import logging
import serial

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

holding = False
ser = serial.Serial("COM7", 9600, timeout=0)
ser.xonxoff = 1
save = ""
pressing = False
def on_move(x, y):
    file1 = open("weapon.txt", "r")  # write mode
    print(file1.read())
    file1.close()

def readin(x, y):
    global holding
    global save
    #a = ser.readline()
    file1 = open("weapon.txt", "r")
    a = str(file1.read()).strip()
    if a != "":
        holding = True
    else:
        holding = False
    if holding and not pressing and save != a:
        ser.write(b'w')
        if a == "vandal":
            ser.write(b'3')
            ser.write(b'6')
        elif a == "phantom":
            ser.write(b'2')
            ser.write(b'5')
        elif a == "spectre":
            ser.write(b'2')
            ser.write(b'0')
        elif a == "stinger":
            ser.write(b'1')
            ser.write(b'5')
        elif a == "ares":
            ser.write(b'3')
            ser.write(b'5')
        elif a == "odin":
            ser.write(b'2')
            ser.write(b'5')
        elif a == "bulldog":
            ser.write(b'4')
            ser.write(b'5')
        elif a == "bucky" or "judge" or "operator" or "marshall" or "guardian":
            ser.write(b't')
        ser.write(b'w')
        save = a

    file1.close()
def firing(x, y, button, pressed):
    global holding
    global pressing
    if holding:
        if str(button) == "Button.left":
            if pressed:
                ser.write(b'e')
                ser.write(b'1')
                ser.write(b'e')
                pressing = True
            else:
                ser.write(b'e')
                ser.write(b'0')
                ser.write(b'e')
                pressing = False


with Listener(on_move=readin, on_click=firing) as listener:
    listener.join()