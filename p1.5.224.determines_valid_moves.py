from turtle import *
import arrow, time
from tkinter import messagebox

# FIX 1: Move these to global scope so all functions can access them
cellcenter = {'7':(-200,-200),'8':(0,-200),'9':(200,-200),
              '4':(-200,0),'5':(0,0),'6':(200,0),
              '1':(-200,200),'2':(0,200),'3':(200,200)}  
turn = "blue"
rounds = 0
valid_moves = list(cellcenter.keys())
occupied_moves = {'blue':[], 'red':[]}

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
    update()

def time_up():
    while True:
        # FIX 2: Remove clear() - it erases the board!
        current_time = arrow.now().format('hh:mm:ss A')
        title(f"Tik Tak Toe - {current_time}")
        time.sleep(1)
        # FIX 3: Remove update() - not needed, title doesn't require it

def check_winner():
    win = False
    if '1' in occupied_moves[turn] and '2'in occupied_moves[turn] and '3' in occupied_moves[turn]:
        win = True
    if '4' in occupied_moves[turn] and '5'in occupied_moves[turn] and '6' in occupied_moves[turn]:
        win = True
    if '7' in occupied_moves[turn] and '8'in occupied_moves[turn] and '9' in occupied_moves[turn]:
        win = True
    if '1' in occupied_moves[turn] and '4'in occupied_moves[turn] and '7' in occupied_moves[turn]:
        win = True
    if '2' in occupied_moves[turn] and '5'in occupied_moves[turn] and '8' in occupied_moves[turn]:
        win = True
    if '3' in occupied_moves[turn] and '6'in occupied_moves[turn] and '9' in occupied_moves[turn]:
        win = True
    if '1' in occupied_moves[turn] and '5'in occupied_moves[turn] and '9' in occupied_moves[turn]:
        win = True
    if '3' in occupied_moves[turn] and '5'in occupied_moves[turn] and '7' in occupied_moves[turn]:
        win = True
    return win

def mark_cell(x,y):
    global turn, rounds, valid_moves
    if -300<x<300 and -300<y<300:
        col = int((x + 300) // 200) + 1
        row = int((y + 300) // 200) + 1
        cell = str((3 - row) * 3 + (col))
        print(f"Marking cell {cell} for {turn}")
    else:
        print("Click outside the board")
        return 
    if cell in valid_moves:
        rounds += 1
        up()
        goto(cellcenter[cell])
        dot(90,turn)
        update()
        occupied_moves[turn].append(cell)
        valid_moves.remove(cell)
        
        if check_winner():
            valid_moves=[]
            messagebox.showinfo("Game Over",f'congratulations {turn} wins!')
        elif rounds == 9:
            messagebox.showinfo("Game Over","It's a Tie!")
        
        if turn == "blue":
            turn = "red"
        else:
            turn = "blue"           
    else:
        messagebox.showerror("Invalid Move","Cell already occupied. Choose another cell.")

def main():
    Screen()
    setup(600,600,10,70)
    bgcolor("lightblue")
    tracer(False)
    hideturtle()
    pensize(5)
    color("red")
    # FIX 4: Remove local variable declarations - use globals instead
    draw_board()
    onscreenclick(mark_cell)
    listen()
    # FIX 5: Use mainloop() instead of done() for proper threading
    mainloop()

if __name__ == "__main__":
    import threading
    threading.Thread(target=time_up,args=(), daemon=True).start()   
    main()  # FIX 6: Call main() directly, not in a thread
    #threading.Thread(target=time_up,args=()).start()