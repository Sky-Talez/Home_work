from  Home_work10 import AddressBook, Record, Name, Phone



phoneboook = AddressBook()


def input_error(func):
    def inner(data):
        try:
           return func(data)
        except KeyError:
            return "There are no contact like this in my phonebook"
        except IndexError:
            return "Give me name and phonenumber"
    return inner

def hello(data):
    return "Hello, how can i help you?"

@input_error
def phone(data: str):
    result = ""
    for i in phoneboook[data].phone_numbers:
        result = result + i.value + ", "
    return f"Contact {data} has phones {result}"
    
@input_error
def change(data: str):
    contact_info = data.split(" ")
    phoneboook[contact_info[0]].edit_phone(Phone(contact_info[1]), Phone(contact_info[2]))
    return f"Phonenumber {contact_info[1]} for {contact_info[0]} changed to {contact_info[2]}"

@input_error
def show_all(data):
    result = ""
    for record in phoneboook.values():
        phones = ""
        for phone in record.phone_numbers:
            phones = phones + phone.value +", "
        result = result + f"Name: {record.name.value}, phones {phones} \n"
    if len(result) == 0:
        result = "Phonebook is empty"
    return result


def exit(data):
    return "exit"

@input_error
def add(data: str):
    result = data.split(" ")
    result[0] = Name(result[0])
    for i in range(len(result[1:])):
        result[i+1] = Phone(result[i+1])
    phoneboook.add_record(*result)
    phones = ""
    for i in result[1:]:
        phones = phones + " " + i.value
    return f"Contact {result[0].value} with the phone number(s) {phones} added to phonebook"

COMANDS = {hello: "hello",
           add: "add",
           change: "change",
           phone: "phone",
           show_all: "show all",
           exit: ("exit", "good bye", "close")}


def parser(text: str) -> tuple[callable, str]:   
    for k in filter(lambda comand: text.lower().startswith(COMANDS[comand]) or text.lower() in COMANDS[comand], COMANDS.keys()):
        if type(COMANDS[k]) == tuple:
            for i in filter(lambda x: text == x, COMANDS[k]):
                return k, text.replace(i,"").strip()
        return k, text.replace(COMANDS[k],"").strip()
    

def main():
    while True:
        user_input = input(">>>")
        comand, data = parser(user_input)
        result = comand(data)
        if result == "exit":
            break
        print(result)

if __name__ == "__main__":
    main()