"""
暑期python学习

version:0.1
author:Jason
date: 2019-08-09
"""
from threading import Thread, Lock
from time import sleep


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):  # 模拟存款过程
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.02)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoney(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoney(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为%d 元' % account.balance)


if __name__ == '__main__':
    main()
