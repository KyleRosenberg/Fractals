from turtle import right, left, forward, speed, exitonclick, hideturtle


def dragon(level=4, size=200, zig=right, zag=left):
    if level <= 0:
        forward(size)
        return

    size /= 1.3
    zig(45)
    dragon(level - 1, size, right, left)
    zag(90)
    dragon(level - 1, size, left, right)
    zig(45)


speed(0)
hideturtle()
dragon(12)
exitonclick()  # click to exit