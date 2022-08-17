import json
from models import get_passport, Request, get_bank_acc
data = {
    'surname': 'harutyunyan',
    'middle_name': 'Norayri',
    'birth_date': '2004-13-11',
    'gender': 'Male',
}

obj = get_bank_acc('09058143')
obj.create_request(to='02143743', type='Output', value='800', send=True)
for el in obj.get_requests():
    print(el)

# with open('passports/OT2VCMMEMZpassport_data.json') as f:
#    json_file = json.load(f)
# obj = Passport(write=False, **json_file['Passport'])
# print(obj)
