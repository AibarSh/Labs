#Lecture task: classes and objects

class My_shape:
    def __init__(self, colour = "transparent", is_filled = False):
        self.colour = colour
        self.is_filled = is_filled
    def __str__(self):
        return f"{self.colour}, {self.is_filled}"
    def getArea(self):
        return 0

class Circle(My_shape):
    def __init__(self, colour="transparent", is_filled=False, x_center = 0, y_center  = 0, radius = 0):
        super().__init__(colour, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    def __str__(self):
        return f"Shape: circle, {super().__str__()}, {self.x_center}, {self.y_center}, {self.radius}"
    def getArea(self):
        if self.is_filled == False: return "Area is not filled"
        else: return f"Circle area: {3.14 * pow(self.radius, 2)}"

cir = Circle("Red", True, 0, 0, 5)
print(cir)
print(cir.getArea())
print('-------------------------------------------------------------')

class Rectangle(My_shape):
    def __init__(self, colour="transparent", is_filled=False, x_top_left = 0, y_top_left = 0, length = 0, width = 0):
        super().__init__(colour, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width
    def __str__(self):
        return  f"Shape: rectangle, {super().__str__()}, {self.x_top_left}, {self.y_top_left}, {self.length}, {self.width}"
    def getArea(self):
        if self.is_filled == False: return "Area is not filled"
        else: return f"Rectangle area: {self.length * self.width}"

rec = Rectangle("Green", True, 10, 10, 5, 7)
print(rec)
print(rec.getArea())
# while True:
#     inp = input()
#     if inp == 'exit' or 'Exit': break
#     elif inp == "rec":
#         rec = Rectangle(input())
#     elif inp == "cir":
#         rec = Circle(input())
    
