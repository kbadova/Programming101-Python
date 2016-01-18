class Bill:

    def __init__(self, amount):
        if amount < 0:
            raise ValueError
        try:
            self._amount = amount
        except:
            raise TypeError

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "A {}$ bill".format(self._amount)

    def __hash__(self):
        return hash(self._amount)

    def __eq__(self, other):
        return self._amount == other.total()

    def total(self):
        return self._amount

    def __int__(self):
        return int(self._amount)


class BatchBill:

    def __init__(self, list_of_Bills):
        self.__list_of_Bills = list_of_Bills

    def __len__(self):
        return len(self.__list_of_Bills)

    def total(self):
        return sum(bill.total() for bill in self.__list_of_Bills)

    def __getitem__(self, index):
        return self.__list_of_Bills[index]


class CashDesk:

    def __init__(self):
        self.array_of_money = []

    def take_money(self, obj):
        self.array_of_money.append(obj)

    def total(self):
        return sum([obj.total() for obj in self.array_of_money])

    def __str__(self):
        return "{}".format(self.array_of_money)

    def inspect(self):
        list_of_string = []
        list_of_string.append("We have a total of {}$ in the desk".format(self.total()))
        list_of_amounts = []

        bills = self.array_of_money
        if self.total() > 0:
            list_of_string.append("We have the following count of bills, sorted in ascending order:")
            for bill in bills:
                if isinstance(bill, BatchBill):
                    for one_bill in bill:
                        list_of_amounts.append(one_bill.total())
                else:
                    list_of_amounts.append(bill.total())
            for amount in sorted(set(list_of_amounts)):
                list_of_string.append("{}$ bills - {}".format(amount, list_of_amounts.count(amount)))
            return "\n".join(list_of_string)

