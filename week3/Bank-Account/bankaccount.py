class History:

    CREATED = 'Account was created'
    BALANCE_CHECK = 'Balance check -> {}{}'
    INT_CHECK = '__int__ check -> {}{}'
    DEPOSITE = 'Deposited {}{}'
    DEPOSITE_FAILED = 'Deposited {}{}'
    WITHDRAW = '{}{} was withdrawed'
    WITHDRAW_FAILED = 'Withdraw for {}{} failed.'
    TRANSFER = "Transfered {}{} to {}'s account"
    TRANSFER_FAILED = "Transfer for {}{} to {}'s account failed"

class BankAccount:

    def __init__(self, name, start_balance, curruncy):
        if start_balance < 0:
            raise ValueError("Start balance must be >= 0")
        self.__name = str(name)
        self.__balance = start_balance
        self.__curruncy = str(curruncy)
        self.__history = [History.CREATED]


    def __int__(self):
        self.add_history(History.INT_CHECK.format(self.__balance, self.__curruncy))
        return self.__balance

    def __str__(self):
        return "{}'s bank account, balance {} {}".format(self.__name, self.__balance, self.__curruncy)

    def __repr__(self):
        return self.__str__()


    def deposite(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposite negative or zero amount")
            self.add_history(History.DEPOSITE_FAILED.format(amount, self.__curruncy))
        else:
            self.__balance += amount
            self.add_history(History.DEPOSITE.format(amount, self.__curruncy))
            return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw negative or zero amount")
            self.add_history(History.WITHDRAW_FAILED.format(self.__balance, self.__curruncy))
            return False

        if amount > self.balance():
            raise ValueError("Cannot withdraw more than balance in the account")
            self.add_history(History.WITHDRAW_FAILED.format(self.__balance, self.__curruncy))
            return False

        self.__balance -= amount
        self.add_history(History.WITHDRAW.format(self.__balance, self.__curruncy))
        return True


    def transfer(self, account, transfered_sum):
        if self.curruncy() != account.curruncy():
            raise ValueError("Cannot transfer money between accounts with different curruncies")
            self.add_history(History.TRANSFER_FAILED.format(self.__balance, self.__curruncy, self.__name))
            return False

        if self.balance() < transfered_sum:
            raise ValueError("Cannot transfer amount bigger than account balance")
            self.add_history(History.TRANSFER_FAILED.format(self.__balance, self.__curruncy, self.__name))
            return False

        self.__balance -= transfered_sum
        account.__balance += transfered_sum
        self.add_history(History.TRANSFER.format(transfered_sum, self.__curruncy, account.__name))
        return True


    def balance(self):
        self.add_history(History.BALANCE_CHECK.format(self.__balance, self.__curruncy))
        return self.__balance


    def holder(self):
        return self.__name

    def curruncy(self):
        return self.__curruncy

    def history(self):
        return self.__history

    def add_history(self, event):
        return self.__history.append(event)
