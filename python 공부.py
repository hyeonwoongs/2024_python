def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance+money)) #balance 잔액을 의미
    return balance + money # 입금 후 잔액 반환

balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금
  #def 함수명(전달값1, 전달값2, ...):
#       실행할 문장1
#       실행할 문장2
#       ...
#       return 반환값 반환값이 여러 개인 경우 쉼표로 구분해 튜플 형태로 반환