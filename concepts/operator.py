# 산술연산자 Arithmetic Operator: +, -, *, /, %, **, //

print(1+1)
print(3-2)
print(5*2)
print(6/3)
print(2**3) # 제곱
print(5%3) # 나머지 구하기
print(10%3)
print(5//3) # 몫 구하기
print(10//3)

# 비교연산자 Comparison Operator: >, >=, <, <=
print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

# == 같음 also Assignment Operator
print(3 == 3) # 같음
print(4 == 2)
print(3 + 4 == 7)

# 논리 연산자 Logical Operator: and, or, not
print(1 != 3) # 같지 않음
print(not (1 != 3)) # 같지 않음의 반대는 같음
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5)) # and는 논리연산자, &는 비트연산자, 둘 다 같은 결과가 나옴

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5)) # or는 논리연산자, |는 비트연산자, 둘 다 같은 결과가 나옴

print(5 > 4 > 3) # 5 > 4 and 4 > 3 과 같은 의미, 파이썬에서만 가능한 표현, 다른 언어에서는 불가능
print(5 > 4 > 7) # 5 > 4 and 4 > 7 과 같은 의미, False
 
