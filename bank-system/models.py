"""
    models.py - this file for the models of the project.
                Here you can find all the models used in the
                project.
    Passport - this model for saving Passports of the customers
               of the bank
    BankAccount - this model for saving BankAccounts data for
                  bank
"""
import pytz
import os
from checker import name_updater, date_updater
import json
from others import pass_id_generator, bank_number_generator
from datetime import datetime


# Passport model
class Passport:
    def __init__(self, write=True, **kwargs):
        self.pass_id = pass_id_generator() if write else kwargs.get('pass_id')
        self.name = name_updater(kwargs.get('name'))
        self.surname = name_updater(kwargs.get('surname'))
        self.middle_name = name_updater(kwargs.get('middle_name'))
        self.gender = name_updater(kwargs.get('gender'))
        self.birth_data = date_updater(kwargs.get('birth_data'))
        if write:
            self.apply_changes()

    # applied changes after creating object
    def apply_changes(self):
        with open(f'passports/{self.pass_id}.json', 'w') as write_file:
            json.dump({'Passport': self.__dict__}, write_file, indent=4, separators=(',', ':'))

    def __str__(self):
        if self.pass_id is None:
            return 'Passport not found!'

        return f'Name - {self.name}\n' \
               f'Surname - {self.surname}' \
               f'\nMiddle name - {self.middle_name}' \
               f'\nGender - {self.gender}' \
               f'\nBirth data - {self.birth_data}\n' \
               f'Passport ID - {self.pass_id}'


# BankAccount
class BankAccount:
    def __init__(self, write=True, **kwargs):
        self.owner = kwargs.get('owner')
        self.bank_number = bank_number_generator() if write else kwargs.get('bank_number')
        tmp = kwargs.get('balance', None)
        self.balance = tmp if tmp is not None else 0

        if write:
            self.apply_changes()

    # applied changes after creating object
    def apply_changes(self):
        with open(f'bank_accounts/{self.bank_number}.json', 'w') as write_file:
            json.dump({'Bank Account': self.__dict__}, write_file, indent=4, separators=(',', ':'))

    def get_requests(self):
        directory = './requests'
        requests = []
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                tmp = f.split('/')[2]
                if self.bank_number in tmp:
                    requests.append(tmp)
        res = []
        for path in requests:
            with open(f'requests/{path}', 'r') as f:
                data = json.load(f)
                res.append(Request(False, **data['Request']))
        return res

    def create_request(self, to, type, value, send=False):
        req = Request(write=send, owner=self.bank_number, to=to, type=type, value=value)

    def __str__(self):
        passport = get_passport(pass_id=self.owner)
        return f'Name - {passport.name}\n' \
               f'Surname - {passport.surname}' \
               f'\nMiddle name - {passport.middle_name}' \
               f'\nGender - {passport.gender}' \
               f'\nBirth data - {passport.birth_data}\n' \
               f'Passport ID - {passport.pass_id}\n' \
               f'Bank acc number - {self.bank_number}\n' \
               f'Balance - {self.balance}'


class Request:
    def __init__(self, write=True, **kwargs):
        self.type = kwargs.get('type')
        self.owner = kwargs.get('owner')
        self.to = kwargs.get('to')
        self.value = kwargs.get('value')
        ty_zn = pytz.timezone('Asia/Yerevan')
        self.time = str(datetime.now(ty_zn))
        self.time = self.time[:self.time.find('.')]
        self.accepted = False

        if write:
            if self.apply_changes() is False:
                print('You have already sent request on this bank number')

    def apply_changes(self):
        try:
            with open(f'requests/{self.owner}-{self.to}.json', 'r') as write_file:
                return False
        except:
            with open(f'requests/{self.owner}-{self.to}.json', 'w') as write_file:
                json.dump({'Request': self.__dict__}, write_file, indent=4, separators=(',', ':'))

    def __str__(self):
        return f'Owner - {self.owner}\n' \
               f'To - {self.to} \n'\
               f'Type - {self.type}\n' \
               f'Value - {self.value}\n' \
               f'Time - {self.time}\n' \
               f'Accepted - {self.accepted}'


# get_passport(pass_id) function is finding the passport by unique id and returned it as a object Passport
def get_passport(pass_id):
    with open(f'passports/{pass_id}.json', 'r') as f:
        data = json.load(f)
        obj = Passport(False, **data['Passport'])
        return obj


def get_bank_acc(acc):
    with open(f'bank_accounts/{acc}.json', 'r') as f:
        data = json.load(f)
        obj = BankAccount(False, **data['Bank Account'])
        return obj
