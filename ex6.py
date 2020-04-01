import turtle

def drawcurve(turtle, l, o):
    if o == 0:
        turtle.forward(l)
        # turtle.forward(l)
    else:
        drawcurve(turtle, 1/3*l, o-1)
        turtle.left(60)
        drawcurve(turtle, 1/3*l, o-1)
        turtle.right(120)
        drawcurve(turtle, 1/3*l, o-1)
        turtle.left(60)
        drawcurve(turtle, 1/3*l, o-1)


def drawfullcurve(turtle, l, n):
    drawcurve(turtle, l, n)
    turtle.right(120)
    drawcurve(turtle, l, n)
    turtle.right(120)
    drawcurve(turtle, l, n)




turtle.setup(1200, 600)  # J'ai modifié les coordonnées pour voir le dessin entier.
drawfullcurve(turtle, 300, 2)
turtle.exitonclick()