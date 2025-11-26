from turtle import *
Screen()
setup(810,710,10,70)

hideturtle()
tracer(False)

bgcolor('lightgreen')
pensize(5)
for i in range(-350,400,100):
    up()
    goto(i,-298)
    down()
    goto(i,303)
    up()
pensize(3)
color('gray')

for i in range(-300,400,101):
    up()
    goto(-350,i)
    down()
    goto(350,i)
    up()
done()
try:
    bye()
except Terminator:
    print('exit')
