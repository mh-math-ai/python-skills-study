Environments Enable Higher-Order
    Environment diagrams exist in order to describe how higher order functions work 

    Higher-Order Function: A function that takes a function as an argument value or 
                           returns a function as a return value or both
    
    Our environment diagrams already handle the case of higher-order functions!
    The rules works even if we pass functions around instead of numbers

    def apply_twice(f, x):
        return f(f(x))
    
    def square(x):
        return x * x

    result = apply_twice(square, 2)

    Names can be Bounded to Functional Arguments

    applying a user-defined function:
    1. create a new frame
    2. bind formal parameters (f & x) to arguments
    3. execute the body: return f(f(x))

Environments for Nested Definitions

    def make_adder(n): # A function that returns a function 
        """ Return a function that takes one argument K and return K + N
        >>> add_three = make_adder(3) # the name add_three is bound to a function 
        >>> add_three(4)
        7
        """
        def adder(k): # a local def statement 
            return k + n # can refer to names in the enclosing function 
        return adder 

    add_three = make_adder(3)
    result  = add_three(4)

    global frame - fucntion make_adder - func make_adder(n) [parent=global]
                            add_three  - func adder(k) [parent=f1]

    f1: make_adder [parent=global] 
        n -bind-> 3 
        adder -bind-> adder(k) # local
        return -bind-> adder(3) # goes to global 

    f2: adder [paren=f1]
        k -bind-> 4
        return 7

Environment Diagrams for Nested Def Statements
    the current environment when we actually evaluate k plus n, starts with the adder frame 
    and then is followed by its parent, which is f1, followed by its parent, which is global frame 

    Every user-defined function has a parent frame (often global)
    The parent of a function is the frame in which it was defined
    Every local frame has a parent frame (often global)

How to Draw an Environment Diagrams

    When a function is defined:
        Create a function value: func <name>(<formal parameters>) [parent=<parent>]
        Its parent is the current frame.
            f1: make_adder func adder(k) [parent=f1]
        Bind <name> to the function value in the current frame
    
    When a function is called:
        1. Add a local frame, titled with the <name> of the function being called
        2. Copy the parent of the function to the local frame: [parent=<lavel>]
        3. Bind the <formal parameters> to the arguments in the local frame
        4. Execute the body of the function in the environment that starts with the local frame

Local Names

    Local Names are not Visible to Other (Non-Nested) Functions 

        def f(x, y):
            return g(x)
        def g(a):
            return a + y 

        result = f(1, 2)
        >>> "y" is not found 

        An environment is a sequence of frames.
        The environment created by calling a top-level function (no def within def) consists of
        one local frame, followed by the global frame 

Function Composition 

    def square(x):
        return x * x
    def triple(x):
        return 3 * x
    def compose1(f, g):
        def h(x):
            return f(g(x))
        return h

    compose1(square, make_adder(2))(3) 

    Draw diagram of this composed functions

Lambda Expressions
    Lambda expression allows you to make a function in an assignment expression 
    Lambda expression are not common in Python, but important in general 
    Lambda expression in Python cannot contain statements, and 
    so they are limited relative to their close cousin, the def statement 

    >>> x = 10
    >>> square = x * x # An expression: this one evaluates to a number 
    >>> square = lambda x: x * x # a function with formal parameter x that returns the values of "x * x"
    # there is no "return" keyword in lambda expression 
    # and expression must be single 

Lambda Expression Versus Def Statements
    Both create a function with the same domain, range, and behavior
    Both functions have as their parent the frame in which they were defined
    Both bind that function to the name square
    Only the def statement gives the function an intrinsic name 

Currying 
    transforming a multi-argument function into a single-argument, higher-order function 
    discovered by Moses Schonfinkel and re-discovered by Haskell Curry 

    Function Currying 
    Function currying is a way of manipulating functions

    def make_adder(n):
        return lambda k: n + k

    make_adder(2)(3)
    add(2, 3) 
    # the difference between them?
    # there's a general relationship between these functions 

    def curry2(f):
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g
    curry2 = lambda f: lambda x: lambda y: f(x, y)
