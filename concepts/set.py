# 집합 (Set)
# - 중복을 허용하지 않음
# - 순서가 없음 (인덱싱 불가)

# my_set = {1, 2, 3, 3, 3} 
# print(my_set) # {1, 2, 3} 

java = {"김태호", "유재석", "양세형"}
python = set(["유재석", "박명수"]) # set() 함수를 이용하여 리스트를 집합으로 변환

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) 
print(java.intersection(python)) # intersection() 메서드를 이용하여 교집합 구하기

# 합집합 (java 또는 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # union() 메서드를 이용하여 합집합 구하기

# 차집합 (java는 할 수 있지만 python은 할 수 없는 개발자)
print(java - python)
print(java.difference(python)) # difference() 메서드를 이용하여 차집합 구하기

# python을 할 수 있는 사람이 늘어남
python.add("김태호") # add() 메서드를 이용하여 집합에 요소 추가
print(python) # {'유재석', '박명수', '김태호'}

# java를 까먹은 사람이 생김
java.remove("김태호") # remove() 메서드를 이용하여 집합에서 요소 제거
print(java) # {'유재석', '양세형'}

