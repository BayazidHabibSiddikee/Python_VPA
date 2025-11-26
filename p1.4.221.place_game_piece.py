from turtle import *
Screen()
setup(600,600,10,70) #,startx=0, starty
bgcolor("lightblue")
tracer(False)
hideturtle()
pensize(5)
color("red")
cellcenter = {'7':(-200,-200),'8':(0,-200),'9':(200,-200),
                  '4':(-200,0),'5':(0,0),'6':(200,0),
                '1':(-200,200),'2':(0,200),'3':(200,200)}  
def draw_board():
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
    #Go to the center of each cell
    for cell, center in list(cellcenter.items()):
        goto(center)
        write(cell,align='center',font=('Arial',20,'italic'))
draw_board()

turn = "blue"
def mark_cell(x,y):
    global turn
    if -300<x<300 and -300<y<300:
        col = int((x + 300) // 200) + 1
        row = int((y + 300) // 200) + 1
        cell = (3 - row) * 3 + (col)
        print(f"Marking cell {cell} for {turn}")
    else:
        print("Click outside the board")
    up()
    goto(cellcenter[str(cell)])
    dot(90,turn)
    if turn == "blue":
        turn = "red"
    else:
        turn = "blue"
onscreenclick(mark_cell)
listen()
done()
try:
    bye()   
except:
    pass
    