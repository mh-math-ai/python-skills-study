python = "Python is Amazing"
print(python.lower())
# 문자열을 모두 소문자로 변환하는 메서드입니다.
print(python.upper())
# 문자열을 모두 대문자로 변환하는 메서드입니다.
print(python[0].isupper())
# 문자열의 특정 위치에 있는 문자가 대문자인지 확인하는 메서드입니다
print(len(python))
# 문자열의 길이를 반환하는 메서드입니다.
print(python.replace("Python", "Java"))
# 문자열에서 특정 부분을 다른 문자열로 대체하는 메서드입니다.

index = python.index("n")
print(index)
# 문자열에서 특정 문자가 처음으로 나타나는 위치의 인덱스를 반환하는 메서드입니다. 
# 만약 찾는 문자가 문자열에 없으면 오류가 발생합니다.
index = python.index("n", index + 1)
print(index)
# index 메서드에 두 번째 인자로 시작 인덱스를 지정하여, 특정 문자가 나타나는 위치를 찾을 수 있습니다.

print(python.find("n"))
# 문자열에서 특정 문자가 처음으로 나타나는 위치의 인덱스를 반환하는 메서드입니다. 
# 만약 찾는 문자가 문자열에 없으면 -1을 반환합니다.
print(python.find("Java"))
# print(python.index("Java"))
# index 메서드는 찾는 문자가 문자열에 없으면 오류가 발생하지만,
# find 메서드는 -1을 반환합니다. 
# 따라서 find 메서드를 사용하여 문자열에서 특정 문자가 존재하는지 확인할 수 있습니다.
print("hi")
print(python.count("n"))
# 문자열에서 특정 문자가 나타나는 횟수를 반환하는 메서드입니다.
