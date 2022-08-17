SYMBOLS = list('abcdefghijklmnopqrstuvwxyz')


def name_updater(name):
    name = name.lower()
    for el in name:
        if el not in SYMBOLS:
            raise ValueError(f'{el} is the incorrect character in {name}')
    return name[0].upper() + name[1:]


def date_updater(date):
    if isinstance(date, str):
        return date
    if len(date) != 3:
        raise ValueError(f'Invalid len of values ({len(date)}) (must be 4)')
    if len(str(date[0])) != 4:
        raise ValueError(f'{date[0]} is incorrect value for year')
    if date[1] > 29 and date[2] == 2:
        raise ValueError(f'{date[1]} is incorrect value for day')
    if date[1] < 1 or date[1] > 31:
        raise ValueError(f'{date[1]} is incorrect value for day')
    if date[2] > 12 or date[2] < 1:
        raise ValueError(f'{date[2]} is incorrect value for month')
    return f'{str(date[0])}-{str(date[1])}-{str(date[2])}'
