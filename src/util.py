from OpenGL.GL import *

def draw_grid(width, height):
    size = 16

    for y in range(height):
        y /= 100
        for x in range(width):
            x /= 100
            glBegin(GL_LINE_LOOP)
            glVertex2f(x - 1 + (x * size),        y - 1 + (y * size))  # Bottom left
            glVertex2f(x - 1 + size + (x * size), y - 1 + (y * size))  # Bottom right
            glVertex2f(x - 1 + size + (x * size), y - 1 + size + (y * size))  # Top right
            glVertex2f(x - 1 + (x * size),        y - 1 + size + (y * size))  # Top left
            glEnd()
