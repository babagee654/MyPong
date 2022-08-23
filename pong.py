import paddle
import ball
import winsound
import turtle
import random
import math
import pathlib
path = pathlib.Path().resolve()


wn = turtle.Screen()
wn.title("Pong by Jerome")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Prevent window from updating,


# Sounds
bounce1 = "{}\\sounds\\bounce1.wav".format(path)
bounce2 = "{}\\sounds\\bounce2.wav".format(path)
bounce3 = "{}\\sounds\\bounce3.wav".format(path)
bounceSounds = [bounce1, bounce2, bounce3]

# Paddle 1
paddle1 = paddle.Paddle("blue", -350, 0)

# Paddle 2
paddle2 = paddle.Paddle("red", 350, 0)


# Ball
gameBall = ball.Ball("white", 1)


# Scoring
p1_score = 0
p2_score = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {}                                    Player 2: {}".format(
    p1_score, p2_score), align="center", font=("Comic Sans MS", 20, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 60)
pen2.write("Press spacebar to play", align="center",
           font=("Comic Sans MS", 20, "normal"))


def updateScore():
    pen.clear()
    pen.write("Player 1: {}                                    Player 2: {}".format(
        p1_score, p2_score), align="center", font=("Comic Sans MS", 20, "normal"))


def resetBall():
    pen2.write("Press spacebar to play", align="center",
               font=("Comic Sans MS", 20, "normal"))
    gameBall.setXCor(0)
    gameBall.setYCor(0)
    gameBall.setXSpeed(0)
    gameBall.setYSpeed(0)


def startGame():
    pen2.clear()
    if gameBall.getXSpeed() == 0:
        randX = math.floor(random.randint(0, 1))
        randY = math.floor(random.randint(0, 1))

        if randX == 0:
            gameBall.setXSpeed(-0.15)
        else:
            gameBall.setXSpeed(0.15)

        if randY == 0:
            gameBall.setYSpeed(-0.15)
        else:
            gameBall.setYSpeed(0.15)


def playCollisionSound():
    rand = math.floor(random.randint(0, 2))
    winsound.PlaySound(bounceSounds[rand], winsound.SND_ASYNC)


# Keybinds
wn.listen()
wn.onkeypress(paddle1.paddle_up, "w")
wn.onkeypress(paddle1.paddle_down, "s")

wn.onkeypress(paddle2.paddle_up, "Up")
wn.onkeypress(paddle2.paddle_down, "Down")

wn.onkeypress(startGame, "space")

# Main Game Loop
while True:
    wn.update()

    # Move ball
    gameBall.moveBall()

    # Top Borders
    if gameBall.getYCor() > 290:
        gameBall.setYCor(290)
        gameBall.setYSpeed(gameBall.getYSpeed() * -1)
        playCollisionSound()

    if gameBall.getYCor() < -290:
        gameBall.setYCor(-290)
        gameBall.setYSpeed(gameBall.getYSpeed() * -1)
        playCollisionSound()

    if paddle1.getYCor() > 250:
        paddle1.setYCor(250)
    if paddle2.getYCor() > 250:
        paddle2.setYCor(250)

    if paddle1.getYCor() < -250:
        paddle1.setYCor(-250)
    if paddle2.getYCor() < -250:
        paddle2.setYCor(-250)

    # Player 1 score
    if gameBall.getXCor() > 390:
        resetBall()
        p1_score += 1
        updateScore()

    # Player 2 score
    if gameBall.getXCor() < -390:
        resetBall()
        p2_score += 1
        updateScore()

    # Paddle + ball collision
    if (gameBall.getXCor() > 340 and gameBall.getXCor() < 350) and (gameBall.getYCor() < paddle2.getYCor() + 50 and gameBall.getYCor() > paddle2.getYCor() - 50):
        gameBall.setXCor(340)
        gameBall.setXSpeed(gameBall.getXSpeed() * -1.15)
        playCollisionSound()

    if (gameBall.getXCor() < -340 and gameBall.getXCor() > -350) and (gameBall.getYCor() < paddle1.getYCor() + 50 and gameBall.getYCor() > paddle1.getYCor() - 50):
        gameBall.setXCor(-340)
        gameBall.setXSpeed(gameBall.getXSpeed() * -1.15)
        playCollisionSound()
