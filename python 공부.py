def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

# balance = 0 # 초기 잔액
# balance = deposit(balance, 1000) # 1,000원 입금
# print(balance) # 반환값 저장

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
