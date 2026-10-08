import math

#1. Calculate The circle radius
def circle_area():
    radius = float(input("Enter circle radius? "))
    area = math.pi *(radius**2)
    print(f"Circle area = {area}")

#2. Converts Celsius into Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter the temperature in Celsius? "))
    fahrenheit = (celsius * 9/5) +32
    print(f"{celsius} (C)= {fahrenheit} (F)")

#3. Checks whether a number is prime or not
def check_prime():
    n=int(input("Enter the number? "))
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(f"{n} is a NOT prime number")
                return
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a NOT prime number")
#4. Checks whether a number is perfect or not.
def check_perfect():
    n=int(input("Enter a number? "))
    if n >0:
        sum_divisors=sum(i for i in range(1, n) if n % i ==0)
        if sum_divisors == n:
            print(f"{n} is a perfect number")
        else:
            print(f"{n} is a NOT perfect number")
    else:
        print(f"{n} is a NOT perfect number")

#5. Asks user for their favorite color and find its index
def find_color():
    colors = ["Red","Orange","Yellow","Green","Blue","Purple"]
    color_input =input("What is your favorite color? ")
    color_input = color_input.lower()
    if color_input in [color.lower() for color in colors]:
        index = [color.lower() for color in colors].index(color_input)
        print(f"Your color is at index {index} in my list")
    else:
        print("Sorry, I could not find your color")

#6. Using range() to create and print sequences
def print_sequences():
    range1 = list(range(7))  
    range2 = list(range(1, 11, 3)) 
    range3 = list(range(5, 0, -1))  
    range4 = list(range(6, -3, -2))  

    print("range1: ", range1)
    print("range2: ", range2)
    print("range3: ", range3)
    print("range4: ", range4)

#7. Function to remove the dollar sign in a string
def remove_dollar_sign(s):
    return s.replace('$', '')

#8. Function to extract even items in an integer list
def extract_even(l):
    return [x for x in l if x % 2 == 0]

#9. Function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Number must be a non-negative integer."
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

#10. Function to get all divisors of a number
def get_divisors(n):
    if n <= 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]

#11. Program to compute distance between two points
def calculate_distance():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance between points: {distance}")

#12. Function to print out an m x n pattern
def print_pattern(m, n):
    for i in range(m):
        print('* ' * n)