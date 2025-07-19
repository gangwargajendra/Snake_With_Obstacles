from turtle import Turtle

OBSTACLE_POSITIONS = [(-180, -180), (-160, -180), (-140, -180), (-120, -180), (-120, -160), (-120, -140), (-120, -120), (120, -180), (120, -160), (120, -140), (120, -120), (120, -100), (120, -80), (120, -60), (120, -40), (-220, 120), (-200, 120), (-180, 120), (-160, 120), (-140, 120), (-120, 120), (-100, 120), (-80, 120), (-60, 120), (-40, 120), (100, 220), (100, 200), (100, 180), (100, 160), (100, 140), (100, 120), (120, 120), (140, 120), (160, 120), (180, 120)]

class Obstacle:

    def __init__(self):
        super().__init__()
        self.obstacle_list = []
        self.create_obstacle()


    def create_obstacle(self):
        for obstacle_index in range(0, len(OBSTACLE_POSITIONS)) :
            new_obstacle = Turtle()
            new_obstacle.penup()
            new_obstacle.color("#E3C4A8")
            new_obstacle.shape("square")
            new_obstacle.goto(OBSTACLE_POSITIONS[obstacle_index])
            self.obstacle_list.append(new_obstacle)