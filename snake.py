from turtle import Turtle


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.space = 0
        for x in range(3):
            tim = Turtle()
            tim.shape("square")
            tim.color("white")
            tim.penup()
            tim.goto(self.space, 0)
            self.space += 40
            self.turtle_list.append(tim)

    def extend(self):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        self.space = self.turtle_list[-1].position()
        # print(self.space[0])
        tim.goto(self.space)
        # self.space += 40
        self.turtle_list.append(tim)

    def turn_right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)

    def turn_left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)

    def turn_up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)

    def turn_down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)

    def move(self):
        coords = self.turtle_list[0].position()
        self.turtle_list[0].forward(20)

        #
        for mover in self.turtle_list[1:len(self.turtle_list)]:
            next_coords = mover.position()
            if mover == self.turtle_list[1]:
                now_coords = mover.position()
                mover.goto(coords[0], coords[1])
            else:
                mover.goto(now_coords[0], now_coords[1])
                now_coords = next_coords



        # if abs(coords[0]) == 270 or abs(coords[1]) == 270:
        #     alive = False
        #     return alive
        return True



