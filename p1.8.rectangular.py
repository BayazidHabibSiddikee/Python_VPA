from turtle import *
Screen()
setup(600,500,100,200)
bgcolor("sky blue")

title("Python turtle graphics to build rectangle")
hideturtle()
tracer(False)
pensize(6)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
update()
done()
try:
    bye()
except Terminator:
    print('exit')