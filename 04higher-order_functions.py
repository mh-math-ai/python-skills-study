The Fibonacci Sequence
    Starts with 0, and 1, and then every element after that is the sum of the previous two elements
    Fibonacci did not invented this sequence; it was discussed and described by mathematicians long before him
    However, he made it popular in the West and so we still refer to him 
    Every Fibonacci numbers is associated with its index, the position in Fibonacci sequence
    0 is usually called 0th Fibonacci number since it is zero; it is a convention

    The Golden Spiral can be made by tiling squares together whose side lengths are Fibonacci numbers 
    A spiral going through the intersection points of these squares ever expanding and 
    it looks particularly well-balanced to human eye; it is also a spiral people like to look for in nature 

    def fib(n):
        """ Compute the nth Fibinacci number, for n >= 1 """
        pred, curr = 0, 1 # 0th and 1st Fibonacci numbers
        k = 1 # curr is the kth Fibonacci number
        while k < n:
            pred, curr = curr, pred + curr # the nex Fibonacci number is the sum of the current one and its predecessor
            k = k + 1
        return curr 
    
    # when designing an iterative function, one of the most important thing to think about is 
    # what information we need to track of in order to perform the iteration 

    What if the body of this function changed to this?
    
    pred, curr = 1, 0 
    k = 0 

    Is this alternative definition of fib the same or different from the original fib? 
    # it is correct implementation of fib for every n greater or equal to 1, 
    # even better because it can compute the 0th Fibonacci number correctly

Control 
    Control statements, such as if and while are different from functions in that 
    they control which parts of the code get executed and how many times 

    But maybe we can have the same control just using functions

    If Statements and Call Expressions
        Let us try to write a function that does the same thing as an if statement.
            if ___:
                ____ 
            else:
                ____ 
        
        Execution Rule for Conditional Statements:
            Each clause is considered in order
            1. Evaluate the header's expression (if present)
            2. If it is a true value (or an else header), 
               execute the suite & skip the remaining clause
        
        We can consider writing as this 
        def if_(c, t, f): # c is header for if, t is if suite, and f else suite 
            if c:
                return t
            else: 
                return f 

        However, call expression has its evaluation Rule
        Evaluation Rule for Call Expressions:
            1. Evaluate the operator and then the operand subexpressions
            2. Apply the function that is the value of the operator 
               to the arguments that are the values of the operands 

        In what case might we see a difference between using an if statement and using an if-call expression?

        from math import sqrt
        def real_sqrt(x):
            """ Return the real part of the square root of x """
            if x >= 0:
                return sqrt(x)
            else:
                return 0
        
        Think about changing the function body as this 

        def real_sqrt(x):
            return if_(x >= 0, sqrt(x), 0)

Control Expressions
    Some expressions allow the Python interpreter to skip evaluating some sub-expressions

    Logical Operators
    The logical operators AND and OR exhibit a behavior called short-circuiting 

    To evaluate the expression <left> AND <right>:
        1. Evaluate the subexpression <left>
        2. If the result is a false value v, then the expression evaluates to v
        3. Otherwise, the expression evaluates to the value of the subexpression <right>

    To evaluate the expression <left> OR <right>:
        1. Evaluate the subexpression <left>
        2. if the result is a true value v, then the expression evaluates to value
        3. Otherwise, the expression evaluates to the value of the subexpression <right>

    Why is this useful?
    
    from math import sqrt
    def has_big_sqrt(x):
        return x > 0 and sqrt(x) > 10 
    >>> has_big_sqrt(-1000)

    def reasonable(n):
        return n == 0 or 1/n != 0
    >>> reasonable(0)
    >>> reasonable(10 *** 1000)

Higher-Order functions
    A feature of a programming language that allow us to design functions as we should,
    by expressing very general methods of computation 

    Generalizing Patterns with arguments
        ex: Regular geometric shapes related length and area 
        
        the area of square = 1 * r^2
        the area of circle = pi * r^2
        the area of hexagon = (3 * sqrt(3)) / 2 * r^2 

        Finding common structure allows for shared implementation 

        """ Generalization """
        def area_square(r):
            return r * r
        def area_circle(r):
            return r * r * print
        def area_hexagon(r):
            return r * r * 3 * sqrt(3) / 2

        >>> area_hexagon(-10) 
        # it computes values the same as area_hexagon(10), which is not quite right 

        assert <expression>, <print>
        it evaluate <expression> and if it is false it prints <print>

        def area_square(r):
            assert r > 0, 'A length must be positive'
            return r * r
        def area_circle(r):
            assert r > 0, 'A length must be positive'
            return r * r * print
        def area_hexagon(r):
            assert r > 0, 'A length must be positive'
            return r * r * 3 * sqrt(3) / 2
        
        This repeats itself a lot 
        we can use higher-order function 

        def area(r, shape_constant):
            assert r > 0, 'A length must be positive'
            return r * r * shape_constant

        def area_square(r):
            return area(r, 1) 
        def area_circle(r):
            return area(r, pi)
        def area_hexagon(r):
            return area(r, 3 * sqrt(3) / 2)

    Generalizing Over Computational Process
        The common structure among functions may be a computational process, rather than a number

        def sum_naturals(n):
            """ Sum the first N natural numbers
            >>> sum_naturals(5)
            15
            """
            total, k = 0, 1
            while k <= n:
                total, k = total + k, k + 1
            return total

        def sum_cubes(n):
            """ Sum the first N cubes of natural numbers
            >>> sum_cubes(5)
            225
            """
            total, k = 0, 1
            while k <= n:
                total, k = total + pow(k, 3), k + 1
            return total

        def pi_sum(n):
            total, k = 0, 1
            while k <= n:
                total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
            return total

        from operator import mul

        def identity(k):
            return k
        def cube(k):
            return pow(k, 3)
        def pi_term(k):
            return 8 / mul(4 * k - 3, 4 * k - 1)

        def summation(n, term):
            """ Sum the first N terms of a sequence.
            >>> summation(5, cube)
            225
            """
            total, k = 0, 1
            while k <= n:
                total, k = total + term(k), k + 1
            return total 

        now we can write 

        def sum_naturals(n):
            return summation(n, identity)
        def sum_cubes(n):
            return summation(n, cube)
        def pi_sum(n):
            return summation(n, pi_term)

        Functions as Return Values 
            an example of this is below 

            def make_adder(n):
                """ Return a function that takes one argument K and return K + N
                >>> add_three = make_adder(3)
                >>> add_three(4)
                7
                """
                def adder(k):
                    return k + n
                return adder 

            Locally Defined Functions
                Functions defined within other function bodies are bound to names in a local frame 

                def make_adder(n): # A function that returns a function 
                    """ Return a function that takes one argument K and return K + N
                    >>> add_three = make_adder(3) # the name add_three is bound to a function 
                    >>> add_three(4)
                    7
                    """
                    def adder(k): # a local def statement 
                        return k + n # can refer to names in the enclosing function 
                    return adder 
                
                make_adder(1) (   2   ) 
                   operator    operand

            The Purpose of Higher-Order Functions
                Functions are fist-class: Function can be manipualated as values in our programming language
                Higher-order function: A function that takes a function as an argument value or returns a function as a return value 

                Higher-order functions:
                    express general methodes of computation 
                    remove repetition from programming
                    separate concerns among functions 