# 사전
# 딕셔너리는 중괄호 {}로 표현
# 딕셔너리는 순서가 없다. (파이썬 3.7 이전 버전에서는 순서가 없었지만, 3.7 이후 버전에서는 순서가 유지됩니다.)
# 딕셔너리는 변경 가능한 자료형입니다. 따라서 요소를 추가, 삭제, 변경할 수 있습니다. 

# cabinet = {3: "유재석", 100: "김태호"} # 딕셔너리는 키와 밸류로 이루어져 있습니다. 키는 고유해야 합니다.
# print(cabinet[3]) # 딕셔너리에서 키를 사용하여 값을 가져올 수 있습니다.
# print(cabinet[100])
# print(cabinet.get(3)) # get() 메서드를 사용하여 값을 가져올 수도 있습니다. 
# # get() 메서드는 키가 존재하지 않을 경우 None을 반환합니다.
# # print(cabinet[5]) # 존재하지 않는 키를 가져오려고 하면 KeyError가 발생합니다. 
# # 여기서 프로그램이 종료됩니다. 따라서 get() 메서드를 사용하는 것이 안전합니다.

# print(cabinet.get(5)) # 존재하지 않는 키를 가져오려고 하면 None이 반환됩니다.
# print(cabinet.get(5, "사용 가능")) # get() 메서드의 두 번째 인자로 기본값을 설정할 수 있습니다.
# print("hi") # 프로그램이 종료되지 않고 계속 실행됩니다.

# print(3 in cabinet) # in 연산자를 사용하여 키가 딕셔너리에 존재하는지 확인할 수 있습니다.
# print(5 in cabinet) 

cabinet = {"A-3": "유재석", "B-100": "김태호"} # 키에 숫자뿐만 아니라 문자열도 사용할 수 있습니다.
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님이 들어옴
print(cabinet)
cabinet["A-3"] = "김종국" # 기존 키에 새로운 값을 할당하면 기존 값이 덮어씌워집니다.
cabinet["C-20"] = "조세호" # 새로운 키와 값을 추가할 수 있습니다.
print(cabinet) 

# 손님이 나감
del cabinet["A-3"] # del 키워드를 사용하여 딕셔너리에서 요소를 제거할 수 있습니다.
print(cabinet)

# key 들만 출력
print(cabinet.keys()) # keys() 메서드를 사용하여 딕셔너리의 키를 가져올 수 있습니다.

# value 들만 출력
print(cabinet.values()) # values() 메서드를 사용하여 딕셔너리의 값을 가져올 수 있습니다.

# key, value 쌍으로 출력
print(cabinet.items()) # items() 메서드를 사용하여 딕셔너리의 키와 값을 튜플 형태로 가져올 수 있습니다.

# 목욕탕 폐점
cabinet.clear() # clear() 메서드를 사용하여 딕셔너리의 모든 요소를 제거할 수 있습니다.
print(cabinet)