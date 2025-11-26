import arrow, time
from turtle import *

Screen()
setup(600,600,10,70) #,startx=0, starty=0)
bgcolor("lightblue")
tracer(False)
hideturtle()
pensize(5)
color("red")
def time_up():
    while True:
        clear()
        current_time = arrow.now().format('hh:mm:ss A')
        title(f"Tik Tak Toe - {current_time}")
        time.sleep(1)
        update()
def draw():
    for i in (-100,100):
        up()
        goto(i,-300)
        down()
        goto(i,300)
        up()
        goto(-300,i)
        down()
        goto(300,i)
        up() 
    #create a dictionary to hold the positions
    cellcenter = {'1':(-200,-200),'2':(0,-200),'3':(200,-200),'4':(-200,0),'5':(0,0),'6':(200,0),
                '7':(-200,200),'8':(0,200),'9':(200,200)}        
    #Go to the center of each cell
    for cell, center in list(cellcenter.items()):
        goto(center)
        write(cell,align='center',font=('Arial',20,'italic'))
        
import threading
threading.Thread(target=time_up,args=(),daemon=True).start()
threading.Thread(target=draw,args=(),daemon=True).start()
#mainloop()
done()   
try:
    bye()
except:
    pass
