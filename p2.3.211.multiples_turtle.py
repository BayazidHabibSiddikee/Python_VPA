import turtle as t 
t.Screen()
t.setup(810,710,10,70)
t.tracer(False)
t.hideturtle()
t.bgcolor('light blue')
t.color('blue')
t.pensize(5)
t.up()
t.goto(-200,-100)
t.down()
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)

#Create second turtle
msg = t.Turtle()
msg.hideturtle()
msg.up()
msg.color('red')
msg.goto(-300,-200)
msg.write('This is written by the second turtle ',font=('Arial',30,'normal'))


t.update()
t.done()
try:
    t.bye()
except:
    pass