# Python OOP
In python, object oriented programming is based on the four pillars:
- Functions and good practices of functions

## Functions
Let's create a function

Syntax: `def` is used to declare followed by name of the `function()`:
```python
def greeting():
    print("Welcome on board! Enjoy your trip!")

    
greeting() # If we didn't call the function it would execute the code but with no output
```
The key to functions is **DRY**:
- Don't
- Repeat
- Yourself

If you need to do the same thing in a program multiple times, just use functions and call it when you need them!

The `return` statement is used to signal the last thing a function will give to us before ending:
```python
def greeting():
    return "Welcome on board! Enjoy your trip!"


print(greeting())
```
So even though the output is the same as the first iteration above, the method of printing to the screen is different. `return` is very useful for passing data out of a function without printing it out to the screen. You can also discard stuff you don't need this way too

So let's start passing arguments (`args`) into the function so we can make it more personal to the user:
```python
def greeting(name):
    return "Welcome on board " + name


print(greeting("Lena")) # = "Welcome on board Lena"
```
We can even get creative and ask the user for their name:
```python
def greeting(name):
    return "Welcome on board " + name


print(greeting(input("Enter your name: ")))
```
Let's create a funtion with multiple args as an int:
```python
def add(num1, num2):
    return num1 + num2


print(add(9, 3)) # = 12
```
```python
def multiply(num1, num2):
    print("This function multiplpies 2 numbers") # This will get printed out
    return num1 * num2
    print(" this is required outcome of 2 numbers") # This comes after the `return` statement so will not execute


print(multiply(3, 3))
```
This means that all of the things you want done have to occur between `def` and `return`