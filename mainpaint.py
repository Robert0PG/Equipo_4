"Este programa es un juego de dibujo, en donde puedes sibujar lineas y diversas figuras, así mismo se le puede cambiar el color"
"Autores: Roberto Peláez García A01732317"
from turtle import *

from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circl(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    circle(50)
    end_fill()


def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(300)
        left(90)
        forward(150)
        left(90)

    end_fill()


def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(300)
        left(120)

    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'),'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circl), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
