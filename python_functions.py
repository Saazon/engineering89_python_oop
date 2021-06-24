# Let's create a function
# Syntax def is used to declare followed by name of the function():

# First iteration
def greeting():
    print("Welcome on board! Enjoy your trip!")


greeting()  # If we didn't call the function it would execute the code but with no output


# DRY - Don't repeat yourself by declaring functions and reusing code

# Second iteration
def greeting():
    return "Welcome on board! Enjoy your trip!"


print(greeting())


# Third iteration with user name as a string presented as argument/args
def greeting(name):
    return "Welcome on board " + name


print(greeting("Lena"))


# Create a function to prompt the user to enter their name and display the name back to the user with a greeting
def greeting(name):
    return "Welcome on board " + name


print(greeting(input("Enter your name: ")))


# Let's create a function with multiple args as an int
def add(num1, num2):
    return num1 + num2


print(add(9, 3))
# print(add(int(input("Insert your first number: ")), int(input("Insert your second number: "))))

def multiply(num1, num2):
    print("This function multiplpies 2 numbers") # This will get printed out
    return num1 * num2
    print(" this is required outcome of 2 numbers") # This comes after the `return` statement so will not execute


print(multiply(3, 3))