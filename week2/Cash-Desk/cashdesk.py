class Bill:

    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("Invalid value for bill amount")
        if isinstance(amount, float):
            raise TypeError("Bill amount cannot be float number")
        self.amount = amount

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __repr__(self  ):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount + 13)

    def __add__(self, other):
        return self.amount + other.amount


class BatchBill:

    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

    def total(self):
        return sum(self.list)

    def __getitem__(self, index):
        return self.list[index]


class CashDesk:

    def __init__(self):
        self.cash = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self.cash.append(money)

        elif isinstance(money, BatchBill):
            self.cash.extend(money)

    def total(self):
        return sum(int(money) for money in self.cash)

    def inspect(self):
        inspect = {money: self.cash.count(money) for money in self.cash}
        for key in inspect:
            print ("{} - {}".format(key, str(inspect[key])))



values = [10, 20, 50, 100, 10, 15]
bills = [Bill(value) for value in values]
print (bills)
batch = BatchBill(bills)

for bill in batch:
    print (bill)

desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(15))
print(desk.total())
print(desk.inspect())
