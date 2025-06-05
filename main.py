from turtle import *

shape("turtle")  # форма черепашки
colormode(255)

bgcolor("sienna")  # цвет фона
speed(1)  # скорость черепашки

pencolor("red")
pensize(3)

penup()
forward(100)
left(90)
pendown()
backward(50)
right(135)
forward(20)

done()


from turtle import *

shape("turtle")
colormode(255)

bgcolor("blue")
speed(3)

pencolor("red")
pensize(3)

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
left(180)
forward(50)

pendown()
right(30)
forward(50)
right(120)
forward(50)

penup()
left(120)
forward(130)

pencolor("yellow")
pendown()
circle(30)

penup()
left(90)
forward(30)

for i in range(8):
    penup()
    forward(30)
    pendown()
    forward(50)
    penup()
    backward(80)
    right(45)


done()





from turtle import *

shape("turtle")
colormode(255)

bgcolor("pink")
speed(3)

pencolor("red")
pensize(3)

for i in range(6):
    left(150)
    forward(30)
    left(30)
    forward(100)
    left(160)
    forward(100)
    left(30)
    forward(30)
    left(50)
done()



