from turtle import Turtle,Screen
import random
#
# #creating the turtles
# turtle = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# tam = Turtle(shape="turtle")
# tum = Turtle(shape="turtle")
# tem = Turtle(shape="turtle")
# tåm = Turtle(shape="turtle")

my_screen=Screen()
my_screen.setup(width=500, height=400)
user_bet=my_screen.textinput(title="Who is going to win?", prompt="Which turtle is going to win the race? Enter a color: ")
color=["red","blue","green","yellow","purple", "orange"]
y_position=[-80,-50,-20,10,40,70]
is_race_on=False

all_turtles=[]
for turtle_index in range(0,6):
    turtle=Turtle(shape="turtle")
    turtle.color(color[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have  won! The {winning_color} turtle is the winner")
            else:
                print(f"You have  lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


my_screen.exitonclick()
