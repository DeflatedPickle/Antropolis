from pathfinding.core.grid import Grid

class Map:
    def __init__(self):
        self.matrix = []
        for y in range(640 // 16):
            row = []
            for x in range(480 // 16):
                row.append(1)
            self.matrix.append(row)

        # TODO: Write a method to update the grid, and clean up the old one
        self.grid = Grid(matrix=self.matrix)
