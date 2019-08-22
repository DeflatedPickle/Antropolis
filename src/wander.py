import random

import action

class Wander(action.Action):
    directions = ["north", "south", "east", "west"]

    def perform(self, ant):
        dir = random.choice(Wander.directions)

        if dir == "north":
            ant.position.y += 0.1
        elif dir == "south":
            ant.position.y -= 0.1
        elif dir == "east":
            ant.position.x += 0.1
        elif dir == "west":
            ant.position.x -= 0.1
