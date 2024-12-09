import graphics
from graphics.rectangle import area as rect_area,perimeter as rect_perimeter
from graphics.circle import area as circ_area,perimeter as circ_perimeter
from graphics.three_d_graphics.cuboid import cuboid_area,cuboid_volume
from graphics.three_d_graphics.sphere import *
length=float(input("Enter length of rectangle:"))
width=float(input("Enter width of rectangle:"))
print("Rectangle Area:","{:.2f}".format(rect_area(length,width)))
print("Rectangle Perimeter:","{:.2f}".format(rect_perimeter(length,width)))
radius=float(input("Enter radius of circle:"))
print("Circle Area:","{:.2f}".format(circ_area(radius)))
print("Circle Perimeter:","{:.2f}".format(circ_perimeter(radius)))
l=float(input("Enter length of Cuboid:"))
w=float(input("Enter width of Cuboid:"))
h=float(input("Enter height of Cuboid:"))
print("Cuboid Surface Area:","{:.2f}".format(cuboid_area(l,w,h)))
print("Cuboid Volume:","{:.2f}".format(cuboid_volume(l,w,h)))
r=float(input("Enter radius of sphere:"))
print("sphere Surface Area:","{:.2f}".format(area(r)))
print("sphere volume:","{:.2f}".format(volume(r)))
