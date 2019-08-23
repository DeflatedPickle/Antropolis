import random

from OpenGL.GL import *
import vectormath as vmath
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

import action
import globals

class Wander(action.Action):
    directions = ["north", "south", "east", "west"]
    distance = 0.2

    def __init__(self, ant, *args):
        super().__init__(ant, *args)
        self.target = ant.position + vmath.Vector3(random.uniform(-Wander.distance, Wander.distance), random.uniform(-Wander.distance, Wander.distance), random.uniform(-Wander.distance, Wander.distance))

        globals.local_map.grid.cleanup()
        # TODO: Need a way to get the ants position and use it here
        node_start = globals.local_map.grid.node(0, 0)
        node_end = globals.local_map.grid.node(int(self.target.x.item() * 10),
                                               int(self.target.y.item() * 10))

        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        self.path, runs = finder.find_path(node_start, node_end, globals.local_map.grid)

        print('operations:', runs, 'path length:', len(self.path))
        print(globals.local_map.grid.grid_str(path=self.path, start=node_start, end=node_end))

    def perform(self):
        if len(self.path) > 0:
            step = self.path.pop()
            self.ant.position += vmath.Vector3(step[0] / 100, -step[1] / 100, 0)

        else:
            self.is_complete = True

    def render(self):
        glBegin(GL_LINES)
        glVertex2f(self.ant.position.x, self.ant.position.y)
        glVertex2f(self.target.x, self.target.y)
        glEnd()
