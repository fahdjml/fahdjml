print("****CIRCLE****")
import math
def circle_perimeter(radius):
return math.pi*radius*2
def circle_area(radius):
return math.pi*radius*radius
def main():
radius=float(input("Enter value for radius of circle :"))
area=circle_area(radius)
perimeter=circle_perimeter(radius)
area=round(area,4)
perimeter=round(perimeter,4)
print("The Area of circle is :",area)
print("The perimeter of cicle is :",perimeter)
main()
