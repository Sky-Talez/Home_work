phoneboook = {}

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
    result = phoneboook[data]
    return f"Contact {data} has phone {result}"
    
@input_error
def change(data: str):
    contact_info = data.split(" ")
    phoneboook[contact_info[0]] = contact_info[1]
    return f"Phonenumber for {contact_info[0]} changed to {contact_info[1]}"

@input_error
def show_all(data):
    result = ""
    for name in phoneboook:
        result = result + f"Name: {name}, phone {phoneboook[name]} \n"
    if len(result) == 0:
        result = "Phonebook is empty"
    return result


def exit(data):
    return "exit"

@input_error
def add(data: str):
    result = data.split(" ")
    phoneboook.update({result[0]: result[1]})
    return f"Contact {result[0]} with the phone number {result[1]} added to phonebook"

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