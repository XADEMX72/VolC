import time

pi = 3.14159

# Print welcome message
print("Welcome to VolC | By XADEMX1")
time.sleep(1)

# Prompt user to choose a shape for calculation
shape = input("Choose a shape for calculation | (1) Cylinder | (2) Cone | (3) Sphere: ")

if shape == "1":
    # Calculate volume of a cylinder
    r = float(input("What is the radius: "))  # Prompt user for radius
    h = float(input("What is the height: "))  # Prompt user for height
    v = pi * (r ** 2) * h  # Calculate volume of cylinder
    v1 = round(v, 1)  # Round the volume to 1 decimal place
    print("The Volume of the Cylinder is:", v1)  # Print the result

elif shape == "2":
    # Calculate volume of a cone
    r = float(input("What is the radius: "))  # Prompt user for radius
    h = float(input("What is the height: "))  # Prompt user for height
    v = (pi * (r ** 2) * h) / 3  # Calculate volume of cone
    v1 = round(v, 1)  # Round the volume to 1 decimal place
    print("The Volume of the Cone is:", v1)  # Print the result

elif shape == "3":
    # Calculate volume of a sphere
    r = float(input("What is the radius: "))  # Prompt user for radius
    v = (4 / 3) * pi * (r ** 3)  # Calculate volume of sphere
    v1 = round(v, 1)  # Round the volume to 1 decimal place
    print("The Volume of Sphere is:", v1)  # Print the result

else:
    # Invalid choice
    print("Invalid Choice")
