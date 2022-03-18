from canvas import Canvas
from shapes import Square, Rectangle

canvas_height = int(input("canvas height? "))
canvas_width = int(input("canvas width? "))
canvas_color = input("canvas color? white or black? ")
if canvas_color == "white":
    canvas_color = [255, 255, 255]
else:  # black
    canvas_color = [0, 0, 0]
canvas1 = Canvas(canvas_height, canvas_width, canvas_color)
while 1 > 0:
    shape = input("What dou you want to paint? square, rectangle or none ")
    if shape == "square":
        x = int(input("Square's x ? "))
        y = int(input("Square's y = "))
        side = int(input("Square's side? "))
        color1 = int(input("Square's color[1]? "))
        color2 = int(input("Square's color[2]? "))
        color3 = int(input("Square's color[3]? "))
        square1 = Square(x=x, y=y, side=side, color=(color1, color2, color3))
        square1.draw(canvas=canvas1)
    elif shape == "rectangle":  # rectangle
        x = int(input("Rectangle's x ? "))
        y = int(input("Rectangle's y ? "))
        width = int(input("Rectangle's width? "))
        height = int(input("Rectangle's height? "))
        color1 = int(input("Rectangle's color[1]? "))
        color2 = int(input("Rectangle's color[2]? "))
        color3 = int(input("Rectangle's color[3]? "))
        rectangle1 = Rectangle(x=x, y=y, width=width, height=height, color=(color1, color2, color3))
        rectangle1.draw(canvas=canvas1)
    elif shape == "none":
        canvas1.make("image.png")
        quit()
