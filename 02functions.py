
# ctrl + L clears screen 

pi 
# NameError: name 'pi' is not defined
# Most names aren't available unless you import them

from math import pi

sin 
# Built-in functions 

Assignment Statements 

    The expression (right) is evaluated, and its value is assigned to the name (left).

radius = 10 
# Assignment makes you build your own 

area, circ = pi * radius * radius, 2 * pi * radius 
# you can do multiple assignments in one line

Defining Functions 

    Assignment is a simple means of abstraction: binds names to values
    Function definition is a more powerful means of abstraction: binds names to expressions

def <name>(<formal parameters>): 
    # The formal parameters part is called Function Signature, indicates how many arguments a function takes 
    return <return expression>
    # Function Body is everything that's indented after the first line, 
    # It defines what function does, the computational process expressed by a function

Execution procedure for def statements:
    1. Create a function with signature <name>(<formal parameters>)
    2. Set the body of that function to be everything indented after the first line
    3. Bind <name> to that function in the current frame 


Calling User-Defined Functions

    1. Add a local frame, forming a new environment
    2. Bind the function's formal parameters to its arguments in that frame
    3. Execute the body of the function in that new environment

from operator import mul 
def square(x):
    return mul(x, x) 
square(-2)
# In global frame we have mul, a built-in function, and squre, a user-defined function
# In local frame, a function squre is called
# It binds argument -2 to its formal variable x,
# and returns value 4 

# function signature has all the information needed to create a local frame

Looking Up Names In Environments

    Every expression is evaluated in the context of an environment. 
    # Environments are the memory that keeps track of the correspondence between names and values 
    So far, the current environment is either:
    • The global frame alone, or
    • A local frame, followed by the global frame.

    Most important two things I’ll say all day:
    An environment is a sequence of frames.
    A name evaluates to the value bound to that name in the earliest frame of the
    current environment in which that name is found.

    E.g., to look up some name in the body of the square function:
    • Look for that name in the local frame.
    • If not found, look for it in the global frame.
    (Built-in names like “max” are in the global frame too,
    but we don’t draw them in environment diagrams.)

from operator import mul
def square(square):
    return mul(square, square)
>>> square(-2)
# then in the local frame square binds to -2 and it doesn't go outside to the global frame
# hence it returns 
>>> 4 

Environment Diagrams 

    Environment diagrams are a way for us to keep track of 
    what's going on within the Python interpreter when it executes a program that we type in. 
    It visualizes the intepreter's process.

    Code: Statements and expressions 

    Frames: Each name is bound to a value 
            Within a frame, a name cannot be repeated 
# https://pythontutor.com/cp/composingprograms.html#mode=edit

Assignment Statements

    Execution rule for assignment statements:
        1. Evaluate all expressions to the right of = from left to right.
        2. Bind all names to the left of = to those resulting values in the current frame.

a = 1
b = 2
b, a = a + b, b 
>>> a, b = 2, 3 

# Discussion Question
f = min 
f = max 
g, h = min, max
max = g 
max(f(2, g(h(1,5), 3)), 4)
>>> ?

Print and None 

    Pure functions just return values and non-pure functions have side effects 
    print function is non-pure function whose return value is None but 
    displays its inputs 

    None indicates that nothing is returned 
         The special value None represents nothing in Python
         A function that does not explicitly return a value will return None
         Careful: None is not displayed by the interpreter as the value of an expression

def does_not_square(x):
    x * x 

does_not_square(4) 
# returns nothing because the function itself has no return and
# none value is not displayed 

sixteen = does_not_square(4)
sixteen + 4
>>> TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

print(print(1), print(2))
>>>
1
2
None None

