# 1. What Would Python Display?

def mad(max):
    g = lambda: (print(1) or 2) or (print(3) or 4)
    print(max(5, 6))
    return g
print (mad(print)(), 7, print(8))

5 6
None 
1
8
2 7 None 


    # (a) What is the last line printed?
    2 7 None 
    # (b) Which of these whole lines appear somewhere in the printed output? Select all that apply
    1
    5 6
    8
    None 
    # (c) What order do 1, 6, and 8 appear in the printed output? 
    6 1 8 

# 2. Which One
    complete the environment diagram below and then answer the question that follow 
    there is one question for each labeled blanck in the diagram
    the blanks with no labels have no questions associated with them and are not scored

x, y, z = 1, 2, 3 

def switch(x):
    z = 4
    if x == y:
        def which(one):
            return x + one
    else:
        def which(one):
            return x - one
    x = which(x)
    which(x)

def which(one):
    return x * one

switch(x+1)
x = 5
which(z)

    f1: switch parent: global 
        x = 2
        z = 4
        which = which(one) [parent=f1]
        return value None 
    f2: which parent: f1
        one = 2
        return value = 4
    f3: which parent: f1
        one = 4
        return value = 8
    f4: which parent: global
        one = 3
        return value = 15 

# 3. Final Digit
    Implement final_digit, which takes a non-negative integer n
    As long as n has more than one digit, replace n with the sum of the digits of n
    This process repeats until n becomes a single-digit number, which is returned 

def final_digit(n):
    """Sum the digits of n repeatedly to reach one digit.
    >>> final_digit(321) # 3 + 2 + 1 = 6
    6
    >>> final_digit(987) # 9 + 8 + 7 = 24, and 2 + 4 = 6
    6
    >>> final_digit(989898989) # The digit sum is 77, 7 + 7 = 14, and 1 + 4 = 5
    5
    """
    while n >= 10:
        s = 0
        while n:
            n, s = n // 10, s + (n % 10) 
        n = s 
    return n

# 4. Close Enough
    Implement close, which takes two non-negative integers m and n. 
    It returns whether m can be changed into n by either inserting one digit, 
    removing one digit, or changing one digit.
    If m and n are the same number, they are not close.

def close(m, n):
    """Return whether m can result from starting with n and adding, removing,
    or changing one digit.
    >>> close(3756, 3456) and close(3456, 346) and close(346, 3456) and close(456, 56)
    True
    >>> close(5, 5) or close(3456, 3546) or close(3456, 36) or close(34, 3456) or close(345, 456)
    False
    """
    if m < n:
        m, n = n, m
    while m or n:
        if m % 10 = n % 10:
            m, n = m // 10, n // 10 
        else:
        return m // 10 == n // 10 or m // 10 == n # Hint: check here that just one change is enough
    return False
    
# 5. Shifty
    # (a) 
        Implement shift, which takes a number k and a one-argument function f
        It returns a one-argument function g that takes a number x
        For all numbers x, g(x) is equal to f(x + k)
        def shift(k, f):
            """Return a function of x that returns f(x+k).
            >>> square = lambda x: x * x
            >>> g = shift(2, square)
            >>> g(3) # square(3 + 2)
            25
            """
        return lambda x: f(x + k)

        # give an altenate solution
        # this time, your solution must call compose, and f may not be the operator of a call expression
        # in other words, you cannot write f( in your answer. you may not write [ or if
        
        def compose(f, g):
            """ Return a function that takes x and calls f on g of x """
            return lambda x: f(g(x))
        
        compose(f, lambda x: x + k)

        lambda f: lambda x: x + k 

    # (b) Implement sum_range, which takes positive integers p and q with p <= q, as well as a one-argument
    # function term. It returns the sum of the return values of term called on each consecutive integer starting
    # with p and ending with q (including both p and q). You may call shift, summation, and compose. Assume
    # shift is implemented correctly.

        def summation(n, term):
        """Sum the first n terms of a sequence: term(1) + term(2) + ... + term(n).
        >>> summation(5, lambda x: x*x) # 1*1 + 2*2 + 3*3 + 4*4 + 5*5
        55
        """
        total, k = 0, 1
        while k <= n:
        total, k = total + term(k), k + 1
        return total
        def sum_range(p, q, term):
        """Sum terms p through q of a sequence: term(p) + term(p+1) + ... + term(q).
        >>> sum_range(1, 5, lambda x: x*x) # 1*1 + 2*2 + 3*3 + 4*4 + 5*5
        55
        >>> sum_range(4, 5, lambda x: x*x) # 4*4 + 5*5
        41
        >>> sum_range(5, 5, lambda x: x*x) # 5*5
        25
        """
        assert p <= q
        return summation(q - p + 1, shift(p - 1, term))

        # (c) The shifter function below is a curried version of shift.
        # Implement unshift, which takes the result of shifter(k) for some number k. 
        # It returns a function that takes the result of shifter(k)(f) for some function f and 
        # returns a function equivalent to f. That is: f(x) == unshift(shifter(k))(shifter(k)(f))(x)
        # You can write your answer on multiple lines if it’s long. 
        # You can abbreviate lambda using the greek symbol lambda.
        # Your answer must be a call to shift. You may also call any of compose, summation, or sum_range.
        Hint: If you can compute k, then you can shift backward by k to undo the original shift.

            def shifter(k):
                def shifted(f):
                    return shift(k, f)
                return shifted

            def unshift(shifted):
                """Assume shifted is the return value of shifter(k) for some k.
                >>> cubic = lambda x: x*x*x - 5*x*x + 1
                # Some complicated function
                >>> cubic(2.0)
                -11.0
                >>> cubic(9.0)
                325.0
                >>> do = shifter(4)
                >>> do(cubic)(2.0)
                # same as cubic(6.0)
                37.0
                >>> do(cubic)(9.0)
                # same as cubic(13.0)
                1353.0
                >>> undo = unshift(do)
                >>> undo(do(cubic))(2.0) # same as cubic(2.0)
                -11.0
                >>> undo(do(cubic))(9.0) # same as cubic(9.0)
                325.0
                """
                return lambda g: _______

            # (i) Fill in the blank with a single call to shift.
                lambda g: shift(-shifted(lambda x: x)(0), g) 
                lambda g: shifter(-shifted(lambda x: x)(0))(g)