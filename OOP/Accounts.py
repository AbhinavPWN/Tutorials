import datetime
import pytz


class Account:
    """ Simple bank Account """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance) -> None:
        self.__name = name
        self.__balance = balance  # double underscore helps to make it non-public
        self.__transaction_list = [(Account._current_time(), balance)]
        print(f'Account created for {self.__name}')
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        self.show_balance()
        self.__transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.__transaction_list.append((Account._current_time(), -amount))
        else:
            print(
                'Your balance is less than you want to withdraw and also should be  more than zeros')
        self.show_balance()

    def show_balance(self):
        print(f'Your total balance is {self.__balance}')

    def show_transaction(self):
        for date, amount in self.__transaction_list:
            if amount > 0:
                tran_type = 'deposit'
            else:
                tran_type = 'withdrawn'
            print(
                f'{amount} {tran_type} on {date.astimezone()} ')


if __name__ == '__main__':
    abhi = Account('Abhinav', 10000)
    abhi.show_balance()
    abhi.deposit(10000)
    # abhi.withdraw(2000)
    abhi.withdraw(1000)

    print('***********' + ' Your Transaction ' + '*********')
    abhi.show_transaction()

    abhinav = Account('Abhi karki', 5000)
    abhinav.__balance = 1000
    abhinav.deposit(1000)
    abhinav.withdraw(500)
    abhinav.show_transaction()
