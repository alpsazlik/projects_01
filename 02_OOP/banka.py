from pprint import pprint

alp_account = {
    'account no': '12345',
    'full name': 'Alp Sazlık',
    'password': '1907',
    'balance': 999999999999999999,
    'additional balance': 1000,
    'iban': 'TR-a88faefe-b306-4fda-9b20-558c168905bf'
}

berkay_account = {
    'account no': '98765',
    'full name': 'Berkay Karaca',
    'password': '1303',
    'balance': 4000,
    'additional balance': 1000,
    'iban': 'TR-0d09819e-8916-4bd1-8502-abbd833b57ad'
}

users = [alp_account, berkay_account]

def login(account_no: str, password: str) -> dict:
    print('Sign In')
    for user in users:
        if user['account no'] == account_no and user['password'] == password:
            return user
    return None

def menu(account: dict) -> str:
    return (f'Welcome, {account["full name"]}\n'
            f'=============================\n'
            f'Withdraw Money ------------>1\n'
            f'Deposit Money ------------->2\n'
            f'EFT ----------------------->3\n'
            f'Account Info -------------->4\n'
            f'Exit ---------------------->5\n'
            f'===============================\n')

def balance_result(account: dict) -> str:
    return (f'Account No: {account["account no"]}\n'
            f'Balance: {account["balance"]}\n'
            f'Additional Balance: {account["additional balance"]}')

def withdraw_money(amount: int, account: dict) -> bool:
    if account['balance'] >= amount:
        account['balance'] -= amount
        print(balance_result(account))
        return True
    else:
        total_balance = account['balance'] + account['additional balance']
        if total_balance >= amount:
            use_additional_balance = input(
                'Insufficient balance. Do you want to use additional balance? ("y" or "n"): ').lower()

            if use_additional_balance == 'y':
                amount_used_from_additional = amount - account['balance']
                account['balance'] = 0
                account['additional balance'] -= amount_used_from_additional
                print(balance_result(account))
                return True
            elif use_additional_balance == 'n':
                print('Transaction has been cancelled.')
                print(balance_result(account))
                return False
            else:
                print('Please choose a valid answer. ("y" or "n")')
                return False
        else:
            print('Insufficient total balance. Transaction has been cancelled.')
            return False

def deposit_money(amount: int, account: dict):
    account['balance'] += amount
    if account['additional balance'] < 1000:
        transfer_amount = 1000 - account['additional balance']
        if account['balance'] >= transfer_amount:
            account['balance'] -= transfer_amount
            account['additional balance'] += transfer_amount
    print(balance_result(account))

def eft_transaction(sender_account: dict, receiver_iban: str, amount: int):
    for user in users:
        if user['iban'] == receiver_iban:
            result = withdraw_money(amount=amount, account=sender_account)
            if result:
                deposit_money(amount=amount, account=user)
                print('EFT completed successfully.')
            return
    print('Receiver IBAN not found. Transaction cancelled.')

def main():
    user_account = login(
        account_no=input('Account No: '),
        password=input('Password: ')
    )

    if user_account:
        while True:
            print(menu(account=user_account))
            process = input('Please type a process number: ')

            if process == '1':
                amount = int(input('Amount: '))
                withdraw_money(amount=amount, account=user_account)
            elif process == '2':
                amount = int(input('Amount: '))
                deposit_money(amount=amount, account=user_account)
            elif process == '3':
                receiver_iban = input("Receiver IBAN: ")
                amount = int(input('Amount: '))
                eft_transaction(sender_account=user_account,
                                receiver_iban=receiver_iban,
                                amount=amount)
            elif process == '4':
                pprint(user_account)
            elif process == '5':
                print("Goodbye!")
                break
            else:
                print('Please choose a valid process number.')
    else:
        print('Invalid credentials. Login failed.')

main()