import queue

from OpenGL.GL import *
import vectormath as vmath

import wander

class Ant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.position = vmath.Vector3(0, 0, 0)
        self.size = vmath.Vector3(0.25, 0.25, 0.25)

        # self.action_default = wander.Wander
        self.action_queue = queue.Queue(6)
        self.action_cooldown = 0

    def __str__(self):
        return "Ant { " + f"name={self.name}, age={self.age}, position={self.position}, action_queue={self.action_queue}" + " }"

    def update(self, delta):
        if self.action_cooldown > 0:
            self.action_cooldown -= 1
        else:
            if not self.action_queue.empty():
                self.action_queue.get(False).perform(self)
                self.action_cooldown = 60

            else:
                self.action_queue.put(wander.Wander(), False)

    def render(self):
        # TODO: Replace with a shader
        glBegin(GL_POLYGON)
        glVertex2f(self.position.x, self.position.y)  # Bottom left
        glVertex2f(self.position.x + self.size.x, self.position.y)  # Bottom right
        glVertex2f(self.position.x + self.size.x, self.position.y + self.size.y)  # Top right
        glVertex2f(self.position.x, self.position.y + self.size.y)  # Top left
        glEnd()
