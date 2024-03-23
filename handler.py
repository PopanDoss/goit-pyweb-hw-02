import metd
from functools import wraps
import pickle

book = metd.AddressBook()

#Створюємо декоратор для обробки помилок 
def input_error(func) :
    def inner(*args, **kwargs) :
        try :
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the correct argument for the command"
        except KeyError :
            return  "Name is Not Found"
        except IndexError :
            return "Enter the argument for the command"
    return inner


#функція, що зчитує команду та значення
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



#функція, що додає новий запис в список 
@input_error
def add_contact(args):

    name, phone = args
    if name not in book :
        record = metd.Record(name)
        record.add_phone(phone)
        book.add_record(record)
        massage = "Contact added."
        return massage
    else :
        massage = "Contact already exists"
        return massage

#Функція, що змінює номер 
@input_error
def  change_contact(args):
    name, phone = args
    record = book.find(name)

    if record:
        oldphone = record.phones[0].value
        record.edit_phone(oldphone, phone)
        massage =  f"Phone {oldphone} changed to {phone}" 
        return massage
    else:
        massage = f"Contact {name} not found"
        return massage

#Функція, що відображає телефон  
@input_error
def show_phone(args) :
    name = args[0] 
    record = book.find(name)

    if record :    
        result = ', '.join(map(str, record.phones))
        massage = f"Contact {name} phone {result}"
        return massage
    else:
        massage = f"Contact {name} not found"
        return massage

#Функція,що відображає всі записи
@input_error
def show_all(book): 
        return book.__str__() 
    
#Функція, що додає дні народження 
@input_error
def add_birthday(args):
    name = args[0]
    bdays = args[1]
    record = book.find(name)

    if record :
        record.add_birthday(bdays)
        message = "Birthday added"
        return message
    else:
        message = f"Contact {name} not found"
        return message

#Функція, що показує день народження
@input_error
def show_birthday(args):
    name = args[0] 
    record = book.find(name)

    if record:
        if record.birthday:
            bday = record.birthday.value.strftime("%d.%m.%Y")
            message =  f"Contact name: {name}, birthday: {bday}"    
            return message
        else :
            message = f" Contact {name} birthday not found"
            return message
    else:
        message = f"Contact {name} not found"
        return message

#Функція, що виводить всі дні народження 
@input_error
def birthdays():
    message = book.get_upcoming_birthdays()
    return message


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)   

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            loaded_data = pickle.load(file)
            return metd.AddressBook(loaded_data)
    except FileNotFoundError:
        return metd.AddressBook()  

class Context_Manager:

    def handle_context(command, *args ):    

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            massage = add_contact(args)
            return massage
        elif command == "change":
            massage = change_contact(args)
            return massage
        elif command == "phone" :
            massage = show_phone(args)
            return massage
        elif command == "all" :
            massage = show_all(book)
            return massage
        elif command == "add-birthday" :
            massage = add_birthday(args)
            return massage
        elif command == "show-birthday":
            massage = show_birthday(args)
            return massage
        elif command == "birthdays":
            massage = birthdays()
            return massage
        else:
            massage = ("Invalid command.")
            return massage
