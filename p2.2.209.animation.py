from turtle import *
import arrow, time 

#Set the screen
Screen()
setup(800,600,10,70)
tracer(False)
bgcolor('sky blue')
hideturtle()
#Put the screen in an infinite loop
while True:
    #Clear screen
    clear()
    current_time = arrow.now().format('hh:mm:ss A')
    color('blue')
    up()
    goto(-300,50)
    #Write the first line of text
    write('The current time is\n',font=('Arial',50,'normal'))
    color('red')
    goto(-300,-100)
    write(current_time,font=('Arial',80,'normal'))
    time.sleep(1)
    #Put everything on screen
    update()
done()
try:
    bye()
except Terminator:
    print('Exit')