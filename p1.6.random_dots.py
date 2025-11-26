import turtle as t 
import random
t.Screen()
t.setup(600,500,100,200)
t.bgcolor('springgreen3')
t.title('Python graphiics')
color = ['red','blue','green','yellow','skyblue','lightgreen','black','white','chocolate']
for i in range(100):
    #t.up()
    t.goto(random.randint(-300,300),random.randint(-250,250))
    t.dot(random.randint(5,30),random.choice(color))
    
t.hideturtle()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')