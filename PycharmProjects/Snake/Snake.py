class Snake:
    def __init__(self, x, y, xChange, yChange):
        self.x = x
        self.y = y
        self.xChange = xChange
        self.yChange = yChange

    def move_snake(self):
        self.x += self.xChange
        self.y += self.yChange

