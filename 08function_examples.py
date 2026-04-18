What Would Python Print?
    The print function returns None 
    It also displays its arguments(separated by spaces) when it is called 

        from operator import add, mul
        def square(x):
            return mul(x, x)

        # expression -> evaluation -> interactive output 
        5 -> 5 -> 5
        print(5) -> None -> 5
        print(print(5)) -> None -> 5 None 

        def delay(arg):
            print('delayed')
            def g():
                return arg
            return g 
        
        delay(delay)()(6)() -> 6 -> delayed delayed 6
        print(delay(print)()(4)) -> None -> delayed 4 None 

        from operator import add, mul
        def square(x):
            return mul(x, x)

        def pirate(arggg):
            print('matey')
            def plunder(arggg):
                return arggg
            return plunder 

        add(pirate(3)(square)(4), 1) -> 17 -> matey 17
        # A name evaluates to the value bound to the name 
        # in the earliest frame of the current environment in which that name is found
        # in particular, the name arg will always evaluate to the value bound to it in the plunder frame
        # whatever plunder is called, we get back whatever it's called on 

        pirate(pirate(pirate))(5)(7) -> Error -> matey matey Error
        # pirate(3) returns plunder which didn't take 3 but pirate(pirate(pirate)) is plunder and it took 5
        # so we have 5(7) which gives us an Error 

        def horse(mask):
            horse = mask
            def mask(horse):
                return horse
            return horse(mask)

            mask = lambda horse: horse(2)
            horse(mask)

Implementing Functions 

    def remove(n, digit):
        """ Return all digits of non-negative N
            that are not DIGIT, for some
            non-negative DIGIT less than 10
        
        >>> remove(231, 3)
        21
        >>> remove(243132, 2)
        4313
        """
        kept, digits = 0, 0

        while n > 0
            n, last = n // 10, n % 10
            if last != digit:
                kept = kept + last * 10 ** digits
                digits += 1 
        return kept 

    # Read the description 
    # Verify the examples & pick a simple one
    # Read the template
    # Implement without the template, then change your implementation to match the template
    # OR If the template is helpful, use it 
    # Annotate names with values from your chosen example
    # Write code to compute the result
    # Did you really return the right thing?
    # check your solution with the other examples

Decorators

    Function Decorators

        @trace examples 

        def trace1(fn):
            """ Returns a version of fn that first prints before it is called 
            fn - a function of 1 argument
            """
            def traced(x):
                print('Calling', fn, 'on argument', x)
                return fn(x)
            return traced 

        @trace1 
        def square(x):
            return x * x
        
        @trace1
        def sum_squares_up_to(n):
            k = 1
            total = 0
            while k <= n:
                total, k = total + square(k), k + 1
            return total 

        # having decorator on top of a function's definition works as fn = trace1(fn) 
        # i. e. 

            @trace1
            def triple(x):
                return 3 * x

            is identical to

            def triple(x):
                return 3 * x
            triple = trace1(triple)

            