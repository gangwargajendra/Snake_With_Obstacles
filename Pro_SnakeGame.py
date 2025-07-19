from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from obstacle import Obstacle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)  # controls the drawing updates of the screen
screen.bgcolor("black")  # to make backGround black
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right , key="Right")

obstacle = Obstacle()


game_is_on = True
while game_is_on :
    screen.update() # screen will update
    time.sleep(0.1) # after every 0.1 sec, screen will refresh

    snake.move()

    # detect food is not overlap with obstacles
    for obstacle_segment in obstacle.obstacle_list:
        if food.position == obstacle_segment.position :
            food.refresh()

    # detect collision with obstacles
    for obstacle_segment in obstacle.obstacle_list:
        if snake.head.distance(obstacle_segment) < 10 :
            game_is_on = False
            scoreboard.game_over()

    # detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segment_list:
        if segment == snake.head :
            pass
        elif snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()









screen.exitonclick()