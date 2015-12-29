class BankAccount:

    def __init__(self, name, initial_balance, currency):
        self._name = name
        self._initial_balance = initial_balance
        self._currency = currency
        self.list_history = []
        self.list_history.append("Account was created")

    def deposit(self, amount):
        self._initial_balance += amount
        self.list_history.append("Deposit {}{}".format(amount, self._currency))
        return self._initial_balance

    def balance(self):
        self.list_history.append("Balance check -> {}{}".format(self._initial_balance, self._currency))
        return self._initial_balance

    def withdraw(self, amount):
        if self._initial_balance > amount:
            self._initial_balance -= amount
            self.list_history.append("{}{} was withdrawed".format(amount, self._currency))
            return True
        return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".\
                format(self._name, self.balance(), self._currency)

    def __int__(self):
        self.list_history.append("__int__ check -> {}{}".format(self._initial_balance, self._currency))
        return self._initial_balance


    def transfer_to(self, account, amount):
        if self._currency == account._currency:
            self._initial_balance -= amount
            account._initial_balance += amount
            self.list_history.append("Transfer to {} for {}{}".format(account._name, amount, self._currency))
            return True
        return "Not equal currencies"

    def history(self):
        return self.list_history


