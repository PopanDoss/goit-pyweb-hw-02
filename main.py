import handler 
from abc import ABC, abstractmethod

class AbstractVeiw(ABC):
    @abstractmethod
    def interface_massage(self, massage):
        pass

    @abstractmethod
    def get_input(self):
        pass

class ConsoleVeiw(AbstractVeiw):
    def interface_massage(self, massage):
        print(massage)

    def get_input(self):
        return input("Enter a command: ")

    
class Application:
    def __init__(self, display):
        self.display = display

    def start(self) :
        self.display.interface_massage("Welcome to the assistant bot!")
        
        handler.book = handler.load_data()

        while True:
            user_input = self.display.get_input()
            command, *args = handler.parse_input(user_input)

            if command in ["close", "exit"]:

                handler.save_data(handler.book)
                print("Good bye!")
                break

            else:
                self.display.interface_massage(handler.Context_Manager.handle_context(command, *args))         
    
def main():
    display = ConsoleVeiw()
    app = Application(display)
    app.start()

if __name__ == "__main__":
    
    main()