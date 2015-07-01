import sqlite3
from settings import DB_CONNECTION_STRING
from AccountManager import AccountManager
from BankInterface import BankInterface


def main():
    conn = sqlite3.connect(DB_CONNECTION_STRING)
    conn.row_factory = sqlite3.Row

    bank_manager = AccountManager(conn)
    interface = BankInterface(bank_manager)
    interface.main_menu()

if __name__ == "__main__":
    main()
