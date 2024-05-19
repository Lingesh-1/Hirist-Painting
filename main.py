import turtle as t
import random as r

#aamai-Turtle
aamai=t.Turtle()
t.colormode(255)
aamai.speed("fastest")
aamai.penup()
aamai.hideturtle()
def rando_color():
    re=r.randint(0,255)
    b=r.randint(0,255)
    g=r.randint(0,255)
    ct=(re,b,g)
    return ct

aamai.setheading(225)
aamai.forward(300)
aamai.setheading(0)
nodo=100
for i in range(1,nodo+1):
    aamai.dot(20,rando_color())
    aamai.forward(50)
    if i%10==0:
        aamai.setheading(90)
        aamai.forward(50)
        aamai.setheading(180)
        aamai.forward(500)
        aamai.setheading(0)
        # # aamai.right(90)
        # # aamai.left(90)
        # # aamai.setheading(90)
        # aamai.left(90)
        # aamai.forward(50)
        # aamai.dot(20,rando_color())
    # else:
        
    # if nodo % 10==0:
    #     aamai.setheading(90)
    #     aamai.forward(50)
    #     aamai.setheading(180)
    #     aamai.forward(500)
    #     aamai.setheading(0)

myscr=t.Screen()
myscr.exitonclick()
