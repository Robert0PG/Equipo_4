"Programa que cuenta con una serpiente encargada de obtener su comida, si la serpiente se toca a si misma o choca en la pared se termina el juego"
"Autores: Roberto Peláez García A01732317, Santiago León Salinas A01734958, Christian Flores Alberto A01734997"
"Fecha: 29/10/2021"
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Funcion que cambia la direccion de la serpiente"
    aim.x = x
    aim.y = y


def inside(head):
    "Funcion que regresa si la cabeza de la serpiente se encuentra dentro del recuadro"
    return -200 < head.x < 190 and -200 < head.y < 190

colorbody=['blue','moccasin','black','green','purple']
"Lista de colores que pueden ser elegidos para el cuerpo de la serpiente"
color=random.choice(colorbody)
"Funcion que regresa un color random"
colorfood=['orange','cyan','gray','pink','gold']
"Lista de colores que pueden ser elegidos para la comida"
color2=random.choice(colorfood)
"Funcion que regresa un color random"


def move():
    "Funcion que mueve a la serpiente"
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9,color)

    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

"Setup inicial"
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
