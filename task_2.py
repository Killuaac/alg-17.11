class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def per(self, width, height):
        return width * height

    def pl(self, width, height):
        return (width ** 2) + (height ** 2)
