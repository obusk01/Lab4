# The Authors' are Olivia Busk and Katherine O'Roark
import turtle
jack=turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==3:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
