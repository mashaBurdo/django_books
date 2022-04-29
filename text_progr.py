import random
import turtle

t = turtle.Pen()


def square(step):
    for i in range(4):
        t.forward(step)
        t.right(90)


def go_to_random():
    t.up()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.down()


def generate_color():
    R = random.random()
    B = random.random()
    G = random.random()
    t.color(R, G, B)


t.speed(10)
for i in range(10):
    generate_color()
    square(random.randint(2, 100))
    go_to_random()

turtle.mainloop()