import datetime

class Client:
    def __init__(self,id_client, name,email):
        self.id_client=id_client
        self.name=name
        self.email=email
        self.accounts={}
        
class Bank:
    def __init__(self, name):
        self.name=name
        self.clients={}
        self.accounts={}
        self.next_account_number = 1
        self.next_client_id=1

    def create_client(self,name,email):
        client_id = self.next_client_id
        self.next_client_id += 1
        client=Client(client_id, name, email)
        self.clients[client_id]=client
        return client
    
    def open_account(self, client_id, currency, initial_balance):
        if client_id not in self.clients:
            raise ValueError("Client was not found")
        client=self.clients[client_id]
        if currency in client.accounts:
            raise ValueError(f"The client already has an account in the currency {currency}")
        account_number = f"ACC-{self.next_account_number}"
        self.next_account_number +=1
        account=BankAccount(account_number,client,currency,initial_balance)
        client.accounts[currency] = account
        self.accounts[account_number] = account
        return account
    
    def find_account(self, account_number):
        return self.accounts.get(account_number)
       
    
    def close_account(self,account_id, current_client_id):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        account = self.accounts[account_id]
        if account.client.id_client != current_client_id:
            raise ValueError("You can only transfer from your own accounts")
        if account.balance != 0:
            raise ValueError(f"Cannot close account with balance: {account.balance} {account.currency}. Withdraw all money first.")
        account.close_account()
        del self.accounts[account_id]
        client = account.client
        for currency, acc in client.accounts.items():
            if acc.account_id == account_id:
                del client.accounts[currency]
                break

    def transfer (self, from_account_number, to_account_number, money, current_client_id):
        from_account=self.find_account(from_account_number)
        to_account=self.find_account(to_account_number)
        if not from_account:
            raise ValueError ("Sender's account was not found")
        if not to_account:
            raise ValueError ("The recipient's account has not been found")
        if from_account.client.id_client != current_client_id:
            raise ValueError("You can only transfer from your own accounts")
        if  from_account.currency != to_account.currency:
            raise ValueError ("You cannot transfer between accounts in different currencies")
        from_account.send_money(to_account,money)
        
    def save_accounts_statement(self, client_id, filename=None):
        if client_id not in self.clients:
            raise ValueError("Client was not found")
        client=self.clients[client_id]
        if not filename:
            raise ValueError("The file name is not specified! Please specify the file name")
        total_balance = 0
        with open(filename,"w", encoding='utf-8') as file:
            file.write(f'ACCOUNT STATEMENT\n')
            file.write(f"Client:{client.name} (ID: {client_id})\n")
            file.write(f'Email {client.email}\n')
        
            for currency, account in client.accounts.items():
                file.write(f"Account: {account.account_id}\n")
                file.write(f"Currency: {currency}\n")
                file.write(f"Balance: {account.balance} {currency}\n")
                file.write(f"Status: {'Active' if account.is_active else 'Closed'}\n")
                total_balance += account.balance
            file.write(f"\nTOTAL BALANCE: {total_balance}\n")

        return filename
    
    def get_client_id(self):
        if not self.clients:
            print("No clients available. Please create a client first.")
            return None
        print("Available clients:")
        for client_id, client in self.clients.items(): 
            print(f"ID: {client_id}, Name: {client.name}, Email: {client.email}")
        try:
            client_id = int(input("Enter client ID: "))
            if client_id in self.clients:
                return client_id
            else:
                print("Invalid client ID!")
                return None
        except ValueError:
            print("Please enter a valid number!")
            return None
        
    def show_account(self,client_id):
        if client_id not in self.clients:
            raise ValueError("Client was not found /n")
        client=self.clients[client_id]
        print(f"name: {client.name}")
        for currency, account in client.accounts.items():
            status = "Active" if account.is_active else "Closed"
            print(f"  {currency}: {account.balance} {currency} (Account: {account.account_id}, Status: {status})")
            
         

class BankAccount:
    def __init__(self, account_id,client, currency, initial_balance=0):
        self.account_id=account_id
        self.client=client
        self.currency=currency
        self.balance=initial_balance
        self.is_active = True
        self.transactions = []
        
    def add_money(self,money):
        if  not self.is_active:
            raise ValueError("Account is closed")
        if money <= 0:
            raise ValueError ("the amount must be positive")
        self.balance += money
        self.transactions.append
        self.transactions.append(f"{datetime.datetime.now()}: +{money} {self.currency}")

    def take_money(self, money):
         if  not self.is_active:
            raise ValueError("Account is closed")
         if self.balance < money:
             raise ValueError ("there is not enough money in the balance")
         if money <= 0:
             raise ValueError("The amount must be positive")
         self.balance -=money
         self.transactions.append(f'{datetime.datetime.now()}: -{money} {self.currency}')

    def send_money(self,target_account, money):
        if not self.is_active:
            raise ValueError("Account is closed")
        if  not target_account.is_active:
             raise ValueError("Target account is closed")
        if self.balance < money:
             raise ValueError ("there is not enough money in the balance")
        if money <= 0:
             raise ValueError("The amount must be positive")
        self.balance -= money
        self.transactions.append(f'{datetime.datetime.now()}: -{money} {self.currency} (transfer to {target_account.account_id})')
        target_account.balance += money
        target_account.transactions.append(f'{datetime.datetime.now()}: +{money} {target_account.currency} (transfer from {self.account_id})')

    def close_account(self):
        if self.balance != 0:
            raise ValueError ("There should be no money in the account")
        self.is_active = False
        self.transactions.append(f"{datetime.datetime.now()}: the account is closed")   

def menu():
    print("1. Open account")
    print("2. Close account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer money")
    print("6. Show my accounts")
    print("7. Save statement to file")
    print("8. Exit")

def main ():
    bank = Bank("MyBank")

    client1 = bank.create_client("Алексей", "alex@test.com")
    bank.open_account(client1.id_client, "RUB", 1000)
    
    client2 = bank.create_client("Ольга", "olga@test.com") 
    bank.open_account(client2.id_client, "RUB", 2000)
    bank.open_account(client2.id_client, "USD", 100)
    
    print("Demo clients created!")
    print(f"Client 1 - ID: {client1.id_client}, Name: {client1.name}")
    print(f"Client 2 - ID: {client2.id_client}, Name: {client2.name}")

    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice==1:
            name=input('enter a name')
            email=input('enter email')
            client=bank.create_client(name,email)
            print(f"Client created with ID: {client.id_client}")

            currency = input("Enter currency: ")
            initial_balance = float(input("Enter initial balance: "))
            account = bank.open_account(client.id_client, currency, initial_balance)
            print(f"Account opened: {account.account_id}")

        elif choice==2:
            client_id = bank.get_client_id()
            if client_id:
                try:
                    account_id = input("Enter account ID to close: ")
                    bank.close_account(account_id, client_id)
                    print(" Account closed successfully")
                except ValueError:
                    print('Error')

        elif choice==3:
            client_id=bank.get_client_id()
            currency = input("Enter currency: ").upper()
            money = float(input("Enter amount to deposit: "))
            client=bank.clients[client_id]
            if currency in client.accounts:
                client.accounts[currency].add_money(money)
                print(f" {money} {currency} deposited ")
            else:
                print ('No account found for this currency')

        elif choice==4:
            client_id=bank.get_client_id()
            client=bank.clients[client_id]
            currency = input("Enter currency: ").upper()
            money = float(input("Enter amount to withdraw: "))
            if currency in client.accounts:
                client.accounts[currency].take_money(money)
                print(f" {money} {currency} withdraw ")
            else:
                print ('No account found for this currency')
           
        elif choice == 5:
            client_id=bank.get_client_id()
            if client_id:
                money = float(input("Enter amount to transfer: "))
                from_currency=input("Enter your account currency: ").upper()
                to_account_id = input("Enter recipient account ID: ")
                client=bank.clients[client_id]
                if from_currency in client.accounts:
                    from_account=client.accounts[from_currency]
                    bank.transfer(from_account.account_id,to_account_id, money, client_id)
                    print(f"Successfully transferred {money} {from_currency}")
                else:
                    print("No account found for this currency")

        elif choice == 6:
            client_id=bank.get_client_id()
            if client_id:
                bank.show_account(client_id)

        elif choice == 7:
            client_id=bank.get_client_id()
            if client_id:
                file_name=input('enter a filename ')
                print(f"Statement saved to: { bank.save_accounts_statement(client_id, file_name )}")
            else:
                print('Error ')

        elif choice == "8":
            print("You're out")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 8.")

main()