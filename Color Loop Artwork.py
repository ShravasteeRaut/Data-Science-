
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colour Loop Artwork")

board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]

for i in range(70):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 3)
    board.right(91)

board.penup()
board.goto(0, -50)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()

for i in range(5):
    board.forward(110)
    board.right(144)

board.end_fill()

def petal():
    for j in range(2):
        board.circle(50, 60)
        board.left(120)

board.penup()
board.goto(0, 0)
board.pendown()

petal_colors = ["cyan", "lime", "violet", "orange", "pink"]

for i in range(24):
    board.color(petal_colors[i % len(petal_colors)])
    board.begin_fill()
    petal()
    board.end_fill()
    board.right(15)

turtle.done()


