def deposit(name, sum):
    if name not in account:
        account[name] = 0
    account[name] += sum


def withdraw(name, sum):
    if name not in account:
        account[name] = 0
    account[name] -= sum


def balance(name):
    if name not in account:
        print('ERROR')
        return 1
    print(account[name])
    return 1


def transfer(name1, name2, sum):
    if name1 not in account:
        account[name1] = 0
    if name2 not in account:
        account[name2] = 0
    account[name1] -= sum
    account[name2] += sum


def income(p):
    for name in account:
        if account[name] > 0:
            account[name] += (account[name] * p )// 100


account = {}
with open('input.txt', 'r', encoding='utf8') as f:
    for row in f.readlines():
        if row.strip() != '':
            row = list(row.split())
            if row[0] == 'DEPOSIT': deposit(row[1], int(row[2]))
            elif row[0] == 'WITHDRAW': withdraw(row[1], int(row[2]))
            elif row[0] == 'BALANCE': balance(row[1])
            elif row[0] == 'TRANSFER': transfer(row[1], row[2], int(row[3]))
            elif row[0] == 'INCOME': income(int(row[1]))
