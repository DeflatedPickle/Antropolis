from OpenGL.GL import *
import vectormath as vmath

class Block:
    id = 0
    
    def __init__(self, x, y):
        self.position = vmath.Vector3(x, y, 0)
        self.size = vmath.Vector3(0.16, 0.16, 0.16)

    def update(self, delta):
        pass

    def render(self):
        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(self.position.x, self.position.y)  # Bottom left
        glVertex2f(self.position.x + self.size.x, self.position.y)  # Bottom right
        glVertex2f(self.position.x + self.size.x, self.position.y + self.size.y)  # Top right
        glVertex2f(self.position.x, self.position.y + self.size.y)  # Top left
        glEnd()
        glColor3f(0, 0, 0)

    def does_fill(self):
        return True
