import random

from OpenGL.GL import *
import vectormath as vmath

import action
import globals

class Wander(action.Action):
    directions = ["north", "south", "east", "west"]
    distance = 0.02

    def __init__(self, ant, *args):
        super().__init__(ant, *args)
        self.target = ant.position + vmath.Vector3(random.uniform(0, Wander.distance), random.uniform(0, Wander.distance), random.uniform(0, Wander.distance))

    def perform(self):
        if self.ant.position.all() == self.target.all():
            self.is_complete = True

        else:
            # TODO: Check if we're colliding, get out of there
            for i in globals.ant_list:
                if not i.does_fill():
                    pass

            # TODO: Figure out a path to where we're going

    def render(self):
        glBegin(GL_LINES)
        glVertex2f(self.ant.position.x, self.ant.position.y)
        glVertex2f(self.target.x, self.target.y)
        glEnd()
