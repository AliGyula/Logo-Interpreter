import os
import time
import threading
from gui import gui
from Turtle import Turtle
from pynput.keyboard import Key, Listener

width = 800
height = 600

canGet = False


def onPress(key):
    global canGet
    letter = str(key).replace("'", "")
    if letter == "Key.enter":
        canGet = True
    elif letter == "Key.esc":
        os._exit(0)


def listening():
    with Listener(on_press=onPress) as listener:
        listener.join()


threading.Thread(target=listening).start()


def processText(text):
    words = list(text.split(" "))
    i = 0
    while i < len(words):
        if words[i] == "fd":
            turtle.move(int(words[i + 1]))
            i += 1
        elif words[i] == "bk":
            turtle.move(-(int(words[i + 1])))
            i += 1
        elif words[i] == "rt":
            turtle.turn(360 - (int(words[i + 1])))
            i += 1
        elif words[i] == "lt":
            turtle.turn(int(words[i + 1]))
            i += 1
        elif words[i] == "cs":
            gui.canvas.delete("all")
            turtle.turn(-turtle.angle)
            turtle.setXY(width / 2, height / 2)
            turtle.recreateTurt()
        elif words[i] == "pu":
            turtle.penUp()
        elif words[i] == "pd":
            turtle.penDown()
        elif words[i] == "ht":
            turtle.isTurtleHidden = True
        elif words[i] == "st":
            turtle.isTurtleHidden = False
            turtle.recreateTurt()
        elif words[i] == "setxy":
            x = turtle.x
            y = turtle.y
            turtle.setXY(int(words[i + 1]), -int(words[i + 2]))
            turtle.canvas.create_line(x + turtle.xOff, y + turtle.yOff, turtle.x + turtle.xOff, turtle.y + turtle.yOff)
            i += 2
        elif words[i] == "home":
            x = turtle.x
            y = turtle.y
            turtle.setXY(0, 0)
            turtle.canvas.create_line(x + turtle.xOff, y + turtle.yOff, turtle.x + turtle.xOff, turtle.y + turtle.yOff)
        elif words[i] == "repeat":
            sub = text[text.find('[') + 1:text.rfind(']')]
            for i in range(int(words[i + 1])):
                processText(sub)
            text = text.replace(text[text.find('['):text.rfind(']') + 1], '')
            words = list(text.split(" "))
        elif words[i] == "label":
            turtle.canvas.create_text(turtle.x + turtle.xOff, turtle.y + turtle.yOff, anchor='nw', text=words[i + 1])
            i += 1
        i += 1


if __name__ == '__main__':
    gui = gui(width, height, "Logo Interpreter")
    text = ""
    turtle = Turtle(0, 0, width, height, gui.canvas)
    while 1:
        gui.update()
        gui.update_idletasks()
        turtle.display(gui.canvas)
        if canGet:
            text = gui.text.get()
            canGet = False
            processText(text)
        time.sleep(0.01)

gui.mainloop()
