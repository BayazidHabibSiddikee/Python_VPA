from turtle import *
Screen()
setup(600,600,10,70) #,startx=0, starty
bgcolor("lightblue")
tracer(False)
hideturtle()
pensize(5)
color("red")    
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
    #create a dictionary to hold the positions
    cellcenter = {'7':(-200,-200),'8':(0,-200),'9':(200,-200),
                  '4':(-200,0),'5':(0,0),'6':(200,0),
                '1':(-200,200),'2':(0,200),'3':(200,200)}        
    #Go to the center of each cell
    for cell, center in list(cellcenter.items()):
        goto(center)
        write(cell,align='center',font=('Arial',20,'italic'))
draw_board()

'''
def click_handler(x,y):
    print(f"Mouse clicked at x={x}, y={y}")
    col = int((x + 300) // 200) + 1
    row = int((y + 300) // 200) + 1
    if 1 <= col <= 3 and 1 <= row <= 3:
        cell_number = (3 - row) * 3 + col
        print(f"Cell clicked: {cell_number}")
    else:
        print("Click outside the board")
onscreenclick(click_handler)'''


def get_xy(x,y):
    print(f'(x,y)=({x},{y})')
    
def cell_number(x,y):
    if -300<x<300 and -300<y<300:
        col = int((x + 300) // 200) + 1 # x + 300 to make it positive 0 to 600 and //200 to get the column
        row = int((y + 300) // 200) + 1 # +1 for the range 1 to 3
        print(f"Column number is {col}, Row number is {row}")
        cell = (3 - row) * 3 + (col)
        print(f"Cell number is {cell}")
onscreenclick(get_xy)
onscreenclick(cell_number)
listen()

done()   
try:
    bye()   
except:
    pass