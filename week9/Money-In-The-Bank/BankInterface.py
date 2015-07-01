class BankInterface():

    def __init__(self, account_manager):
	    self.__acount = account_manager
		
    def help_main(self):
	    for command in commands_main.keys():
		    print('{} - {}'.format(command, commands_main[command]))
			
    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.__acount.register(username, password)
        print("Registration Successfull.")
		
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        logged_user = self.__acount.login(username, password)
		
        if logged_user:
            logged_menu(logged_user)
        else:
            print('Login failed!')
		
    def info(self, logged_user):
        print("You are: " + logged_user.get_username())
        print("Your id is: " + str(logged_user.get_id()))
        print("Your balance is:" + str(logged_user.get_balance()) + '$')

    def change_pass(self, logged_user):
        new_pass = input("Enter your new password: ")
        self.__acount.change_pass(new_pass, logged_user)	
		
    def change_message(self, logged_user):
        new_message = input("Enter your new message>")
        self.__acount.change_message(new_message, logged_user)
		
    def show_message(self, logged_user):
        print(logged_user.get_message())
		
		
    def main_menu(self):
        print("Welcome to our bank service. You are not logged in. \nPlease register or login")
        while True:
            command = input("$$$>")
			
            if command == 'register':
                self.register()
				
            elif command == 'login':
                self.login()
				
            elif command == 'help':
                self.help_main()
				
            elif command == 'exit':
                print("Exit bank service!")
                break
				
            else:
                print("Not a valid command.")
				
    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                self.get_info(logged_user)
				
            elif command == 'change pass':
                self.change_pass(logged_user)
				
            elif command == 'change message':
                self.change_message(logged_user)
				
            elif command == 'show message':
                self.show_message(logged_user)
