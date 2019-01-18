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


class Game(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.setposition(-290, 310)
        self.score = 0
        self.lives = 3

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="center", font=("Verdana", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

    def update_lives(self):
        self.clear()
        self.write("Score: {}".format(self.lives), False, align="center", font="Verdana")

    def change_lives(self):
        self.lives -= 1
        self.update_lives()


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

    def goal_collision_check(self, target):
        if self.distance(target) < 20:
            goal.move_goal()
            game.change_score(1)

    def asteroid_collision_check(self, target):
        if self.distance(target) < 20:
            asteroid.move_goal()
            game.change_score(-5)


class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("#ffbb7b")
        self.speed = 6
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


class Asteroid(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("#5f4e43")
        self.speed = 6
        self.shape("square")
        self.setposition(random.randint(-260, 260), random.randint(-260, 260))
        self.setheading(random.randint(0, 360))
        self.shapesize(2, 2)

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
game = Game()


# multiple goals
goals = []
for count in range(6):
    goals.append(Goal())

asteroids = []
for count in range(4):
    asteroids.append(Asteroid())

# draw border
border.draw_border()

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
        player.goal_collision_check(goal)
    for asteroid in asteroids:
        asteroid.move()
        # check for collision between player and goal
        player.asteroid_collision_check(asteroid)


