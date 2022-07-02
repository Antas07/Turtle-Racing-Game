from turtle import Turtle, Screen
import random
screen = Screen()
is_RaceOn = False
screen.setup(width=500, height=400)
user_choice = screen.textinput(title='Make Your Bet', prompt= "Which turtle will win the race? Enter a color: ")
colors = ['red', 'green', 'yellow', 'orange', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []
for i in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])
    all_turtles.append(tim)
if user_choice:
    is_RaceOn = True
while is_RaceOn:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_RaceOn = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You have Won!The winning color {winning_color}")
            else:
                print(f"You have lost!The winning color {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.mainloop()