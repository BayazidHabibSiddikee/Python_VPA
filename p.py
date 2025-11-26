from turtle import *
import arrow, time
''' setup(600, 500, 100, 200) creates a window that is 600x500 pixels and positions its top-left corner 100 pixels right 
and 200 pixels down from the top-left corner of your monitor.'''
Screen()
setup(400,40,-200,-20)
tracer(False)
title("Simple watch in turtle module")
bgcolor('sky blue')
hideturtle()
while True:
    clear()
    current_time = arrow.now().format("hh:mm:ss A")
    #color('blue')
    #up()
    #goto(-280,50)
    #write('The current time is\n',font=('Arial',45,'normal'))
    color('black')
    up()
    goto(10,5)
    write(current_time,font=('Arial',20,'normal'))
    time.sleep(1)
    update()
done()
try:
    bye()
except:
    pass