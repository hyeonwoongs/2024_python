def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금
print(balance) # 반환값 저장

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다.".format(balance))
        return balance

balance = 0 # 초기 잔액
balance = dep(balance, 1000) # 1,000원 입금
print(balance) # 반환값 저장

  #def 함수명(전달값1, 전달값2, ...):
#       실행할 문장1
#       실행할 문장2
#       ...
#       return 반환값 반환값이 여러 개인 경우 쉼표로 구분해 튜플 형태로 반환