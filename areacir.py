import math

def area():
    length = int(input("Enter the length"))
    width = int(input("Enter the height"))
    area = length * width
    print("Square footage of home=" + str(area))
    

    
    
def Cir():
        PI = 3.14
        radius = float(input(' Please Enter the radius of a circle: '))
        diameter = 2 * radius
        circumference = 2 * PI * radius
        print("Circumference of a Circle = %.2f" %circumference)