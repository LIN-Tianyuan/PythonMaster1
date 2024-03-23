"""
account_amount = 0  # Solde du compte


def atm(num, deposit=True):
    global account_amount
    if deposit:
        account_amount += num
        print(f"Dépôts: + {num}, Solde du compte: {account_amount}")
    else:
        account_amount -= num
        print(f"Retraits: - {num}, Solde du compte: {account_amount}")


atm(300)
atm(300)
atm(100, False)
print('----------')
"""

def account_create(initial_amount = 0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"Dépôts: + {num}, Solde du compte: {initial_amount}")
        else:
            initial_amount -= num
            print(f"Retraits: - {num}, Solde du compte: {initial_amount}")
    return atm


fn = account_create()
fn(300)
fn(300)

fn1 = account_create()
fn1(700)