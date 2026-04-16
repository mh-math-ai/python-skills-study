"""
Q1: WWPD(What Would Python Display?)
"""

>>> True and 13
13
# <left> and <right> evaluates <left> and if it's false it returns <left> otherwise it evaluate <right> and returns <right>


>>> False or 0
0 
# <left> or <right> evaluates <left> and if it's true it returns <left> otherwise it evaluate <right> and returns <right>

>>> not 10
False
# anything other than 0, None, "" etc. are True 

>>> not None
True

>>> True and 1 / 0
ZeroDivisionError: division by zero
# evaluating 1 / 0 gets this error 

>>> True or 1 / 0
True 

>>> -1 and 1 > 0
True 

>>> -1 or 5
-1

>>> (1 + 1) and 1
1

>>> print(3) or ""
3
''
# "" gets evaluated by repr() 

>>> def f(x):
...     if x == 0:
...         return "zero"
...     elif x > 0:
...         return "positive"
...     else:
...         return ""
>>> 0 or f(1)
"positive"

>>> f(0) or f(-1)
"zero"

>>> f(0) and f(-1)
''

"""
Q2: Higer-Order Functions
"""

>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
beets
# Python only runs function print('beet') def is saved in the memory, it returns pie, so chocolate is now pie 

>>> chocolate
<function cake.<locals>.pie at ______>
# function name 

>>> chocolate()
sweets
'cake'
# chocolate is binded to pie() 

>>> more_chocolate, more_cake = chocolate(), cake
sweets

>>> more_chocolate
'cake'
# chocolate() returns 'cake', cake() returns pie, which is a function 

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
<function cake.<locals>.pie at _____>

>>> snake(10, 20)()
sweets
'cake'

>>> cake = 'cake'
>>> snake(10, 20)
30

"""
Q3: Lambda
"""

>>> lambda x: x  # A lambda expression with one parameter x
<function <lambda> at _____>

>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
5

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
3

>>> b = lambda x, y: lambda: x + y  # Lambdas can return other lambdas!
>>> c = b(8, 4)
>>> c
<function <lambda>.<locals>.<lambda> at _____>

>>> c()
12

>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
______

>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
TypeError 

>>> higher_order_lambda(g)(2)
4

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
3

>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambda
<function <lambda> at _____>

>>> one_thousand = print_lambda(1000)
1000

>>> one_thousand # What did the call to print_lambda return?

# print_lambda(1000) is value, which is None because print() returns None 

"""
Q4: Composite Identity Function
"""
Write a function that takes in two single-argument functions, f and g, and 
returns another function that has a single parameter x. 
The returned function should return True if f(g(x)) is equal to g(f(x)) and False otherwise. 
You can assume the output of g(x) is a valid input for f and vice versa.

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    def is_identity(x)
        return f(g(x)) == g(f(x))
    return is_identity 
    
