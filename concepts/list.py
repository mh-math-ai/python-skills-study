# # 리스트 []
# # 리스트는 여러 개의 값을 저장할 수 있는 자료형입니다.
# # 리스트는 대괄호 []로 감싸서 표현합니다.
# # 리스트는 다양한 자료형의 값을 저장할 수 있습니다.
# # 리스트는 순서가 있는 자료형입니다. 따라서 인덱스를 사용하여 요소에 접근할 수 있습니다.
# # 리스트는 변경 가능한 자료형입니다. 따라서 요소를 추가, 삭제, 변경할 수 있습니다.

# # 지하철 칸 별로 10명, 20명, 30명
# # subway1 = 10
# # subway2 = 20
# # subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호")) # index()는 리스트에서 특정 요소의 인덱스를 반환하는 함수입니다.

# # 하하가 다음 정류장에서 다음 칸에 탔다.
# subway.append("하하") # append()는 리스트에 요소를 추가하는 함수입니다.
# print(subway)

# # 정형돈을 유재석 조세호 사이에 태웠다.
# subway.insert(1, "정형돈") # insert()는 리스트의 특정 위치에 요소를 삽입하는 함수입니다.
# # .insert(인덱스, 요소) 형식으로 사용합니다. 인덱스는 0부터 시작합니다.
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) # pop()은 리스트에서 마지막 요소를 제거하고 반환하는 함수입니다.
# print(subway)

# # print(subway.pop()) 
# # print(subway)

# # print(subway.pop()) 
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인하기
# subway.append("유재석") 
# print(subway)
# print(subway.count("유재석")) # count()는 리스트에서 특정 요소의 개수를 반환하는 함수입니다.

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
# num_list.sort() # sort()는 리스트를 오름차순으로 정렬하는 함수입니다.
# print(num_list) 

# # 순서 뒤집기도 가능
# num_list.reverse() # reverse()는 리스트의 요소 순서를 뒤집는 함수입니다.
# print(num_list)

# # 모두 지우기
# num_list.clear() # clear()는 리스트의 모든 요소를 제거하는 함수입니다.
# print(num_list) 

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True] # 리스트는 다양한 자료형의 값을 저장할 수 있습니다.
#print(mix_list)
num_list.extend(mix_list)
print(num_list) # extend()는 리스트에 다른 리스트의 요소를 추가하는 함수입니다.
# .extend(리스트) 형식으로 사용합니다.    
