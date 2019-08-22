import queue

import vectormath as vmath

class Ant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.position = vmath.Vector3(0, 0, 0)

        self.action_queue = queue.Queue(6)

    def __str__(self):
        return "Ant { " + f"name={self.name}, age={self.age}, position={self.position}, action_queue={self.action_queue}" + " }"

    def update(self, delta):
        # TODO: Wait an abitrary amount of time, then process the oldest action
        pass
