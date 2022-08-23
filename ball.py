import turtle


class Ball:

    def __init__(self, color, size):
        # Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color(color)
        self.ball.shapesize(stretch_wid=size, stretch_len=size)
        self.ball.penup()
        self.ball.goto(0, 0)

        self.xSpeed = 0
        self.ySpeed = 0

    def getXSpeed(self):
        return self.xSpeed

    def setXSpeed(self, xSpeed):
        self.xSpeed = xSpeed

    def getYSpeed(self):
        return self.ySpeed

    def setYSpeed(self, ySpeed):
        self.ySpeed = ySpeed

    def moveBall(self):
        self.ball.setx(self.ball.xcor() + self.xSpeed)
        self.ball.sety(self.ball.ycor() + self.ySpeed)

    def getXCor(self):
        return self.ball.xcor()

    def setXCor(self, x):
        self.ball.setx(x)

    def getYCor(self):
        return self.ball.ycor()

    def setYCor(self, y):
        self.ball.sety(y)
