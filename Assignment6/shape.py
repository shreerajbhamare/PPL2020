import turtle
import math
t = turtle.Turtle()
def turtle_screen():
    s = turtle.getscreen()
    
    turtle.title("My Turtle Program")
    t.pen(pensize=3, speed = 1)
    t.fillcolor("red")
    
class shape:
    def __init__(self, length = 0) :

        self.length = length


class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane,two-dimensional  with straight sides.")
        print("It has",self.no_sides,"sides")
        print("Lenght of each side ",self.length)
        area = 0.25*((self.length)**2) *self.no_sides*1/math.tan(math.pi/(self.no_sides))
        print("Area : ", area)
        print("Perimeter :",self.no_sides * self.length)
class square(polygon):
    def __init__(self, lenght, no_sides = 4) :
        super().__init__(lenght)
        self.no_sides = no_sides
    def show(self):
        for i in range(4):
           t.forward(self.length) 
           t.right(90) 
class pentagon(polygon):
    def __init__(self, lenght,no_sides = 5) :
        super().__init__(lenght)
        self.no_sides = no_sides
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 
           
class hexagon(polygon):
    def __init__(self,lenght, no_sides = 6) :
        super().__init__(lenght)
        self.no_sides = no_sides
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)
class octagon(polygon):
    def __init__(self, lenght, no_sides = 8) :
        super().__init__(lenght)
        self.no_sides = no_sides
    def show(self):
        for i in range(8):
           t.forward(self.length) 
           t.right(45)

class triangle(polygon):
    def __init__(self,lenght,  no_sides = 3) :
        super().__init__(lenght)
        self.no_sides = no_sides
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
turtle_screen()
print("*******Different Shapes**********")
print("Which shape do you want ?")
print("1 . Square")
print("2 . Pentagon")
print("3 . Hexagon")
print("4 . Octagon")
print("5 . Triangle")
choice = int(input("Enter Choice :"))
if(choice == 1) : 
    len = int(input("Enter side of square :"))
    
    s1 = square(len)
    s1.info()
    s1.show()
elif(choice == 2) :
    len = int(input("Enter side of pentagon :"))
    s2 = pentagon(len)
    s2.info()
    s2.show()
elif(choice == 3) :
    len = int(input("Enter side of Hexagon :"))
    s3 = hexagon(len)
    s3.info()
    s3.show()
elif(choice == 4) :
    len = int(input("Enter side of octagon:"))
    s4 = octagon(len)
    s4.info()
    s4.show()
else :
    len = int(input("Enter side for equilateral triangle :"))
    s5 = triangle(len)
    s5.info()
    s5.show()
turtle.done()