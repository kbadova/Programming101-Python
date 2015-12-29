import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Rado", 1000, "BGN")

    def test_deposit(self):
        self.assertEqual(self.account.deposit(1000), int("2000"))

    def test_balance(self):
        self.assertEqual(self.account.balance(), int("1000"))

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(200), True)

    def test__str__(self):
        self.assertEqual(self.account.__str__(), "Bank account for Rado with balance of 1000BGN")

    def test__int__(self):
        self.assertEqual(self.account.__int__(), 1000)

    def test_transfer(self):
        ivo = BankAccount("ivo", 1000, "BG")
        self.assertEqual(self.account.transfer_to(ivo, 500), "Not equal currencies")

    def test_list_history(self):
        self.assertEqual(self.account.history(), ['Account was created'])

if __name__ == '__main__':
    unittest.main()
