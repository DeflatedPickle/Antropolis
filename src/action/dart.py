
import random

import action

class Dart(action.Action):
    directions = ["north", "south", "east", "west"]
    increment = 0.01

    def perform(self):
        dir = random.choice(Dart.directions)

        if dir == "north":
            self.ant.position.y += Dart.increment
        elif dir == "south":
            self.ant.position.y -= Dart.increment
        elif dir == "east":
            self.ant.position.x += Dart.increment
        elif dir == "west":
            self.ant.position.x -= Dart.increment

        self.is_complete = True
