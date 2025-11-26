from turtle import *
Screen()
setup(600,600,10,70)
bgcolor("lightblue")
tracer(False)
hideturtle()
pensize(5)
color("red")

for i in (-100,100):
    up()
    goto(-100,-300)
    down()
    goto(-100,300)
    up()
    goto(100,-300)
    down()
    goto(100,300)
    up()
    goto(-300,-100)
    down()
    goto(300,-100)
    up()
    goto(-300,100)
    down()
    goto(300,100)
    up()
# create a dictionary to hold the positions
cell = {'1':(-200,-200),'2':(0,-200),'3':(200,-200),'4':(-200,0),'5':(0,0),'6':(200,0),
        '7':(-200,200),'8':(0,200),'9':(200,200)}        
# Go to the center of each cell
for c, center in list(cell.items()):
    goto(center)
    dot(90,"blue")
    write(c,align='center',font=('Arial',20,'italic'))
    
done()
try:
    bye()
except:
    pass