import turtle

wn = turtle.Screen()
wn.bgcolor("#0e202e")
wn.bgpic("./img/space.gif")
wn.title("Galactic Battle")
wn.tracer(0)


# classes
class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color('#97a4a6')
        self.speed = 1

    def move(self):
        self.forward(self.speed)

    def turn_left(self):
        self.left(90)

    def turn_right(self):
        self.right(90)

    def increase_speed(self):
        self.speed += 1

    def decrease_speed(self):
        if self.speed > 1:
            self.speed -= 1


# sprites
# wn.register_shape("spaceship.gif")
player = Player()
# player.shape("spaceship.gif")

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
