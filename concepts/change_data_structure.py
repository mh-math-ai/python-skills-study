# 자료구조의 변경

# 자료구조의 변경은 기존에 사용하던 자료구조를 다른 자료구조로 변경하는 것을 의미합니다.
# 예를 들어, 리스트를 튜플로 변경하거나, 딕셔너리를 리스트로 변경하는 등의 작업이 있습니다.
# 자료구조의 변경은 데이터의 형태를 바꾸는 것이므로, 
# 기존에 사용하던 자료구조의 메서드나 속성이 더 이상 유효하지 않을 수 있습니다.
# 따라서, 자료구조의 변경을 할 때는 
# 기존에 사용하던 자료구조의 메서드나 속성을 새로운 자료구조에 맞게 변경해야 합니다.
# 예를 들어, 리스트를 튜플로 변경할 때는 
# 리스트의 메서드인 append()나 extend() 등의 메서드를 사용할 수 없게 됩니다.
# 대신, 튜플의 메서드인 count()나 index() 등의 메서드를 사용할 수 있게 됩니다.  

menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>
menu = list(menu)
print(menu, type(menu)) # ['커피', '우유', '주스'] <class 'list'>
menu = tuple(menu)
print(menu, type(menu)) # ('커피', '우유', '주스') <class 'tuple'>
menu = set(menu)
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>

# Quiz} 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에서 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1부터 20까지라고 가정하겠습니다.
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가입니다.
# 조건3: random 모듈의 shuffle과 sample을 활용하겠습니다.

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
from random import * #random 모듈의 모든 함수를 가져옴 
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = range(1, 21) # 1부터 20까지의 숫자를 생성
#print(type(lst)) # <class 'range'>, range는 리스트가 아님
lst = list(lst) # range를 리스트로 변환
#print(type(lst)) # <class 'list'>, 리스트로 변환됨

shuffle(lst) # shuffle 함수는 리스트의 순서를 무작위로 섞어줌
print(lst) 
chicken = lst[0] 
lst = lst[1:]
coffee = sample(lst, 3)
print(f"-- 당첨자 발표 --\n치킨 당첨자 : {chicken}\n커피 당첨자 : {coffee}\n-- 축하합니다 --")


winners = sample(lst, 4) 
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")
