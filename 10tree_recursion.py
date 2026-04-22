Orders of Recursive Calls 
    understanding orders of recursive calls is important for understanding the behavior of recursive functions 
    
    The Cascade Function 
        def cascade(n):
            if n < 10:
                print(n)
            else:
                print(n) 
                cascade(n//10)
                print(n)
        
        cascade(123) 

        global frame cascade func cascade(n) parent=global

        f1: cascade [parent=global]
            n 123
        f2: cascade [parent=global]
            n 12
        f3: cascade [parent=global]
            n 1
            return None 
        f2: cascade [parent=global] # each cascade frame is from a different call to cascade 
            n 12                    # until the return value appears, that call has not completed 
            return None 
        f1: cascade [parent=global]
            n 123
            return None 

    Two Definitions of Cascade 
        def cascade(n):
            print(n)
            if n > 10:
                cascade(n//10)
                print(n)

        if two implementations are equally clear, then shorter is usually better 
        in this case, the longer implementation is more clear (at least to me)
        when learing to write recursive functions, put the base cases first 
        both are recursive functions, even though only the first has typical structure 

    Example: Inverse Cascade 

        Inverse cascade 
            Write a function that prints an inverse cascade:
            def inverse_cascade(n):
                grow(n)
                print(n)
                shrink(n)

            def f_then_g(f, g, n):
                if n:
                    f(n)
                    g(n)

            grow = lambda n: f_then_g(grow, print, n // 10)
            shrink = lambda n: f_then_g(print, shrink, n // 10)

Tree Recursion
    Tree-shaped processes arise whenever executing 
    the body of a recursive function makes more than one call to that function 

    Fibonacci Sequence in Tree Structure 

        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n-2) + fib(n-1)

        The computational process of fib evolves into a tree structure 
        how can we illustrate this process?

        @trace # from 08function_examples.py 
        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n-2) + fib(n-1)
    
    Repetition in Tree-Recursive Computation 
        This preceess is highly repetitivel; fib is called on the same argument multiple times
        We can speed up this computation dramatically in a fee weeks by remembering results

    Example: Counting Partitions
        The number of partitions of a positive integer n, using parts up to size m, 
        is the number of ways in which n can be expressed as the sum of positive integer parts 
        up to m in increasing order

        count_partition(6, 4)
        2 + 4 = 6
        1 + 1 + 4 = 6
        3 + 3 = 6
        1 + 2 + 3 = 6
        1 + 1 + 1 + 3 = 6
        2 + 2 + 2 = 6
        1 + 1 + 2 + 2 = 6
        1 + 1 + 1 + 1 + 2 = 6
        1 + 1 + 1 + 1 + 1 + 1 = 6 

        Recursive decomposition: finding simpler instances of the problem 
        
        Explore two possibilities:
            Use at least one 4 
            Do not use any 4\
        Solve two simpler problems:
            count_partitions(2, 4)
            count_partitions(6, 3)
        
        Tree recursion often involoves exploring different choices 

        def count_partitions(n, m):
            if n == 0
                return 1
            elif n < 0:
                return 0 
            elif m == 0
                return 0
            else: 
                with_m = count_partitons(n-m, m)
                without_m = count_partition(n, m-1)
                return with_m + without_m           
        
        result = count_partitions(5, 3) 