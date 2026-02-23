# 저장값 (Input)
# 함수나 프로그램으로 들어가는 값
# 함수나 프로그램에 전달하는 값을 인자(argument)라고 한다.
# parameter 

# 출력값 (Output)
# 함수나 프로그램이 돌려주는 값
# print() 함수를 사용하여 출력을 한다.
# return value

def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 이 함수는 저장값을 받지 않고, 출력값을 리턴한다.


def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money # 리턴값을 반환한다.

def withdraw(balance, money): # 출금 
    if balance >= money: 
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0 # 잔액 
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)


def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))