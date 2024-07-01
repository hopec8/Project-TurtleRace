import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, or purple): ")
is_race_on = False
turtles = []

for turtle_index in range(0,6):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
