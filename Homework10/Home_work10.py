from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass

        

class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = name

    phone_numbers = []

    def add_phone(self, phone):
        self.phone_numbers.append(phone)

    
    def remove_phone(self, phone):
        self.phone_numbers.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        for i in filter(lambda x: x.value == old_phone, self.phone_numbers):
            i.value = new_phone


class AddressBook(UserDict):
    def add_record(self, *args):
        new_record = Record(args[0])
        if len(args) > 1:
            for i in args[1:]:
                new_record.add_phone(i)
        self.data.update({new_record.name.value: new_record})


