class Action:
    def __init__(self, ant, *args):
        self.ant = ant
        self.is_complete = False

    def perform(self):
        pass

    def render(self):
        pass
