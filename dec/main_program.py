# main_program.py

# Selectively import the required functions
from pack_main.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from pack_main.circle import area as circle_area, perimeter as circle_perimeter
from pack_sub.cuboid import area as cuboid_area, volume as cuboid_volume
from pack_sub.sphere import area as sphere_area, volume as sphere_volume

# Rectangle example
length = 5
width = 3
print(f"Rectangle Area: {rectangle_area(length, width)}")
print(f"Rectangle Perimeter: {rectangle_perimeter(length, width)}")

# Circle example
radius = 4
print(f"Circle Area: {circle_area(radius)}")
print(f"Circle Perimeter: {circle_perimeter(radius)}")

# Cuboid example
height = 7
print(f"Cuboid Area: {cuboid_area(length, width, height)}")
print(f"Cuboid Volume: {cuboid_volume(length, width, height)}")

# Sphere example
print(f"Sphere Area: {sphere_area(radius)}")
print(f"Sphere Volume: {sphere_volume(radius)}")
