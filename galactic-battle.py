import turtle
import random

wn = turtle.Screen()
wn.bgcolor("#000")
wn.bgpic("./img/space.gif")
wn.title("Galactic Battle")
wn.tracer(0)


# classes
class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.setposition(-300, -300)
        self.pendown()
        self.setposition(-300, 300)
        self.setposition(300, 300)
        self.setposition(300, -300)
        self.setposition(-300, -300)


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color('#97a4a6')
        self.speed = 1
        self.shapesize(2, 2, 0)

    def move(self):
        self.forward(self.speed)

        # border checking
        if self.xcor() > 275 or self.xcor() < -275:
            self.left(60)
        if self.ycor() > 275 or self.ycor() < -275:
            self.left(60)

    def turn_left(self):
        self.left(30)

    def turn_right(self):
        self.right(30)

    def increase_speed(self):
        self.speed += 1

    def decrease_speed(self):
        if self.speed > 1:
            self.speed -= 1

    def collision_check(self, target):
        global score
        if self.distance(target) < 20:
            score += 1
            print("Player score: ", score)
            goal.move_goal()


class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("#ffbb7b")
        self.speed = 3
        self.shape("circle")
        self.setposition(random.randint(-260, 260), random.randint(-260, 260))
        self.setheading(random.randint(0, 360))
        self.shapesize(1.15, 1.15)

    def move(self):
        self.forward(self.speed)

        # border checking
        if self.xcor() > 275 or self.xcor() < -275:
            self.left(60)
        if self.ycor() > 275 or self.ycor() < -275:
            self.left(60)

    def move_goal(self):
        self.setposition(random.randint(-260, 260), random.randint(-260, 260))
        self.setheading(random.randint(0, 360))


# class instances
player = Player()
border = Border()

# multiple goals
goals = []
for count in range(6):
    goals.append(Goal())

# draw border
border.draw_border()

# scoring
score = 0

# key bindings
wn.listen()
wn.onkeypress(player.turn_left, "Left")
wn.onkeypress(player.turn_right, "Right")
wn.onkeypress(player.increase_speed, "Up")
wn.onkeypress(player.decrease_speed, "Down")

# main game loop
while True:
    wn.update()
    player.move()
    for goal in goals:
        goal.move()
        # check for collision between player and goal
        player.collision_check(goal)


