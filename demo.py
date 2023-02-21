import graphics
from graphics import circle,rectangle
from graphics.threeDgraphics import cuboid,sphere
from graphics.circle import *

print("Area of a circle with radius 5 is : ",circle.area_circle(5))
print("Permeter of a circle with radius 5 is ",circle.perimeter_circle(5))

print("Area of a circle with radius 5 is : ",area_circle(5))

print("Area of a Rectangle with length and width 8 is : ",rectangle.area_rec(8,8))
print("Permeter of a Rectangle with length and width 8 is : ",rectangle.perimeter_rec(8,8))

print("Area of a  cuboid with length,width,height 10 is : ",cuboid.area_cuboid(10,10,10))
print("Permeter of a cuboid with length,width,height 10 is : ",cuboid.perimeter_cuboid(10,10,10))

print("Area of a sphere with radius 7 is : ",sphere.area_sphere(7))
print("Permeter of a sphere with radius 7 is ",sphere.perimeter_sphere(7))