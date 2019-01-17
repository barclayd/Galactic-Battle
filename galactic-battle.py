import turtle

wn = turtle.Screen()
wn.bgcolor("#0e202e")
wn.bgpic("./img/space.gif")
wn.title("Galactic Battle")


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
        self.shape("triangle")
        self.color('#97a4a6')
        self.speed = 1

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


# sprites
# wn.register_shape("spaceship.gif")
player = Player()
border = Border()
# player.shape("spaceship.gif")

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
    player.move()
