# Types of Expressions
# An expression describes a computation and evaluates to a value
# f(x)

# Call Expressions in Python
# all expressions can use function call notation

from operator import add, mul
add(2, 3)
mul(2, 3)

mul(add(2, mul(4, 6)), add(3, 5))
# in call expressions, you don't need to memorize the order of operations
# just nesting structure of the expression itself tells you exactly what gets multiplied before it gets added

1 * 2 * ((3 * 4 * 5 // 6) ** 3) + 7 + 8
# when you use these infix operators between different values 
# you have to know that muliplication comes before addition in order to understand how the expression gets evaluated

# Anatomy of a Call Expression
# operator ( operand , operand )
# operators and operands are also expressions
# so they evaluate to values 

# Evaluation procedure for call expressions:
# 1. Evaluate the operator and then the operand subexpressions
# 2. Apply the function that is the value of the operator subexpression 
#    to the arguments that are the values of the operand subexpression

mul(add(2, mul(4, 6)), add(3, 5))

# mul add(2, mul(4, 6))
# add 2, mul(4, 6)
# mul 4, 6
# mul 26, add(3, 5)
# add 3, 5
# mul 26, 8 


 