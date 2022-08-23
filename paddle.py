import turtle


class Paddle:
    def __init__(self, color, x, y):
        # Paddle
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)
        # Functions

    def paddle_up(self):
        y = self.paddle.ycor()
        y += 20
        self.setYCor(y)

    def paddle_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.setYCor(y)

    def getYCor(self):
        return self.paddle.ycor()

    def setYCor(self, y):
        self.paddle.sety(y)
