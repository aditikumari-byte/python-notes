class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self, width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** (1/2)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture    

    def get_amount_inside(self, shape):
        width_times = self.width // shape.width
        height_times = self.height // shape.height
        return width_times * height_times

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def set_width(self,width):
        self.width = width
        self.height = width

    def set_height (self,height):
        self.height = height
        self.width = height

    def set_side(self,side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"        
