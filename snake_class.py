from turtle import Turtle
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
STARTING_POSITIONS = [(-20,0),(0,0),(20,0)]

class Snake:

    def __init__(self):
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]
        self.direction_changed = False

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        snake1 = Turtle(shape="square")
        snake1.color("white")
        snake1.penup()
        snake1.goto(position)
        self.snake_pieces.append(snake1)

    def reset(self):
        for piece in self.snake_pieces:
            piece.goto(1000,1000)
        self.snake_pieces.clear()
        self.create_snake()
        self.head = self.snake_pieces[0]

    def extend(self):
        self.add_segment(self.snake_pieces[-1].position())

    def move(self):
        for segment_num in range(len(self.snake_pieces) - 1, 0, -1):
            new_x = self.snake_pieces[segment_num - 1].xcor()
            new_y = self.snake_pieces[segment_num - 1].ycor()
            self.snake_pieces[segment_num].goto(new_x, new_y)
        self.snake_pieces[0].forward(20)

    def up(self):
        if not self.direction_changed and round(self.head.heading()) != DOWN:
            self.head.setheading(UP)
            self.direction_changed = True

    def down(self):
        if not self.direction_changed and round(self.head.heading()) != UP:
            self.head.setheading(DOWN)
            self.direction_changed = True

    def left(self):
        if not self.direction_changed and round(self.head.heading()) != RIGHT:
            self.head.setheading(LEFT)
            self.direction_changed = True

    def right(self):
        if not self.direction_changed and round(self.head.heading()) != LEFT:
            self.head.setheading(RIGHT)
            self.direction_changed = True

    def get_size(self):
        return len(self.snake_pieces)