Self-Reference
    An interesting consequence of the way environments work is that 
    a function can refer to its own name within its body

    def print_all(x):
        print(x)
        return print_all

    >>> print_all(1)(3)(5)
    1
    3
    5

    def print_sums(x):
        print(x)
        def next_sum(y):
            return print_sums(x + y)
        return next_sum 

    >>> print_sums(1)(3)(5)
    1
    4
    9

Recursive Functions 
    Definition: A function is called recursive if the body of that function calls itself, either directly or indirectly
    Implication: Executing the body of a recursive function may require applying that function again 

    Digit Sum 

        2 + 0 + 1 + 3 = 6
        
        If a number a is divisible by 9, then digit_sum(a) is also divisible by 9
        Useful for typo detection!

        A checksum digit is a function of all the other digits; It can be computed to detect typos

            1234 5678 9098 765'8'
            # a checksum digit is a function of all the other digits; it can be computed to detect typos  

            the problem with credit card numbers is that they are very long
            and humans type them in all the time, and humans are prone to error 
            so what exists in every credit card is called a checksum digit
            and the point of that is that if the checksum digit does not match the computation of all the other digits,
            that is an indication that the number was typed in wrong 
            #credit cards actually use the Luhn algorithm, which we will implement after digit_sum 

    Sum Digits Without a While Statement

        def split(n):
            """ Split positive n into all but its last digit and its last digit """
            return n // 10, n % 10

        def sum_digits(n):
            """ Return the sum of the digits of positive integer n """
            if n < 10:
                return n
            else:
                all_but_last, last = split(n)
                return sum_digits(all_but_last) + last 

    Anatomy of a Recursive Function 
        The def statement header is similar to other Functions
        Conditional statements check for base cases
        Base cases are evaluated without recursive calls
        Recursive cases are evaluated with recursive calls 
        
    Recursion in Environment Diagrams

        def fact(n):
            if n == 0:
                return 1
            else:
                return n * fact(n - 1)
        
        >>> fact(3)

        The same function fact is called multiple times
        Different frames keep track of the different arguments in each call
        What n evaluates to depends upon which is the current environment 
        Each call to fact solves a simpler problem than the last: 'smaller n' 

    Iteration vs Recursion 
        Iteration is a special case of recursion 

        Using while:
        def fact_iter(n):
            total, k = 1, 1
            while k <= n:
                total, k = total * k, k + 1
            return total 
        # n, total, k, fact_iter 
        
        Using recursion:
        def fact(n):
            if n == 0:
                return 1
            else:
                return n * fact(n-1)
        # n, fact 

    Verifying Recursive Functions 

        The Recursive Leap of Faith 

            def fact(n):
                if n == 0:
                    return 1
                else:
                    return n * fact(n-1)

        Is fact implemented correctly?
        1. Verify the base case 
        2. Treat fact as a functional abstraction!
        3. Assume that fact(n-1) is correct 
        4. Verify that fact(n) is correct, assuming that fact(n-1) correct 
    
Mutual Recursion 

    The Luhn Algorithm 
        Used to verify credit card numbers 
        1. From the rightmost digit, which is the check digit, moving left, double the value of every second digit;
        if product of this doubling operation is greater than 9 (e.g., 7 * 2 = 14), then sum the digits of the products
        (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5)
        2. Take the sum of all the digits 

        The Luhn sum of a valid credit card number is a multiple of 10 

    def split(n):
        """ Split positive n into all but its last digit and its last digit """
        return n // 10, n % 10

    def sum_digits(n):
        """ Return the sum of the digits of positive integer n """
        if n < 10:
            return n
        else:
            all_but_last, last = split(n)
            return sum_digits(all_but_last) + last 

    def luhn_sum(n):
        if n < 10:
            return n 
        else:
            all_but_last, last = split(n)
            return luhn_sum_double(all_but_last) + last 
        
    def luhn_sum_double(n):
        all_but_last, last = split(n)
        luhn_digit = sum_digits(2 * last)
        if n < 10:
            return luhn_digit
        else:
            return luhn_sum(all_but_last) + luhn_digit 

Recursion and Iteration 

    Converting Recursion to Iteration 
        can be tricky: Iteration is a special case of recursion 
        idea: Figure out what state must be maintained by the iterative function 

        def sum_digits(n):
            """ Return the sum of the digits of positive integer n """
            if n < 10:
                return n
            else:
                all_but_last, last = split(n)
                return sum_digits(all_but_last) + last 
        
        what gets passed into sum_digits in each recursive call and what gets returned?
        these are clues as to what we might need to give names to when we write an iterative version 
        # what gets passed in is what is left to sum(all_but_last), which we call n here as a formal parameter 
        # what gets returned is a partial sum(last), the sum of the digits so far 

        def sum_digits_iter(n):
            digit_sum = 0
            while n > 0:
                n, last = split(n) 
                digit_sum = digit_sum + last 
            return digit_sum 
        # it turns out that converting an iterative implementation using a while statement to recursion
        # is quite a bit more straightforward, precisely because iteration is a special case of recursion 

        More formulaic: Iteration is a special case of recursion 
        Idea: The state of an iteration can be passed as arguments 

        def sum_digits_iter(n):
            digit_sum = 0
            while n > 0:
                n, last = split(n) 
                digit_sum = digit_sum + last # updates via assignment become... 
            return digit_sum 
        
        def sum_digits_rec(n, digit_sum): # arguments to a recursive call 
            if n == 0:
                return digit_sum 
            else:
                n, last = split(n)  
                return sum_digits_rec(n, digit_sum + last)