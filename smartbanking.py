class Account:
    """This Super class doesnt take any instance aruguments."""
    _ids = ["Phurbagyalzen@gmail.com",
            "suniltmg@gmail.com",
            "nishanthapa@gmail.com",
            "nischalkhatri@gmali.com",
            "sanjiblimbu@gmail.com"]
    _passwords = ["123456789","98765432","53257843","232413577","75422763"]
    _amounts = [50000, 60000, 200000, 865422, 1000000, 255555]
    _signatures = ["Phurba", "Sunil", "Nishan", "Nischal", "Sanjib"]
    _account_numbers = ["123456","234567","345678","456789","567890"]
    _cards = ["auex97","xihs47","iabn55","hiaf34","asre98"]
    _pins = ["2345","3452","2324","5353","4353"]

    def verify_account(self,account_number, signature):
        """Takes account number and signature from the users and verify it."""
        if account_number in Account._account_numbers:

            self._indx = Account._account_numbers.index(account_number)
            if signature == Account._signatures[self._indx]:
                return True
            else:
                print("Your signature does not match.")
                return False
        else:
            print("Account does not exist!")
            return False

    def make_transaction(self,t_option,amount):
        if t_option.upper() == "D":
            Account._amounts[self._indx] = Account._amounts[self._indx] + amount
            return Account._amounts[self._indx]
        elif t_option.upper() == "W":
            if amount > Account._amounts[self._indx]:
                print("You have not enough balance.")
                return False
            Account._amounts[self._indx] = Account._amounts[self._indx] - amount
            return Account._amounts[self._indx]
        else:
            print("Invalid Option!")
            return False

    @property
    def transaction_instruction(self):
        print("-" * 30,"Access granted!!!","-" * 30)
        print("""Transaction Option:\n-> Deposite(D)\n-> Withdraw(W)\n-> Show balance(S)\n-> Exit(X)""")

    def show_amount(self):
        """Shows clients amount."""
        print("Your total amount is {}".format(Account._amounts[self._indx]))

    def options(self,account_number,signature):
        while True:
            if self.verify_account(account_number,signature):
                self.transaction_instruction
                t_option = input("What do you want to do? (D/W/S/X): ")
                if t_option.upper() == "X":
                    break
                if t_option.upper() == "S":
                    self.show_amount()
                    break

                if t_option not in ["D","W","S","X","d","w","s","x"]:
                    print("Option not available.")
                    self.options(account_number,signature)
                    break
                else:
                    amount = int(input("Enter the amount: "))
                    if self.make_transaction(t_option,amount):
                        print("Trasaction complete.")
                        self.show_amount()
                        break

            else:
                print("Invalid Input!")
                break


class ATM(Account):
    """inherits from super classs Account"""
    def verify_account(self,card, pin):
        """overwrites the super class method verify_acoount and takes client card and pin as argument and checks it."""
        if card in Account._cards:
            self._indx = Account._cards.index(card)
            if pin == Account._pins[self._indx]:
                print("Access granted!")
                return True
            else:
                print("Pin does not match!")
                return False
        else:
            print("Warning!!! Please use a valid card.")
            return False

    def options(self,card,pin):

            if self.verify_account(card,pin):
                self.transaction_instruction
                t_option = input("What do you want to do? (D/W/S/X): ")
                if t_option.upper() == "X":
                    return
                if t_option.upper() == "S":
                    self.show_amount()
                    return

                if t_option not in ["D","W","S","X","d","w","s","x"]:
                    print("Option not available.")
                    self.options(card,pin)
                    return

                else:
                    amount = int(input("Enter the amount: "))
                    if self.make_transaction(t_option,amount):
                        print("Trasaction complete.")
                        self.show_amount()
                        return
            else:
                print("Invalid Input!")
                return



class InternetBanking(Account):
    """inherits from super classs Account"""
    def verify_account(self,email, password):
        """overwrites the super class method verify_acoount and takes clients email and password as argument and checks it."""
        if email in Account._ids:
            self._indx = Account._ids.index(email)
            if password == Account._passwords[self._indx]:
                print("You are logged in.")
                return True
            else:
                print("Your Password does not match.")
                return False
        else:
            print("Email does not exist!")
            return False

    def options(self,email,password):

        if self.verify_account(email,password):
            self.transaction_instruction
            t_option = input("What do you want to do? (D/W/S/X): ")
            if t_option.upper() == "X":
                return
            if t_option.upper() == "S":
                self.show_amount()
                return

            if t_option not in ["D","W","S","X","d","w","s","x"]:
                print("Option not available.")
                self.options(account_number,signature)
                return
            else:
                amount = int(input("Enter the amount: "))
                if self.make_transaction(t_option,amount):
                    print("Trasaction complete.")
                    self.show_amount()
                    return
        else:
            print("Invalid Input!")
            return

class Cheque(Account):
    """inherits from super classs Account"""
    pass

print("-" * 30, "Welcome to Novel Bank","-" * 30)
print("""Our Services:
            1)Cheque System
            2)Internet Banking
            3)ATM""")

def services():
    """Creates an infinite recursion unless exit is entered."""
    option = input("Choose Your Option(1/2/3): ")
    if option == "1":
        obj = Cheque()
        account_number = input("Enter your account number: ")
        signature = input("Enter your signature: ")
        obj.options(account_number,signature)

    elif option == "2":
        obj = InternetBanking()
        email = input("Enter your id: ")
        password = input("Enter your password: ")
        obj.options(email,password)

    elif option == "3":
        obj = ATM()
        card = input("Please insert your card: ")
        pin = input("Enter your pin: ")
        obj.options(card,pin)

    elif option.lower() == "exit":
        print("Thank you!")
        return

    else:
        print("Option Unavialable!")
    print("-" * 30, "To exit Enter:\"exit\"", "-" * 30)
    services()
services()










