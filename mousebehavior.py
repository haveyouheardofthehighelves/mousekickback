from pynput.mouse import Listener
import logging

def readin(x, y):
    file1 = open("weapon.txt", "r")
    print(file1.read())
    file1.close()


def firing(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
    else:
        print('released ' + str(button))


with Listener(on_move=readin, on_click=firing) as listener:
    listener.join()
