import turtle

def draw_square(some_turtle):
    """

    :type some_turtle: turtle.Turtle()
    """
    for x in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.color('red')
    brad.speed(20)


    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('orange')
    angie.circle(100)
    boxes = range(90)
    for _ in boxes:

        draw_square(brad)
        brad.right(360/len(boxes))


    window.exitonclick()

draw_art()

import turtledemo
print(dir(turtledemo))