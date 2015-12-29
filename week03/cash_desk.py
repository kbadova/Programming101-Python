class Bill:

    def __init__(self, amount):
        self.__amount = amount

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "A {}$ bill".format(self.__amount)

    def __hash__(self):
        return hash(self.__amount)

    def __eq__(self, other):
        return self.__amount == other.total()

    def total(self):
        return self.__amount


class BatchBill:

    def __init__(self, list_of_Bills):
        self.__list_of_Bills = list_of_Bills

    def __len__(self):
        return len(self.__list_of_Bills)

    def total(self):
        return sum(bill.total() for bill in bills)

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
