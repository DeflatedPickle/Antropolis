from collections import deque
import random

from OpenGL.GL import *
import vectormath as vmath

import action

class Ant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # self.position = vmath.Vector3(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        self.position = vmath.Vector3(0.48, 0.08, 0)
        self.size = vmath.Vector3(0.15, 0.15, 0.15)

        # self.action_default = wander.Wander
        self.action_queue = deque([], 6)
        self.action_cooldown = 0

    def __str__(self):
        return "Ant { " + f"name={self.name}, age={self.age}, position={self.position}, action_queue={self.action_queue}" + " }"

    def update(self, delta):
        if self.action_cooldown > 0:
            self.action_cooldown -= 1
        else:
            if len(self.action_queue) != 0:
                act = self.action_queue[0]
                if not act.is_complete:
                    act.perform()
                    act.render()
                else:
                    self.action_queue.popleft()
                    self.action_cooldown = 60

            else:
                self.action_queue.append(action.Wander(self))

    def render(self):
        # TODO: Replace with a shader
        glBegin(GL_POLYGON)
        glVertex2f(self.position.x, self.position.y)  # Bottom left
        glVertex2f(self.position.x + self.size.x, self.position.y)  # Bottom right
        glVertex2f(self.position.x + self.size.x, self.position.y + self.size.y)  # Top right
        glVertex2f(self.position.x, self.position.y + self.size.y)  # Top left
        glEnd()

    def does_fill(self):
        return True
