class Entity:
    def __init__(self, x, y, xChange, yChange, score):
        self.x = x
        self.y = y
        self.xChange = xChange
        self.yChange = yChange
        self.score = score

    def move(self):
        self.x += self.xChange
        self.y += self.yChange

    def checkEdge(self):
        if self.y < 0:
            self.y = 0
        if self.y > 476:
            self.y = 476
