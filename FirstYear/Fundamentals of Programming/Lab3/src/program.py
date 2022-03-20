#
# Write the implementation for A3 in this file
#

"""4. Bank Account

John wants to manage his bank account. To do this, he needs an application to store all the bank transactions performed on his account 
during a month. Each transaction is stored in the application using the following elements: day (of the month in which the transaction was 
made, between 0 and 30 for simplicity), amount of money (transferred, positive integer), type (in - into the account, out – from the account)
, and description. Write a program that implements the functionalities exemplified below:

(A) Add transaction
add <value> <type> <description>
insert <day> <value> <type> <description>
e.g.
add 100 out pizza – add to the current day an out transaction of 100 RON with the "pizza" description
insert 25 100 in salary – insert to day 25 an in transaction of 100 RON with the “salary” description

(B) Modify transactions
remove <day>
remove <start day> to <end day>
remove <type>
replace <day> <type> <description> with <value>
e.g.
remove 15 – remove all transactions from day 15
remove 5 to 10 – remove all transactions between days 5 and 10
remove in – remove all in transactions
replace 12 in salary with 2000 – replace the amount for the in transaction having the “salary” description from day 12 with 2000 RON

(C) Display transactions having different properties
list
list <type>
list [ < | = | > ] <value>
list balance <day>
e.g.
list – display all transactions
list in – display all in transactions
list > 100 - display all transactions having an amount of money >100
list = 67 - display all transactions having an amount of money =67
list balance 10 – compute the account’s balance at the end of day 10. This is the sum of all in transactions, from which we subtract out 
transactions occurring before or on day 10
"""

#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)

from datetime import date


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


def get_transferred_amount(dictionary_in_transaction_list):
    """
    This function gets the transferred amount from the dictionary containing the transaction details
    dictionary_in_transaction_list: the transaction in a dictionary
    return: the transferred amount in the transaction in dictionary_in_transaction_list
    """
    return dictionary_in_transaction_list['transferred_amount']


def get_transaction_type(dictionary_in_transaction_list):
    """
    This function gets the transaction type from the dictionary containing the transaction details
    dictionary_in_transaction_list: the transaction in a dictionary
    return: the type of the transaction in dictionary_in_transaction_list
    """
    return dictionary_in_transaction_list['transaction_type']


def get_transaction_description(dictionary_in_transaction_list):
    """
    This function gets the transaction description from the dictionary containing the transaction details
    dictionary_in_transaction_list: the transaction in a dictionary
    return: the description of the transaction in dictionary_in_transaction_list
    """
    return dictionary_in_transaction_list['transaction_description']


def from_dictionary_in_a_string(dictionary_in_transaction_list):
    """
    This function coverts and returns the content of a dictionary containing transaction details in a string
    dictionary_in_transaction_list: one of the transaction made during a certain day = index of the list;  
    return:  the transaction in a form of a string
        - example {'transferred_amount': '250', 'transaction_type': 'out', 'transaction_description': 'gas'} -> '250 withdrawal for gas'
    """
    transferred_amount = get_transferred_amount(dictionary_in_transaction_list)
    string_for_transaction = transferred_amount
    transaction_type = get_transaction_type(dictionary_in_transaction_list)
    if transaction_type == 'out':
        string_for_transaction = string_for_transaction + ' ' + 'withdrawal for '
    else:
        string_for_transaction = string_for_transaction + ' ' + 'deposit from '
    transaction_type = get_transaction_description(dictionary_in_transaction_list)
    string_for_transaction = string_for_transaction + transaction_type
    return string_for_transaction


def list_of_transaction_strings(bank_transaction_list_for_a_day):
    """
    This functions returns a list of strings containing the transaction from a certain day  
    bank_transaction_list_for_a_day: the list of all the transactions on the day    
    example: [{'transferred_amount': '250', 'transaction_type': 'out', 'transaction_description': 'gas'},{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}]   
    => ['250 withdrawal for gas', '320 withdrawal for food']
    """
    list_transactions_in_string = []
    for i in range(0, len(bank_transaction_list_for_a_day)):
        list_transactions_in_string.append(from_dictionary_in_a_string(bank_transaction_list_for_a_day[i]))
    return list_transactions_in_string


def add_new_bank_transaction(bank_transaction_list_on_days, parameters):
    """
    Function adds the new transaction in the bank_transaction_list_on_days in the list on the position = current_day
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    parameters 'value type description'     
    returns:-
    """
    transaction_types = ['in', 'out']
    today = date.today()  # takes current date
    today_date = today.strftime("%d/%m/%y")  # reformatting the current date
    tokens = today_date.split('/', 1)
    current_day = tokens[0]
    tokens = parameters.split(' ', 2)  # tokens[0] = value; tokens[1] = type(in or out); tokens[2] = description
    strip_tokens_list(tokens)
    transferred_amount, transaction_type, transaction_description = tokens
    if transferred_amount.isalnum() is not True or int(transferred_amount) < 0:
        raise ValueError('Invalid parameter! Value must be a positive number!')
    if transaction_type not in transaction_types:
        raise ValueError('Invalid parameter, transaction type must be in or out!')
    intermediary_list = bank_transaction_list_on_days[int(current_day)].copy()
    intermediary_list.append({'transferred_amount': transferred_amount, 'transaction_type': transaction_type, 'transaction_description': transaction_description})
    bank_transaction_list_on_days[int(current_day)] = intermediary_list.copy()


def insert_new_bank_transaction(bank_transaction_list_on_days, parameters):
    """
    This function inserts a new transaction in the transactions list from a given day   
    bank_transaction_list_on_days - the list which contains all the transactions from the current month
    parameters : day value type description
    """
    transaction_types = ['in', 'out']
    tokens = parameters.split(' ', 3)  # tokens[0] = day; tokens[1] = value; tokens[2] = type(in or out); tokens[3] = description
    strip_tokens_list(tokens)
    current_transaction_day, transferred_amount, transaction_type, transaction_description = tokens
    if current_transaction_day.isalnum() is not True or int(current_transaction_day)not in range(0, 31):
        raise ValueError('Invalid parameter! Day must be a natural number between 0 and 30!')
    if transferred_amount.isalnum() is not True or int(tokens[1]) < 0:
        raise ValueError('Invalid parameter! Value must be a positive number!')
    if transaction_type not in transaction_types:
        raise ValueError('Invalid parameter! Transaction type must be either in or out!')
    intermediary_list = bank_transaction_list_on_days[int(current_transaction_day)].copy()
    intermediary_list.append({'transferred_amount': transferred_amount, 'transaction_type': transaction_type, 'transaction_description': transaction_description})
    bank_transaction_list_on_days[int(current_transaction_day)] = intermediary_list.copy()


def replace_transaction_amount(bank_transaction_list_on_days, parameters):
    """
    The function will replace a transaction (if its only 1 match or all of the matching transactions) from a given day, which matches the specified type and description   
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    parameters: day type description with value; example parameters ='12 in salary with 2000'
    """
    check_if_replace = False  # checking if there are any replacements made, therefore if a listing is necessary
    transaction_types_list = ['in', 'out']
    tokens = parameters.split(' ')  # tokens[0] = day; tokens[1] = transaction type; tokens[2] = transaction description; tokens[4] = new transaction value
    strip_tokens_list(tokens)
    if len(tokens) != 5:
        raise ValueError('Invalid command! Wrong parameters number!')
    else:
        current_day_in_transaction_list = tokens[0]
        transaction_type = tokens[1]
        transaction_description = tokens[2]
        new_bank_transaction_value = tokens[4]
        if current_day_in_transaction_list.isalnum() is not True or int(current_day_in_transaction_list)not in range(0, 31):
            raise ValueError('Invalid parameter! Day must be a natural number between 0 and 30!')
        if new_bank_transaction_value.isalnum() is not True or int(new_bank_transaction_value) < 0:
            raise ValueError('Invalid parameter! Value must be a positive number!')
        if transaction_type not in transaction_types_list:
            raise ValueError('Invalid parameter! Transaction type must be either in or out!')
        if len(bank_transaction_list_on_days[int(current_day_in_transaction_list)]) == 0:
            raise ValueError('There are no transactions on this day !')
        else:
            intermediary_list = bank_transaction_list_on_days[int(current_day_in_transaction_list)].copy()
            for i in range(0, len(intermediary_list)):
                if transaction_type == get_transaction_type(intermediary_list[i]) and transaction_description == get_transaction_description(intermediary_list[i]):  # checking if matching specifications
                    intermediary_list[i] = {'transferred_amount': new_bank_transaction_value, 'transaction_type': transaction_type, 'transaction_description': transaction_description}  # replacing transaction
                    check_if_replace = True
            bank_transaction_list_on_days[int(current_day_in_transaction_list)] = intermediary_list.copy()
            if not check_if_replace:
                raise ValueError('There were no replacements to be made!')


def create_particular_bank_transactions_list_for_type(bank_transaction_list_on_days, new_bank_transaction_list, transaction_type):
    """
    This function will modify the empty list stored in new_bank_transaction_list such that, in the end, it will contain only the transactions which have the same transaction type as transaction_type  
    bank_transaction_list_on_days : the list with all the transactions
    return: - 
    """
    for i in range(0, len(bank_transaction_list_on_days)):
        if len(bank_transaction_list_on_days) > 0:
            intermediary_list = []  # necessary list to modify the list containing all the transactions of the month
            for j in range(0, len(bank_transaction_list_on_days[i])):
                if get_transaction_type(bank_transaction_list_on_days[i][j]) == transaction_type:  # add if matching transaction types
                    intermediary_list.append(bank_transaction_list_on_days[i][j])
            new_bank_transaction_list[i] = intermediary_list.copy()


def create_particular_bank_transaction_list_for_amount_lower(bank_transaction_list_on_days, new_bank_transaction_list, transferred_amount_comparison):
    """
    This function will modify the empty list stored in new_bank_transaction_list such that, in the end, it will contain only the transactions which have the transferred amount is lower than transferred_amount_comparison   
    bank_transaction_list_on_days : the list with all the transactions
    return: - 
    """
    for i in range(0, len(bank_transaction_list_on_days)):
        if len(bank_transaction_list_on_days[i]) > 0:
            intermediary_list = []  # necessary list to modify the list containing all the transactions of the month
            for j in range(0, len(bank_transaction_list_on_days[i])):
                transactions_list_on_day_i = bank_transaction_list_on_days[i].copy()
                if int(get_transferred_amount(transactions_list_on_day_i[j])) < int(transferred_amount_comparison):  # add if lower than amount
                    intermediary_list.append(transactions_list_on_day_i[j])
            new_bank_transaction_list[i] = intermediary_list.copy()


def create_particular_bank_transaction_list_for_amount_equal(bank_transaction_list_on_days, new_bank_transaction_list, transferred_amount_comparison):
    """
    This function will modify the empty list stored in new_bank_transaction_list such that, in the end, it will contain only the transactions which have the transferred amount is equal with transferred_amount_comparison   
    bank_transaction_list_on_days : the list with all the transactions
    return: - 
    """
    for i in range(0, len(bank_transaction_list_on_days)):
        if len(bank_transaction_list_on_days[i]) > 0:
            intermediary_list = []  # necessary list to modify the list containing all the transactions of the month
            for j in range(0, len(bank_transaction_list_on_days[i])):
                transactions_list_on_day_i = bank_transaction_list_on_days[i].copy()
                if int(get_transferred_amount(transactions_list_on_day_i[j])) == int(transferred_amount_comparison):  # add if equal than amount
                    intermediary_list.append(transactions_list_on_day_i[j])
            new_bank_transaction_list[i] = intermediary_list.copy()


def create_particular_bank_transaction_list_for_amount_greater(bank_transaction_list_on_days, new_bank_transaction_list, transferred_amount_comparison):
    """
    This function will modify the empty list stored in new_bank_transaction_list such that, in the end, it will contain only the transactions which have the transferred amount is greater than transferred_amount_comparison   
    bank_transaction_list_on_days : the list with all the transactions
    return: - 
    """
    for i in range(0, len(bank_transaction_list_on_days)):
        if len(bank_transaction_list_on_days[i]) > 0:
            intermediary_list = []  # necessary list to modify the list containing all the transactions of the month
            for j in range(0, len(bank_transaction_list_on_days[i])):
                transactions_list_on_day_i = bank_transaction_list_on_days[i].copy()
                if int(get_transferred_amount(transactions_list_on_day_i[j])) > int(transferred_amount_comparison):  # add if greater than amount
                    intermediary_list.append(transactions_list_on_day_i[j])
            new_bank_transaction_list[i] = intermediary_list.copy()


def create_particular_bank_transactions_list(bank_transaction_list_on_days, parameters):
    """
    This functions creates and returns a new bank transaction list which can be displayed without any additional tests
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    parameters: either type(in or out) or [ < | = | > ] value      
    returns: A new list according to the specified parameters  
    """
    new_bank_transaction_list = [[]]*31  # the new list which will be returned
    tokens = parameters.split(' ', 2)  # tokens[0] is either in|out or <|=|>, tokens[1] is the value(number)
    strip_tokens_list(tokens)
    if len(tokens) == 1:
        transaction_type_or_comparison_operand = tokens[0]
        if transaction_type_or_comparison_operand != 'in' and transaction_type_or_comparison_operand != 'out':  # differentiate between transaction type or <|=|>
            raise ValueError('Invalid parameter! Transaction type must be either in or out!')
        else:
            create_particular_bank_transactions_list_for_type(bank_transaction_list_on_days, new_bank_transaction_list, transaction_type_or_comparison_operand)
    elif len(tokens) == 3:
        raise ValueError('Invalid parameters!')
    else:
        transaction_type_or_comparison_operand, amount_to_compare_with = tokens
        if transaction_type_or_comparison_operand == '<':
            create_particular_bank_transaction_list_for_amount_lower(bank_transaction_list_on_days, new_bank_transaction_list, amount_to_compare_with)
        elif transaction_type_or_comparison_operand == '=':
            create_particular_bank_transaction_list_for_amount_equal(bank_transaction_list_on_days, new_bank_transaction_list, amount_to_compare_with)
        elif transaction_type_or_comparison_operand == '>':
            create_particular_bank_transaction_list_for_amount_greater(bank_transaction_list_on_days, new_bank_transaction_list, amount_to_compare_with)
    return new_bank_transaction_list


def calculate_transactions_type_in_until_day(bank_transaction_list_on_days, day):
    """
    This functions will calculate the amount processed in all in transactions until a given day of the month (including that day)
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    day - self explanatory  
    returns: the sum of in out transactions
    """
    transactions_sum = 0
    for i in range(0, int(day)+1):
        if len(bank_transaction_list_on_days[i]) > 0:
            for j in range(0, len(bank_transaction_list_on_days[i])):
                transactions_list_on_day = bank_transaction_list_on_days[i].copy()
                if get_transaction_type(transactions_list_on_day[j]) == 'in':
                    transactions_sum = int(get_transferred_amount(transactions_list_on_day[j])) + transactions_sum
    return transactions_sum


def calculate_transactions_type_out_until_day(bank_transaction_list_on_days, day):
    """
    This functions will calculate the amount processed in all out transactions until a given day of the month (including that day)
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    day - self explanatory  
    returns: the sum of all out transactions
    """
    transactions_sum = 0
    for i in range(0, int(day)+1):
        if len(bank_transaction_list_on_days[i]) > 0:
            for j in range(0, len(bank_transaction_list_on_days[i])):
                transactions_list_on_day = bank_transaction_list_on_days[i].copy()
                if get_transaction_type(transactions_list_on_day[j]) == 'out':
                    transactions_sum = int(get_transferred_amount(transactions_list_on_day[j])) + transactions_sum
    return transactions_sum


def remove_from_bank_transactions(bank_transaction_list_on_days, parameters):
    """
    The functions will remove transactions from the list with all the transactions of the month according to one of the following:
    parameters: can be day / type / start_day to end_day
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    return: -
    """
    transaction_type = ['in', 'out']
    tokens = parameters.split(' ', 3)   # tokens[0] can be either one of the elements in transaction_type, or a number ('5') representing either day or start day; tokens[1] = 'to'; tokens[2] = end day
    strip_tokens_list(tokens)
    if len(tokens) > 3 or len(tokens) == 0:
        raise ValueError('Invalid command! There are too many parameters!')
    elif len(tokens) == 1:
        transaction_type_or_day = tokens[0]
        if transaction_type_or_day.isalpha() is False:  # testing to differentiate between the commands which have only 1 parameter
            current_day = transaction_type_or_day
            if 0 <= int(current_day) <= 30:
                bank_transaction_list_on_days[int(current_day)] = []
            else:
                raise ValueError('Invalid parameter! Day must be a natural number between 0 and 30!')
        elif transaction_type_or_day not in transaction_type:
            raise ValueError('Invalid parameter! Transaction type must be either in or out!')
        else:
            transaction_type = transaction_type_or_day
            for i in range(0, 31):
                intermediary_list = []  # necessary list to modify the list containing all the transactions of the month
                for j in range(0, len(bank_transaction_list_on_days[i])):
                    if get_transaction_type(bank_transaction_list_on_days[i][j]) != transaction_type:
                        intermediary_list.append(bank_transaction_list_on_days[i][j])
                bank_transaction_list_on_days[i] = intermediary_list.copy()
    elif len(tokens) == 2:
        raise ValueError('Invalid command! The number of parameters is wrong!')
    else:
        start_day_for_remove = tokens[0]
        end_day_for_remove = tokens[2]
        if int(start_day_for_remove) > int(end_day_for_remove):
            raise ValueError('Invalid command! Start day must me smaller or equal to end day!')
        else:
            for i in range(int(start_day_for_remove), int(end_day_for_remove)+1):
                bank_transaction_list_on_days[i] = []


# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities


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
    print(' - exit    which will exit the program')
    print('Requirements for parameters! ')
    print(' ~ value must be a positive integer ')
    print(' ~ type must be either in or out ')
    print(' ~ description can be whatever you want, it is your money after all')
    print(' ~ day, start day, end day must be a natural number from [0,30], and start day < end day')


def print_list_balance_until_day(bank_transaction_list_on_days, parameters):
    """
    The list will print the difference between the sum of all in transactions and the sum of all out transactions until (and including) the day contained in parameters     
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    parameters a string containing a number Ex : '5'    
    """
    tokens = parameters.split(" ", 2)  # tokens[0] - the day until we calculate the sum of all in transactions and the sum of all out transactions
    strip_tokens_list(tokens)
    if len(tokens) != 2:  # check for valid input: Good input - '5'; Bad input - '5 day'
        raise ValueError('Invalid command! Wrong number of parameters!')
    else:
        balance_until_day = calculate_transactions_type_in_until_day(bank_transaction_list_on_days, tokens[1]) - calculate_transactions_type_out_until_day(bank_transaction_list_on_days, tokens[1])
        if balance_until_day > 0:
            print('Good job! Until this day of the month, you earned', balance_until_day, '!')
        elif balance_until_day < 0:
            print('You are not doing great pal... You lost', -int(balance_until_day), 'so far, and the month is not even over. You gotta get some money management lessons asap!')
        else:
            print('Not great, not terrible! You did not gain or lose any money so far!')


def just_list_bank_transactions(bank_transaction_list_on_days):
    """
    The function will display all transactions from the current month   
    bank_transaction_list_on_days - the list which contains all the transactions from the current month     
    return: -
    """
    at_least_one_print = False
    for i in range(0, 31):
        if len(bank_transaction_list_on_days[i]) > 0:
            print('Transactions on day '+str(i)+" : ", list_of_transaction_strings(bank_transaction_list_on_days[i]))
            at_least_one_print = True
    if at_least_one_print is False:
        print('There was nothing to print!')


def start_menu_ui():
    bank_transaction_list_on_days = [[]]*31  # the list which will contain all the transactions for this month
    test_init(bank_transaction_list_on_days)  # adding to the list 10 transactions
    command_dict = {'add': add_new_bank_transaction, 'insert': insert_new_bank_transaction, 'replace': replace_transaction_amount, 'remove': remove_from_bank_transactions}
    are_we_done_yet = False
    greeting_function()
    while not are_we_done_yet:
        try:
            user_command = input('command>')
            command_word, parameters = split_user_command(user_command)
            if command_word == 'exit':
                are_we_done_yet = True
                print('Bye bye! See you next time!')
            elif command_word == 'help!':
                help_with_commands()
            elif command_word == 'list':
                if 'balance' not in parameters:
                    if '<' not in parameters and '=' not in parameters and '>' not in parameters and 'in' not in parameters and 'out' not in parameters:
                        just_list_bank_transactions(bank_transaction_list_on_days)
                    else:
                        just_list_bank_transactions(create_particular_bank_transactions_list(bank_transaction_list_on_days, parameters))
                else:
                    print_list_balance_until_day(bank_transaction_list_on_days, parameters)
            else:
                if command_word not in command_dict:
                    raise ValueError('Invalid command!')
                else:
                    command_dict[command_word](bank_transaction_list_on_days, parameters)

        except ValueError as ve:
            print(ve)


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert


def test_init(test_list):
    # use this function to add the 10 required items
    # use it to set up test data
    test_list[0] = [{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}]
    test_list[1] = [{'transferred_amount': '350', 'transaction_type': 'out', 'transaction_description': 'shopping'}]
    test_list[3] = [{'transferred_amount': '250', 'transaction_type': 'out', 'transaction_description': 'gas'}]
    test_list[4] = [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}]
    test_list[6] = [{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}]
    test_list[17] = [{'transferred_amount': '20', 'transaction_type': 'out', 'transaction_description': 'snacks'}]
    test_list[19] = [{'transferred_amount': '4000', 'transaction_type': 'in', 'transaction_description': 'salary'}]
    test_list[21] = [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'recovered_debt'}]
    test_list[23] = [{'transferred_amount': '1000', 'transaction_type': 'out', 'transaction_description': 'car_repair'}]
    test_list[30] = [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'video_games'}]


def test_create_particular_bank_transactions_list_for_type():
    """
    Test function for create_particular_bank_transactions_list_for_type()
    """
    test_bank_transaction_list = [[]]*31
    test_init(test_bank_transaction_list)
    new_bank_transaction_list = [[]]*31
    create_particular_bank_transactions_list_for_type(test_bank_transaction_list, new_bank_transaction_list, 'in')
    assert new_bank_transaction_list == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '4000', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'recovered_debt'}], [], [], [], [], [], [], [], [], [], ]


test_create_particular_bank_transactions_list_for_type()


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


def test_from_dictionary_in_a_string():
    """
    Test function for test_from_dictionary_in_a_string()
    """
    test_dictionary_1 = {'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}
    assert from_dictionary_in_a_string(test_dictionary_1) == '75 withdrawal for movies'
    test_dictionary_2 = {'transferred_amount': '4000', 'transaction_type': 'in', 'transaction_description': 'salary'}
    assert from_dictionary_in_a_string(test_dictionary_2) == '4000 deposit from salary'


test_from_dictionary_in_a_string()


def test_list_of_transaction_string():
    """
    Test function for list_of_transaction_string()
    """
    test_list = list_of_transaction_strings([{'transferred_amount': '250', 'transaction_type': 'out', 'transaction_description': 'gas'}])
    assert test_list == ['250 withdrawal for gas']
    test_list = list_of_transaction_strings([{'transferred_amount': '250', 'transaction_type': 'out', 'transaction_description': 'gas'}, {'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}])
    assert test_list == ['250 withdrawal for gas', '320 withdrawal for food']


test_list_of_transaction_string()


def test_add_new_bank_transaction():
    """
    Test function for add_new_bank_transaction()
    """
    # Because I used a function to take the current day, the test will be relevant only on the 20th of the month
    testing_list_to_add = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    add_new_bank_transaction(testing_list_to_add, '12 in salary')
    # assert testing_list_to_add == [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[{'transferred_amount': '12', 'transaction_type': 'in', 'transaction_description': 'salary'}]]
    assert testing_list_to_add == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '12', 'transaction_type': 'in', 'transaction_description': 'salary'}]]
# test_add_new_bank_transaction()


def test_insert_new_bank_transaction():
    """
    Test function for insert_new_bank_transaction()
    """
    testing_list_to_insert = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    insert_new_bank_transaction(testing_list_to_insert, '2 100 in salary')
    assert testing_list_to_insert == [[], [], [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_insert = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    insert_new_bank_transaction(testing_list_to_insert, '0 100 in salary')
    assert testing_list_to_insert == [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


test_insert_new_bank_transaction()


def test_replace_transaction_amount():
    """
    Test function for replace_transaction_amount()
    """
    testing_list_to_replace = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    replace_transaction_amount(testing_list_to_replace, '0 out food with 200')
    assert testing_list_to_replace == [[{'transferred_amount': '200', 'transaction_type': 'out', 'transaction_description': 'food'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


test_replace_transaction_amount()


def test_create_particular_bank_transactions_list():
    """
    Test function for create_particular_bank_transactions_list()
    """
    testing_list_to_create = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_create = create_particular_bank_transactions_list([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '> 100')
    assert testing_list_to_create == [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ]
    testing_list_to_create = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_create = create_particular_bank_transactions_list([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], 'in')
    assert testing_list_to_create == [[{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_create = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_create = create_particular_bank_transactions_list([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], 'out')
    assert testing_list_to_create == [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


test_create_particular_bank_transactions_list()


def test_calculate_transactions_type_in_until_day():
    """
    Test function for calculate_transactions_type_in_until_day()calculate_transactions_type_in_until_day()
    """
    assert calculate_transactions_type_in_until_day([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '5') == 100


test_calculate_transactions_type_in_until_day()


def test_calculate_transactions_type_out_until_day():
    """
    Test function for calculate_transactions_type_out_until_day()
    """
    assert calculate_transactions_type_out_until_day([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '5') == 395


test_calculate_transactions_type_out_until_day()


# remove_from_bank_transactions()
def test_remove_from_bank_transactions():
    """
    Test function for remove_from_bank_transactions()
    """
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0')
    assert testing_list_to_remove == [[], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0 to 6')
    assert testing_list_to_remove == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0')
    assert testing_list_to_remove == [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0')
    assert testing_list_to_remove == [[], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


test_create_particular_bank_transactions_list()


def test_create_particular_bank_transaction_list_for_amount_equal():
    """
    Test function for create_particular_bank_transaction_list_for_amount_equal()
    """
    testing_list = [[]]*31
    test_init(testing_list)
    new_bank_transaction_list_test = [[]]*31
    create_particular_bank_transaction_list_for_amount_equal(testing_list, new_bank_transaction_list_test, '100')
    assert new_bank_transaction_list_test == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'recovered_debt'}], [], [], [], [], [], [], [], [], []]


test_create_particular_bank_transaction_list_for_amount_equal()


def test_create_particular_bank_transaction_list_for_amount_greater():
    """
    Test function for create_particular_bank_transaction_list_for_amount_greater()
    """
    testing_list = [[]]*31
    test_init(testing_list)
    new_bank_transaction_list_test = [[]]*31
    create_particular_bank_transaction_list_for_amount_greater(testing_list, new_bank_transaction_list_test, '1000')
    assert new_bank_transaction_list_test == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '4000', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [], [], [], [], [], [], [], []]


test_create_particular_bank_transaction_list_for_amount_greater()


def test_create_particular_bank_transaction_list_for_amount_lower():

    """
    Test function for create_particular_bank_transaction_list_for_amount_lower()
    """
    testing_list = [[]]*31
    test_init(testing_list)
    new_bank_transaction_list_test = [[]]*31
    create_particular_bank_transaction_list_for_amount_lower(testing_list, new_bank_transaction_list_test, '50')
    assert new_bank_transaction_list_test == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '20', 'transaction_type': 'out', 'transaction_description': 'snacks'}], [], [], [], [], [], [], [], [], [], [], [], [], []]


test_create_particular_bank_transaction_list_for_amount_lower()


start_menu_ui()

# TODO enjoy life
