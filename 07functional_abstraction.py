Lambda Function Environments
    A lambda function's parent is the current frame in which the lambda expression is evaluated

    a = 1
    def f(g):
        a = 2
        return lambda y: a * g(y) # this lambda has its parent as f frame 
    f(lambda y: a + y)(a) 
    # the lambda in this context has its parent as the global frame  

Return 
    Returning from a function call means ending the function call and 
    determining what is the value of the call expression

    A return statment completes the evaluation of a call expression and provides its value
        When you evaluate a call expression for a user-defined function, you have to execute the body of that function
        in a new environment, and you keep doing that until you reach a return statement, or you reach the end of the body

        f(x) for user-defined function f: switch to a new invironment; execute f's body
        return statement within f: switch back to the previous environment; f(x) now has a value 
    
    Only one return statement is ever executed while executing the body of a function 

    def end(n, d):
        """ print the final digits of N in reverse order until D is found
        >>> end(34567, 5)
        7
        6
        5
        """
        while n > 0:
            last, n = n % 10, n // 10 
            print(last)
            if d == last:
                return None # we return None as a way af ending the process of the while statemnet 

    def search(f): 
        x = 0 
        while True: # purposefully write infinity loop to find true value of f 
            if f(x): # if f(x) is true 
                return x
            x += 1 # else we add 1 to x 

    def is_three(x):
        return x == 1
    
    def square(x):
        x * x
    
    def positive(x):
        return max(0, square(x) - 100)
        
    def inverse(f):
        """ Return g(y) such that g(f(x)) -> x """
        return lambda y: serch(lambda x: f(x) == y) 

    >>> sqrt = inverse(square)

    # shorter version of search 
    def search(f):
        x = 0 
        while not f(x):
            x += 1
        return x 

Abstractions 

    Functional Abstractions
        functional abstraction is giving a name to some computational process and then 
        referring to that process as a whole without worrying about its implementation details

        def square(x):
            return mul(x, x)

        def sum_squares(x, y):
            return square(x) + square(y)
        
        what dose sum_squares need to know about square?
            square takes one argument Yes 
            square has the intrinsic name square No
            square computes the square of a number Yes
            square computes the square by calling mul No (ex. pow(x, 2) or mul(x, x - 1) + x)

    Choosing Names
        Names typically do not matter for correctness
        but they matter a lot for composition 

        Names should convey the meaning or purpose of the values to which they are bound 
        The type of value bound to the name is best documented in a function's docstring
        Function names typically convey their effect(print), their behavior(triple), or the value returned(abs)

        true_false -> rolled_a_one
        d -> dice
        play_helper -> take_turn
        my_int -> num_rolls
        l, I, 0 -> k, i, m 

    Which Values Deserve a Names

        Repeated compound expressions:
            if sqrt(square(a) + square(b)) > 1:
                x = x + sqrt(square(a) + square(b))
            
            hypotenuse = sqrt(square(a) + square(b))
            if hypothenuse > 1:
                x = x + hypotenuse 

        Meaningful parts of complex expressions:
            x = (-b + sqrt(square(b) - 4 * a * c)) / (2 * a)

            discriminant = sqrt(square(b) - 4 * a * c)
            x = (-b + discriminant) / (2 * a) 
        
        Names can be long if they help document your code:
            average_age = average(age, students)

            is preferable to 

            # Compute average age of students
            aa = avg(a, st) 

        Names can be short if they represent generic quantities:
        counts, arbitrary functions, arguments to mathematical operations, etc.

            n, k, i - usually integers
            x, y, z - usually real numbers
            f, g, h - usually functions 

Errors & Tracebacks
    Errors come in three forms 

    SyntaxError: Having expressions that are not formed well; the syntax of a language is its form  
    The kind that Python can detect before it even starts executing your program 

    RuntimeError: These are detected by the Python interpreter while your program is executing 
    When it occurs, you see a traceback, which is a report that describes what was going on in your program
    and what line to look at in order to fix the error 

    Logical or Behavioral Error: These would not be detected by Python at all; 
    the program runs, it just doing the wrong thing 
    The way to check for those is to write tests and 
    check to see that those tests correctly describe the behavior of your program

    def f(x):
        return g(x - 1)

    def g(y):
        return abs(h(y) - h(1 /* y)

    def h(z):
        z * z
    
    print(f(12)) 

    # we get syntax error 

    def f(x):
        return g(x - 1)

    def g(y):
        return abs(h(y) - h(1 / y))

    def h(z):
        z * z # h is returning none 
    
    print(f(12)) 

    # we get type error(type of runtime error)

    def f(x):
        return g(x - 1)

    def g(y):
        return abs(h(y) - h(1 / y))

    def h(z):
        return z * z 
    
    print(f(1)) 

    # we get division by zero error 