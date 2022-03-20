"""
This is the user interface module. These functions call functions from the domain and functions module.
"""


def strip_tokens_list(list_of_parameters):
    """
    This function will remove all de additional spaces from each parameter in list_of_parameters
    return: -
    """
    for i in range(0, len(list_of_parameters)):
        list_of_parameters[i] = list_of_parameters[i].strip()


def split_user_command(user_command):
    """
    This function will split the user command into command_word = tokens[0], parameters = tokens[1] which will be assigned in start_menu_ui()
    return: command_word, parameters (if possible)
    """
    tokens = user_command.strip().split(' ', 1)
    tokens[0] = tokens[0].strip().lower()
    return tokens[0], '' if len(tokens) == 1 else tokens[1].strip()


def greeting_function():
    print('Welcome to your banking app, John!  If you need more information about the commands you may use, please type: help!')


def help_with_commands():
    print('You have the following commands available at the moment! ')
    print(' - add <value> <type> <description>    which will add, for example, to the current day an out transaction of 100 RON with the "pizza" description ')
    print(' - insert <day> <value> <type> <description>    which will insert, for example, to day 25 an in transaction of 100 RON with the “salary” description ')
    print(' - remove <day>    which will remove, for example, all transactions from day 15 ')
    print(' - remove <start day> to <end day>    which will remove, for example, remove 5 to 10 – remove all transactions between days 5 and 10 ')
    print(' - replace <day> <type> <description> with <value>    which will replace, for example, the amount for the in transaction having the “salary” description from day 12 with 2000 RON ')
    print(' - list    which will display all transactions  ')
    print(' - list <type>    which will display, for example, all in transactions ')
    print(' - list [ < | = | > ] <value>    which will display, for example, display all transactions having an amount of money >100')
    print(' - list balance <day>    which will compute the account’s balance at the end of day 10. This is the sum of all in transactions, from which we subtract out transactions occurring before or on day 10 and then print the value ')
    print(' - sum <type>    which will display the total amount from transactions matching the specified type')
    print(' - max <type> <day>    which will display the maximum amount from transactions matching the specified type and day')
    print(' - filter <type>    which will keep only the transactions matching the specified type')
    print(' - filter <type> <value>    which will keep only the transactions matching the specified type and with an amount smaller than value')
    print(' - undo    which will reverse the last operation that modified the program data, if possible')
    print(' - exit    which will exit the program')
    print('Requirements for parameters! ')
    print(' ~ value must be a positive integer ')
    print(' ~ type must be either in or out ')
    print(' ~ description can be whatever you want, it is your money after all')
    print(' ~ day, start day, end day must be a natural number from [0,30], and start day < end day')


def test_strip_tokens_list():
    """
    Test function for strip_tokens_list()
    """
    testing_list = ['   add', '  qwerty   ']
    strip_tokens_list(testing_list)
    assert testing_list == ['add', 'qwerty']


test_strip_tokens_list()


def test_split_user_command():
    """
    Test for split_user_command()
    """
    command, parameters = split_user_command('   aDD   testing parameter   ')
    assert command == 'add'
    assert parameters == 'testing parameter'


test_split_user_command()
