class Client():
    def __init__(self, name:str, phone_num:str) -> None:
        
        self.name = name
        self.phone = phone_num


class Account():
    def __init__(self, *clients:Client, limit:float=-100.00):

        self.__holders = clients
        self.__holder_list = []
        for holder in self.__holders:
            self.__holder_list.append(f'{holder.name} ({holder.phone})')

        self.__balance = 0
        self.__saving_balance = 0
        self.__statement = []

        self.__limit = limit


    def get_info(self):
        names = ', '.join(self.__holder_list)
        info = f'Holders on this account: {names}'
        print(info)
        print("")


    def __update_statement(self, value:float, operation:int, saving:bool):

        if not saving:
            if operation == 0:  
                self.__statement.append(f'Withdraw: - ${value:.2f}')
            elif operation == 1:
                self.__statement.append(f'Deposit: + ${value:.2f}')
        else:
            if operation == 0:  
                self.__statement.append(f'Withdraw (Savings): - ${value:.2f}')
            elif operation == 1:
                self.__statement.append(f'Deposit (Savings): + ${value:.2f}')


    def withdraw(self, value:float, saving:bool=False):
        if not saving:
            if (self.__balance - value) >= self.__limit:
                self.__balance -= value
                self.__update_statement(value, 0, saving)
                print(f'You have withdrawn ${value:.2f} from your account.')
            else:
                print(f'Your current limit is ${self.__limit} and you cannot exceed it. To change your limit, please get in contact with your personal manager.')
        else:
            if self.__saving_balance - value >= 0:
                self.__saving_balanace -= value
                self.__update_statement(value, 0, saving)
                print(f'You have withdrawn ${value:.2f} from your saving account.')
            else:
                print(f'You cannot go below $0.00 on your saving account. Bruh!')


    def deposit(self, value:float, saving:bool=False):
        if not saving:
            self.__balance += value
            self.__update_statement(value, 1, saving)
            print(f'You have deposited ${value:.2f} to your account.')
        else:
            self.__saving_balance += value
            self.__update_statement(value, 1, saving)
            print(f'You have deposited ${value:.2f} to your saving account.')


    def get_balance(self):
        print(f'Your current balance is ${self.__balance:.2f}')


    def get_saving_balance(self):
        print(f'Your current saving balance is ${self.__saving_balance:.2f}')
    

    def get_statement(self):
        print("")
        print("Account Statement:")
        for entry in self.__statement:
            print(entry)

        self.get_balance()
        self.get_saving_balance()