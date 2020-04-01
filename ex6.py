import turtle


def drawcurve(t, lon, o):
    if o == 0:
        t.forward(lon)
    else:
        drawcurve(t, 1/3*lon, o-1)
        t.left(60)
        drawcurve(t, 1/3*lon, o-1)
        t.right(120)
        drawcurve(t, 1/3*lon, o-1)
        t.left(60)
        drawcurve(t, 1/3*lon, o-1)


def drawfullcurve(t, lon, n):
    drawcurve(t, lon, n)
    t.right(120)
    drawcurve(t, lon, n)
    t.right(120)
    drawcurve(t, lon, n)


turtle.speed(0)  # histoire de dessiner un peu plus vite
turtle.setup(1200, 600)  # J'ai modifié les coordonnées pour voir le dessin entier.
drawfullcurve(turtle, 300, 5)
turtle.exitonclick()
