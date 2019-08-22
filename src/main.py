import time

import glfw
from OpenGL.GL import *

import ant

if __name__ == "__main__":
    if not glfw.init():
        print("Failed to load GLFW")

    window = glfw.create_window(640, 480, "Antropolis", None, None)
    if not window:
        glfw.terminate()

    glfw.make_context_current(window)

    ant_list = []
    # Make some default ants
    for k, v in {"ant 1" : 1, "ant 2" : 2}.items():
        ant_list.append(ant.Ant(k, v))


    glViewport(0, 0, 640, 480)
    glShadeModel(GL_SMOOTH)

    glColor3f(0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.25, 0.25, 0.25, 0)

        curr_time = time.time()
        for i in ant_list:
            print(i)
            new_time = time.time()
            i.update(curr_time - new_time)
            curr_time = new_time

            i.render()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
