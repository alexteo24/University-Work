from Controller import Controller
from Console import Console
if __name__ == '__main__':
    controller = Controller()
    console = Console(controller)
    console.start_program()
