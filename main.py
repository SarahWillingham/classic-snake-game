from turtle import Screen
from snake_class import Snake
from food import Food
from score_board import ScoreBoard
from tkinter import messagebox
import time


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
scoreboard = ScoreBoard()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    if snake.get_size() < 8:
        time.sleep(0.18)
    elif 8 <= snake.get_size() < 12:
        time.sleep(.16)
    elif 12 <= snake.get_size() < 15:
        time.sleep(.14)
    elif 15 <= snake.get_size() < 19:
        time.sleep(.12)
    else:
        time.sleep(.10)
    snake.direction_changed = False
    snake.move()

    #Detect if finds food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        print(snake.get_size())
        scoreboard.increase_score()

    #Detect run into wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -400 or snake.head.ycor()  > 300 or snake.head.ycor() < -290:
        messagebox.showinfo("Game over","Sorry, you lost!")
        scoreboard.reset()
        snake.reset()

    #Detect collission with tail
    for segment in snake.snake_pieces[3:]:
        if snake.head.distance(segment) < 5:
            messagebox.showinfo("Sorry, you lost!")
            scoreboard.reset()
            snake.reset()

screen.exitonclick()