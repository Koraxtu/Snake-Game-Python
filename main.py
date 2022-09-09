from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

alive = True
while alive:
    # for tuttle in turtle_list:
    #     tuttle.forward(5)
    time.sleep(0.1)
    alive = snake.move()
    score.writer()
    screen.update()

    # Detect collision with food
    if snake.turtle_list[0].distance(food) < 15:
        # destroy the food, create a new food
        food.refresh()
        score.score += 1
        snake.extend()
    # Detect collision with wall
    if abs(snake.turtle_list[0].xcor()) > 280 or abs(snake.turtle_list[0].ycor()) > 280:
        alive = False
        score.reset()
    # Detect collission with tail
    for eats_self in snake.turtle_list[1:len(snake.turtle_list)]:
        if snake.turtle_list[0].distance(eats_self) < 10:
            alive = False
            score.reset()

screen.exitonclick()
