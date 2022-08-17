import json
from random import choice


PASS_ID_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
BANK_NUMBER_SYMBOLS = '1234567890'


# pass_id_generator() function generate a unique ID for new created passport
def pass_id_generator():
    res = ''
    for _ in range(10):
        res += choice(PASS_ID_SYMBOLS)
    try:
        with open(f'passports/{res}.json', 'r') as file:
            pass
        return None
    except:
        return res

# bank_number_generator() function generate the unique number for BankAccount object
def bank_number_generator():
    res = ''
    for _ in range(8):
        res += choice(BANK_NUMBER_SYMBOLS)
    try:
        with open(f'bank_accounts/{res}.json', 'r') as file:
            pass
    except:
        return res
