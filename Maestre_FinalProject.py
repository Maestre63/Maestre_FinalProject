import turtle


def draw_pixel(t, x, y, color, size):
    t.penup()
    t.goto(x * size, y * size)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def draw_pacman():
    turtle.setup(500, 500)
    t = turtle.Turtle()
    t.speed(0)
    turtle.bgcolor('black')
    t.hideturtle()

    pixel_size = 20
    pacman_color = 'yellow'
    background_color = 'black'

    # Define a 15x15 grid for Pac-Man
    pacman_pixels = [
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    ]

    for y in range(len(pacman_pixels)):
        for x in range(len(pacman_pixels[y])):
            if pacman_pixels[y][x] == 1:
                draw_pixel(t, x - len(pacman_pixels[y]) // 2, len(pacman_pixels) // 2 - y, pacman_color, pixel_size)
            else:
                draw_pixel(t, x - len(pacman_pixels[y]) // 2, len(pacman_pixels) // 2 - y, background_color, pixel_size)

                turtle.done()


draw_pacman()
