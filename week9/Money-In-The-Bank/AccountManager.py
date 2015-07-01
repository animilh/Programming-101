UPDATE_MESSAGE = """UPDATE clients
				 SET message = ?
				 WHERE id = ?"""
									
UPDATE_PASSOWRD = """UPDATE clients
				SET password = ?
				WHERE id = ?"""	

INSERT_CLIENT = """INSERT INTO clients (username, password)
				VALUES (?, ?)"""

SELECT_CLIENT = """SELECT id, username, balance, message
			  FROM clients
			  WHERE username = ? AND password = ? LIMIT 1"""

class AccountManager():
    def __init__(self, conn):
        self.__conn = conn
		
    def register(self, username, password):
        cursor = self.__conn.cursor()
        cursor.execute(AccountManager.INSERT_CLIENT, (username, password))
        self.__conn.commit()
		
    def login(self, username, password):
        cursor = self.__conn.cursor()
        client = cursor.execute(AccountManager.SELECT_CLIENT, (username, password))
        self.__conn.commit()
		
    def change_message(self, new_message, logged_user):
        cursor = self.__conn.cursor()
        message = cursor.execute(AccountManager.UPDATE_MESSAGE, (new_message, logged_user.get_id()))
        logged_user.set_message(new_message)
        self.__conn.commit()


    def change_pass(self, new_pass, logged_user):
        cursor = self.__conn.cursor()
        upd_pass = cursor.execute(AccountManager.UPDATE_PASSOWRD, (new_pass, logged_user.get_id()))
        self.__conn.commit()
