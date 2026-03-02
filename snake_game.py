import turtle
import time
import random

# Screen
screen = turtle.Screen()
screen.title("Realistic Snake Game")
screen.bgcolor("#0b1d0b")
screen.setup(width=800, height=800)
screen.tracer(0)

delay = 0.1
score = 0
high_score = 0

# Snake Head (oval shape)
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#1aff1a")
head.shapesize(stretch_wid=1.3, stretch_len=2.2)  # elongated head
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Eyes
left_eye = turtle.Turtle()
left_eye.hideturtle()
left_eye.shape("circle")
left_eye.color("black")
left_eye.shapesize(0.2, 0.2)
left_eye.penup()

right_eye = turtle.Turtle()
right_eye.hideturtle()
right_eye.shape("circle")
right_eye.color("black")
right_eye.shapesize(0.2, 0.2)
right_eye.penup()

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(0.8, 0.8)
food.penup()
food.goto(0, 100)

# Score
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 350)
pen.write("Score: 0  High Score: 0",
          align="center",
          font=("Arial", 18, "bold"))

# Game Over Text
game_text = turtle.Turtle()
game_text.hideturtle()
game_text.penup()
game_text.color("red")

segments = []

# Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 15)
    if head.direction == "down":
        head.sety(head.ycor() - 15)
    if head.direction == "left":
        head.setx(head.xcor() - 15)
    if head.direction == "right":
        head.setx(head.xcor() + 15)

# Keyboard
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

def reset_game():
    global score, delay

    time.sleep(1)

    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()

    game_text.goto(0, 0)
    game_text.write("GAME OVER",
                    align="center",
                    font=("Arial", 40, "bold"))
    time.sleep(2)
    game_text.clear()

    score = 0
    delay = 0.1

    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}",
              align="center",
              font=("Arial", 18, "bold"))

# Main Loop
while True:
    screen.update()

    # Update eyes position
    left_eye.goto(head.xcor() - 8, head.ycor() + 8)
    right_eye.goto(head.xcor() + 8, head.ycor() + 8)
    left_eye.showturtle()
    right_eye.showturtle()

    # Wall Collision
    if (head.xcor() > 380 or head.xcor() < -380 or
        head.ycor() > 380 or head.ycor() < -380):
        reset_game()

    # Food Collision
    if head.distance(food) < 20:
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("#00cc44")
        new_segment.shapesize(stretch_wid=1.2, stretch_len=2)
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        delay -= 0.002

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center",
                  font=("Arial", 18, "bold"))

    # Move Body Smoothly
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(),
                         segments[i-1].ycor())

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self Collision
    for segment in segments:
        if segment.distance(head) < 15:
            reset_game()

    time.sleep(delay)

screen.mainloop()