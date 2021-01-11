class Figures:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self. width = width
        self.height = height

    def __str__(self):
        return f"Figures {self.x}, {self.y}, {self.width}, {self.height}"

fig_1 = Figures(5, 10, 50, 100)
print(str(fig_1))

print(type(fig_1))