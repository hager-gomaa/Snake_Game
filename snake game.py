
import turtle
import random
import time

screen = turtle.Screen()
screen.setup(700,700)
screen.bgcolor("black") #("#1d1d1d")
screen.title("SNAKE GAME")
screen.tracer(0)

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

score =0;
delay=0.1

snake= turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction= 'stop'

food= turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(30,30)
old_food=[]

scoring= turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("score:",align="center",font=("courier",24,"bold"))

def snake_go_up():
  if snake.direction != "down":
    snake.direction = "up"

def snake_go_down():
  if snake.direction != "up":
    snake.direction = "down"

def snake_go_left():
  if snake.direction != "right":
    snake.direction = "left"

def snake_go_right():
  if snake.direction != "left":
    snake.direction = "right"

def move () :
  if snake.direction == "up":
    y = snake.ycor()
    snake.sety(y +20)
  if snake.direction == "down":
    y = snake.ycor()
    snake.sety(y -20)
  if snake.direction == "left":
    x = snake.xcor()
    snake.setx(x -20)
  if snake.direction == "right":
    x = snake.xcor()
    snake.setx(x +20)

screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")


def reset_game():
    global score, delay

    time.sleep(1)
    snake.goto(0, 0)
    snake.direction = "stop"

    for segment in old_food:
        segment.goto(1000, 1000) 

    old_food.clear()

    food.goto(30, 30)

    score = 0
    delay = 0.1
    scoring.clear()
    scoring.goto(0,300)
    scoring.write("score:{}".format(score), align="center", font=("courier",24,"bold"))


while True:
  screen.update()

  if snake.distance(food) < 20:
    x = random.randint(-290,270)
    y = random.randint(-240,240)
    food.goto(x,y)
    scoring.clear()
    score +=1
    scoring.write("score:{}".format(score),align="center",font=("courier",24,"bold"))
    delay -=0.001

    new_food = turtle.Turtle()
    new_food.speed(0)
    new_food.shape("square")
    new_food.color("red")
    new_food.penup()
    old_food.append(new_food)

  for index in range(len(old_food)-1,0,-1):
    a = old_food[index-1].xcor()
    b = old_food[index-1].ycor()
    old_food[index].goto(a,b)

  if len(old_food)>0:
    a= snake.xcor()
    b= snake.ycor()
    old_food[0].goto(a,b)
  
  move()

  if snake.xcor()>288 or snake.xcor()<-300 or snake.ycor()>238 or snake.ycor()<-240:
     time.sleep(1) 
     screen.clear() 
     screen.bgcolor("blue") 
     scoring.goto(0,0) 
     scoring.write("Game Over \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
    

  for foods in old_food:
    if foods.distance(snake) < 20:
      time.sleep(1) 
      screen.clear() 
      screen.bgcolor("blue") 
      scoring.goto(0,0) 
      scoring.write("Game Over \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
    

  time.sleep(delay)

turtle.Terminator()