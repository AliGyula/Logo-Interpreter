import math
from PIL import Image, ImageTk
from tkinter import PhotoImage

class Turtle:
    def __init__(self, x, y, width, height, canvas):
        self.isPenDown = True
        self.isTurtleHidden = False
        self.x = x
        self.y = y
        self.xOff = width/2
        self.yOff = height/2
        self.image = PhotoImage(file='turtle.png')
        self.img=Image.open('turtle.png')
        self.image = ImageTk.PhotoImage(self.img)
        self.canvas = canvas
        self.angle = 0
        self.turt = self.canvas.create_image(self.x + self.xOff, self.y + self.yOff, image=self.image)


    def move(self, val):
        angle_in_radians = math.radians(self.angle)
        line_length = val
        center_x = self.x
        center_y = self.y
        xn = center_x - line_length * math.sin(angle_in_radians)
        yn = center_y - line_length * math.cos(angle_in_radians)
        if self.isPenDown:
            self.canvas.create_line(self.x + self.xOff, self.y + self.yOff, xn + self.xOff, yn + self.yOff)
        self.x = xn
        self.y = yn

    def turn(self, angle):
        self.angle += angle
        if self.angle >= 360:
            self.angle = self.angle % 360
        self.image = ImageTk.PhotoImage(self.img.rotate(self.angle))

    def penUp(self):
        self.isPenDown = False

    def penDown(self):
        self.isPenDown = True

    def display(self, canvas):
        if self.isTurtleHidden:
            self.canvas.delete(self.turt)
        else:
            self.canvas.coords(self.turt, self.x + self.xOff, self.y + self.yOff)
            self.canvas.itemconfig(self.turt, image=self.image)

    def recreateTurt(self):
        self.setXY(0, 0)
        self.turt = self.canvas.create_image(self.x, self.y, image=self.image)

    def setXY(self, x, y):
        self.x = x
        self.y = y