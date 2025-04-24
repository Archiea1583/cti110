#Amir Archie
#3/17/25
#P4LAB
#Using turtle graphics, and either a while or for loop, write a program that draws both a square and a triangle.

import turtle
win = turtle.Screen()
pen = turtle.Turtle()

pen.pensize(5)
pen.pencolor("Pink")
pen.shape("arrow")

for side in range(4):
    pen.forward(100)
    pen.left(90)

sides = 3
while sides > 0 :
    pen.forward(100)
    pen.left(120)
    sides = sides - 1








win.mainloop()
