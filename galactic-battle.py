import turtle

wn = turtle.Screen()
wn.bgcolor("#0e202e")
wn.title("Galactic Battle")


# classes
class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color('#e1e5e6')
        self.speed = 1

    def move(self):
        self.forward(self.speed)


player = Player()

# main game loop
while True:
    player.move()