from os import system, name
class Functions:
    @staticmethod
    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
