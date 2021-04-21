class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width*self.height

if __name__ == '__main__':
    figure = Rectangle (12, 10)
    print(f"width: {figure.get_width()}, {figure.get_height()}, {figure.get_area()}")