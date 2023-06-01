import time

pi = 3.14159

print("Welcome to VolC | By XADEMX1")
time.sleep(1)

shape = input("Choose a shape for calculation | (1) Cylinder | (2) Cone | (3) Sphere: ")

if shape == "1":
    r = float(input("What is the radius: "))
    h = float(input("What is the height: "))
    v = pi * (r ** 2) * h
    print("The Volume of the Cylinder is", v)

elif shape == "2":
    r = float(input("What is the radius: "))
    h = float(input("What is the height: "))
    v = (pi * (r ** 2) * h) / 3
    print("The Volume of the Cone is:", v)

elif shape == "3":
    r = float(input("What is the radius: "))
    v = (4 / 3) * pi * (r ** 3)
    print("The Volume of Sphere is:", v)

else:
    print("Invalid Choice")
