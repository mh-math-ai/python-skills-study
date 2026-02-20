# continue and break
# continue는 반복문에서 실행을 중단하고, 다음 반복문으로 이동하여 처리한다.
# break는 반복문에서 실행을 중단하고, 그 시점의 반복문을 종료한다.

absent = [2, 5] # 결석한 학생
no_book = [7] # 책을 깜빡한 학생

for student in range(1, 11): # 1, 2, ... , 10
    if student in absent:
        continue # 결석자는 더이상 실행하지 않고 다음 반복문으로
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 책을 깜빡한 학생이 나오면 반복문을 종료하고 프로그램 종료
    print("{0}, 책을 읽어봐".format(student))

 