import turtle as t 
t.Screen()
t.setup(600,500,100,200)
t.bgcolor('lightgreen')
t.title("Python turtle graphics")
t.pensize(8)
#t.up()
t.goto(100,200)
t.up()
t.pencolor('blue')
t.pensize(10)
for i in range(7):
    t.goto(-200+50*i,-150)
    t.down()
    t.goto(-200+50*i+30,-150)
    t.up()
    
t.hideturtle()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')