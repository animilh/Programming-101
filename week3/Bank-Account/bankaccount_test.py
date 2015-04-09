import unittest
from bankaccount import *


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.test_account = BankAccount('Ana', 150, 'BGN')
        print ("Starting Up")


    def tearDown(self):
        print ("Tearing Down")


    def test_create_new_bank_account_class(self):
        self.assertTrue(isinstance(self.test_account, BankAccount))


    def test_start_balance_negative(self):
        with self.assertRaises(ValueError):
            test = BankAccount('test',-10, '$')


    def test_int_value_from_account(self):
        self.assertEqual(int(self.test_account), 150)


    def test_str_value_from_account(self):
        self.assertEqual(str(self.test_account), "Ana's bank account, balance 150 BGN")


    def test_repr_value_from_account(self):
        self.assertEqual(repr(self.test_account), "Ana's bank account, balance 150 BGN")


    def test_deposit_amount_from_account(self):
        self.assertTrue(self.test_account.deposite(15) == self.test_account.balance())


    def test_negative_deposite_amount(self):
        with self.assertRaises(ValueError):
            self.test_account.deposite(-15)


    def test_balance_function_from_account(self):
        self.assertTrue(self.test_account.balance() == int(self.test_account))


    def test_withdraw_from_account(self):
        self.assertTrue(self.test_account.withdraw(50) == True)


    def test_withdraw_with_negative_amount(self):
        with self.assertRaises(ValueError):
            self.test_account.withdraw(-80)


    def test_withdraw_with_amount_bigger_than_balance(self):
        with self.assertRaises(ValueError):
            self.assertFalse(self.test_account.withdraw(200))


    def test_transfer_amount_to_account(self):
        test = BankAccount('Emo', 0, 'BGN')
        self.assertTrue(self.test_account.transfer(test, 50))


    def test_transfer_money_between_accounts_with_different_curruncies(self):
        test = BankAccount('Emo', 0, '$')
        with self.assertRaises(ValueError):
            self.assertFalse(self.test_account.transfer(test, 60))


    def test_transfer_sum_bigger_than_balance(self):
        test = BankAccount('Emo', 0, 'BGN')
        with self.assertRaises(ValueError):
            self.assertFalse(self.test_account.transfer(test, 300))


if __name__ == '__main__':
    unittest.main()
