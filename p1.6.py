from turtle import *
from tkinter import messagebox
from mptpkg import print_say

class tik_tak_toe:
    def __init__(self):
        self.cellCenter = {'1':(-200,200),'2':(0,200),'3':(200,200),
                           '4':(-200,0),'5':(0,0),'6':(200,0),
                           '7':(-200,-200),'8':(0,-200),'9':(200,-200)}  
        self.turn = 'black'
        self.round = 0
        self.validMoves = list(self.cellCenter.keys())
        self.occupiedMoves = {'black':[],'red':[]}
        
    def draw_board(self):
        Screen()
        setup(600,600,10,70)
        tracer(False)
        title("Tik Tak Toe")
        bgcolor('light yellow')
        hideturtle()
        pensize(5)
        for i in (-100,100):
            up()
            goto(300,i)
            down()
            goto(-300,i)
            up()
            goto(i,-300)
            down()
            goto(i,300)
            up()
        for cell, center in list(self.cellCenter.items()):
            goto(center)
            write(cell, align='center',font=('Arial',30,'italic'))
    
    def position(self,x,y):
        if -300<x<300 and -300<y<300:
            col = int((x + 300) // 200) + 1
            row = int((y + 300) // 200) + 1
            cell = str((3 - row) * 3 + (col))
            print(f"Marking cell: {cell} for player: {self.turn}")
            #print_say(f'Cell number {cell}')
        else:
            print("Click outside the board")
            return None
        if cell in self.validMoves:
            self.round += 1
            self.validMoves.remove(cell)
            self.occupiedMoves[self.turn].append(cell)
            goto(self.cellCenter[cell])
            dot(120,self.turn)
            if self.winner():
                self.validMoves = []
                messagebox.showinfo("Game over",f'{self.turn} wins!')
            elif self.round == 9:
                messagebox.showinfo("Game Over",f"It's a Tie!")
            if self.turn == 'black':
                self.turn = 'red'
            else:
                self.turn = 'black'
        else:
            messagebox.showerror("Invalid Move","Cell already occupied. Choose another cell.")  
    
    def winner(self):
        win = False
        winning_combo = [[str(i) for i in range(1,4)],[str(i) for i in range(4,7)],[str(i) for i in range(7,10)],
                         ['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
        for combo in winning_combo:
            if all(i in self.occupiedMoves[self.turn] for i in combo):
            #if all(num in self.cellCenter.keys() and num in self.occupiedMoves[self.turn] for num in i):
                win = True
                break
        return win
    
    def main(self):
        self.draw_board()
        onscreenclick(self.position)
        done()
        try:
            bye()
        except:
            pass

if __name__ == "__main__":
    game = tik_tak_toe()
    game.main()