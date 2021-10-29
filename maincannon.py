#Este programa es un juego de destreza, pone a prueba la punteria impactando objetivos con proyectiles
#Autores: Roberto Peláez García A01732317, Santiago León Salinas A01734958, Christian Flores Alberto A01734997
#Fecha: 29/10/2021
from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    #Respuesta al click en la pantalla
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15


def inside(xy):
    #Devuelve True si xy está dentro de la pantalla
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    #Se crean los objetivos y la pelota
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    #Movimiento de la pelota y los objetivos
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 50)

#Setup del juego
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
Logo

Free Python Games


Donate
If you or your organization uses Free Games, consider donating:

Donate to Free Python Games

Related Topics
Documentation overview
Previous: Simon Says
Next: Bounce
Quick search
