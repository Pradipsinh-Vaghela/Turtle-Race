from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width = 1000, height = 500)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which Turtle will win the Race? Enter color :")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-150, -90, -30, 30, 90, 150]

turtles_list = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.turtlesize(2)
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-470, y=y_axis[turtle_index])
    turtles_list.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 430:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've Won!, The {winning_color} is the winner.")
            else:
                print(f"You've Lost!, The {winning_color} is the winner.")

        rand_distance = random.randint(10,30)
        turtle.forward(rand_distance)

screen.exitonclick()
