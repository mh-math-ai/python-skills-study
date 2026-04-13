Multiple Environments

    When Python executes a program, different expressions can be evaluated in different environemts.
    There can actually be multiple environments in the same environment diagram.

Life Cycle of a User-Defined Function

    Def statement: >>> def square( x ): # name(formal parameter):
                            return mul(x, x) # def statement/body(return statement that contains return expression) 
    What happens? 
    A new function is created! 
    Name bound to that function in the current frame 

    call expression: square(2+2) #operator(operand) 
    What happens?
    Operator & operands evaluated 
    function(value of operator) called on arguments(values of operands)

    Calling/Applying: 4 -> square(x): -> 16 # Argument goes into signature and returns value 
    What happens?
    A new frame is created!
    Parameters bound to arguments 
    Body is executed in that new environment 

Multiple Environments in One Diagram! 

    An environment is a sequence of frames.
     the global frame alone
     a local, then the global frame 

    Every expression is evaluated in the context of an environment.
    A name evaluates to the value bound to that name in the earliest frame of the current environment
    in which that name is bound.

from operator import mul
def square(x):
    return mul(x, x)
square(square(3))

global frame :  mul     func mul(...)
                square  func square(x) [parent=Global]

f1: square [parent=Global]
x -bind-> 3 
return value -> 9 

f2: square [parent=Global]
x -bind-> 9
return value -> 81 
# we have three environments here, one is the global frame, 
# the other is f1 and then global frame, and f2 and then global frame  

Names Have Different Meanings in Different Environmnets

    A call expression and the body of the function being called are evaluated in different environments

from operator import mul
def square(square):
    return mul(square, square)

square(4)
>>> 16
Why?

global frame :  mul     func mul(...)
                square  func square(x) [parent=Global]

f1: square [parent=Global]
square -bind-> 4 # we found square in this local frame which is the argument 4, we never check global frame
return value -> 16

f1: square [parent=Global]
square -bind-> 4
return value -> 16

'''
Miscellaneous Python Features 
'''

Operators 
# how +, and * works? 
# for now just think of them as being shorthand for calling built-in functions such as add and mul 

# but for division we have two, / and //
# for now think of them as calling built-in functions such as truediv, and floordiv

# and for %
# As for now we think of it as calling built-in function mod  

Multiple Return Values 
# just as you can assign multiple values to multiple names using one assignment statement, 
# you can return multiple values from a function 

def divide_exact(n, d):
    return n //d, n % d

>>> quotient, remainder = divide_exact(2013, 10)
>>> quotient
201
>>> reminder
3

'''
so far we used interactive python interpreter 
we can make source file <name>.py and call it in interactive mode
$ python3 -i <name>.py 
'''

Docstrings 
# when you write functions in a python source file, you don't typically just give them a name and a return statement.
# in addition you give some documentation about what they do. 

from operator import floordiv, mod

def divide_exact(n, d):
    """ Return the quotient and reminder of dividing N by D.
    
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

Doctests 
# whitin docstring, you have example interactive session, and you can simulate that session
# by typing python3 -m doctest <name>.py 
# if everything does what it's supposed to do, you'll see no output. 
# but if you want to see more output, you canb pass -v option, which will tell you everything that happened.  
# python3 -m doctest -v <name>.py 

Default Arguments 
# a default argument is not an assignment,
# it's instead a placeholder for a default value that you put after a formal parameter. 

def divide_exact(n, d=10): # it says if no argument put to bind d, then it'll bind 10 to d 
    """ Return the quotient and reminder of dividing N by D.
    
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

Control 
    
    What is Control?
        Thus far, when we call a user-defined function, we execute the body of the function 
        top-down, until we’ve reached the end of a function or we’ve hit a return statement. 
        However, many of the programs we write will not necessarily run in this order.
        What are some examples of certain functions we may write that may stop early or run out of order?


Conditional Statements 

    Conditional statements (often called "If" Statements) contain statements 
    that may or may not be evaluated. 

    Statements

        A statement is executed by the interpreter to perfom an abstraction
    
    Compound Statements

    # this whole things are statement(compound)
    <header>: # this block of statement with header called clause 
        <statement> # this set of statement called suite 
        <statement>
        ...
    <separating header>
        <statement>
        <statement>
        ...
    ...
    # the first header determinds a statement's type
    # the header of a clause "controls" the suite that follows 
    # def statements are compound statements 

    # a suite is a sequence of statements 
    # to "execute" a suite means to execute its sequence of statements, in order. 

    # Execution Rule for a Sequence of Statemnets: 
    # Execute the first statement
    # Unless directed otherwise, execute the rest 

def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else: 
        return x

# this statement contains three clauses, three headers, and three suites 
    
    Execution Rule for Conditional Statemnets: 
    1. Evaluate the header's expression.
    2. If it is a true value, 
       execute the suite and skip the remaining clauses. 
    
    Syntax Tips
    1. Always start with "if" clause.
    2. Zero or more "elif" clauses.
    3. Zero or one "else" clauses, always at the end. 

Boolean Contexts

    Read 1.5.4 

def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0: # boolean context 
        return -x
    elif x == 0: # boolean context 
        return 0
    else: 
        return x

    False values in python: False, 0, '', None (more to come)
    True values in python: Anything else (True)

Iteration

    While Statement

    While statements contain statements that are repeated as long as some condition is true.
    
        Important considerations:
            • How many separate names are needed and what do they mean?
            • The while condition must eventually become a false value for the statement to end
              (unless there is a return statement inside the while body).
            • Once the while condition is evaluated, the entire body is executed.


    i, total = 0, 0 # Names and their initial values
    while i < 3: # The while condition is evaluated before each iteration
        i = i + 1 # A name that appears in the while condition is changing
        total = total + 1 # Executed even when is set to 3

    >>> i
    3
    >>> total
    6

    Execution Rule for While Statements:
    1. Evaluate the header's expression. 
    2. If it is a true value, execute the (whole) suite, then return to step 1. 
