"""
Functions that implement program features. They should call each other, or other functions from the domain
"""


from datetime import date
from src.ui.console import strip_tokens_list
from src.domain.entity import get_transaction_type, get_transaction_description, get_transferred_amount, list_of_transaction_strings


def add_new_bank_transaction(history_transactions_list, bank_transaction_list_on_days, parameters):
    """
    Function adds the new transaction in the bank_transaction_list_on_days in the list on the position = current_day
    bank_transaction_list_on_days - the list which contains all the transactions from the current month
    history_transactions_list - list of all previous versions of bank_transaction_list_on_days
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
    history_transactions_list.append([])
    history_transactions_list[len(history_transactions_list) - 1] = bank_transaction_list_on_days.copy()


def insert_new_bank_transaction(history_transactions_list, bank_transaction_list_on_days, parameters):
    """
    This function inserts a new transaction in the transactions list from a given day
    bank_transaction_list_on_days - the list which contains all the transactions from the current month
    history_transactions_list - list of all previous versions of bank_transaction_list_on_days
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
    history_transactions_list.append([])
    history_transactions_list[len(history_transactions_list) - 1] = bank_transaction_list_on_days.copy()


def replace_transaction_amount(history_transactions_list, bank_transaction_list_on_days, parameters):
    """
    The function will replace a transaction (if its only 1 match or all of the matching transactions) from a given day, which matches the specified type and description
    bank_transaction_list_on_days - the list which contains all the transactions from the current month
    history_transactions_list - list of all previous versions of bank_transaction_list_on_days
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
            else:
                history_transactions_list.append([])
                history_transactions_list[len(history_transactions_list) - 1] = bank_transaction_list_on_days.copy()


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


def remove_from_bank_transactions(history_transactions_list, bank_transaction_list_on_days, parameters):
    """
    The functions will remove transactions from the list with all the transactions of the month according to one of the following:
    parameters: can be day / type / start_day to end_day
    bank_transaction_list_on_days - the list which contains all the transactions from the current month
    history_transactions_list - list of all previous versions of bank_transaction_list_on_days
    return: -
    """
    any_modification_made = False
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
                if len(bank_transaction_list_on_days[int(current_day)]) != 0:
                    any_modification_made = True
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
                if len(bank_transaction_list_on_days[i]) != len(intermediary_list):
                    any_modification_made = True
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
                if len(bank_transaction_list_on_days[i]) != 0:
                    any_modification_made = True
                bank_transaction_list_on_days[i] = []
    if any_modification_made is True:
        history_transactions_list.append([])
        history_transactions_list[len(history_transactions_list) - 1] = bank_transaction_list_on_days.copy()
    else:
        raise ValueError('There were no transactions removed!')


def calculate_sum_of_type_transactions(bank_transaction_list_on_days, parameters):
    """
    This function will calculate the sum of all transactions matching the type in parameters
    :param bank_transaction_list_on_days: the list which contains all the transactions from the current month
    :param parameters: type, where type can be either in or out
    :return: the sum of all transactions matching the type in parameters
    """
    sum_of_type_transactions = 0
    transaction_types = ['in', 'out']
    parameters.strip(' ')
    if ' ' in parameters:
        raise ValueError('Invalid command! Wrong number of parameters!')
    else:
        transaction_type = parameters
        if transaction_type not in transaction_types:
            raise ValueError('Invalid parameter! Transaction type must be either in or out!')
        else:
            for i in range(0, 31):
                intermediary_list = bank_transaction_list_on_days[i].copy()
                for j in range(0, len(intermediary_list)):
                    if transaction_type == get_transaction_type(intermediary_list[j]):
                        sum_of_type_transactions = sum_of_type_transactions + int(get_transferred_amount(intermediary_list[j]))
    return sum_of_type_transactions


def maximum_of_type_transaction_on_given_day(bank_transaction_list_on_days, parameters):
    """
    The function will return the maximum amount processed by a transaction with its type matching the type in parameters
    :param bank_transaction_list_on_days: the list which contains all the transactions from the current month
    :param parameters: type day; type can be either in or out, day must be an integer btw 0 and 30
    :return: the maximum amount processed by a matching transaction or -1 if there were no type transactions during
    the given day
    """
    parameters.strip(' ')
    maximum_transaction_amount = -1
    transaction_types = ['in', 'out']
    tokens = parameters.split(' ')
    if len(tokens) != 2:
        raise ValueError('Invalid command! Wrong number of parameters!')
    else:
        strip_tokens_list(tokens)
        transaction_type = tokens[0]
        transaction_day = tokens[1]
        if not transaction_day.isalnum() or int(transaction_day) not in range(0, 31):
            raise ValueError('Invalid parameters! Transaction day must be an integer between 0 and 30')
        if transaction_type not in transaction_types:
            raise ValueError('Invalid parameters! Transaction type must be either in or our!')
        for i in range(0, len(bank_transaction_list_on_days[int(transaction_day)])):
            processed_amount = int(get_transferred_amount(bank_transaction_list_on_days[int(transaction_day)][i]))
            if processed_amount > maximum_transaction_amount:
                maximum_transaction_amount = processed_amount
    return maximum_transaction_amount


def filter_transactions_list_for_type(history_transactions_list, bank_transaction_list_on_days, parameters):
    """
    This function filters the list of all transactions, in such way that it will contain only the transactions having matching type with the type in parameters
    :param bank_transaction_list_on_days: list of all previous versions of bank_transaction_list_on_days
    :param history_transactions_list: list of all previous versions of bank_transaction_list_on_days
    :param parameters: type, which must be either in or out
    :return: -
    """
    any_modifications_made = False
    transaction_types = ['in', 'out']
    parameters.strip(' ')
    transaction_type = parameters
    if transaction_type not in transaction_types:
        raise ValueError('Invalid parameter! Transaction type must be either in or out!')
    else:
        for i in range(0, 31):
            intermediary_list = []  # necessary list to modify the list containing all the transactions of the month
            for j in range(0, len(bank_transaction_list_on_days[i])):
                if get_transaction_type(bank_transaction_list_on_days[i][j]) == transaction_type:
                    intermediary_list.append(bank_transaction_list_on_days[i][j])
            if len(bank_transaction_list_on_days[i]) != len(intermediary_list):
                any_modifications_made = True
            bank_transaction_list_on_days[i] = intermediary_list.copy()
    if any_modifications_made:
        history_transactions_list.append([])
        history_transactions_list[len(history_transactions_list) - 1] = bank_transaction_list_on_days.copy()
    else:
        raise ValueError('No modifications were made!')


def filter_transactions_list_for_type_and_value(history_transactions_list, bank_transaction_list_on_days, parameters):
    """
    This function will filter bank_transaction_list according to the type and value in parameters
    :param history_transactions_list: list of all previous versions of bank_transaction_list_on_days
    :param bank_transaction_list_on_days: list of all previous versions of bank_transaction_list_on_days
    :param parameters: type and value, type must be either in or out, value must be a positive integer
    :return:
    """
    any_modifications_made = False
    transaction_types = ['in', 'out']
    tokens = parameters.split(' ')
    transaction_type = tokens[0]
    amount_for_comparison = int(tokens[1])
    if transaction_type not in transaction_types:
        raise ValueError('Invalid parameter! Transaction type must be either in or out!')
    for i in range(0, 31):
        intermediary_list = []  # necessary list to modify the list containing all the transactions of the month
        for j in range(0, len(bank_transaction_list_on_days[i])):
            if get_transaction_type(bank_transaction_list_on_days[i][j]) == transaction_type and int(get_transferred_amount(bank_transaction_list_on_days[i][j])) < amount_for_comparison:
                intermediary_list.append(bank_transaction_list_on_days[i][j])
        if len(bank_transaction_list_on_days[i]) != len(intermediary_list):
            any_modifications_made = True
        bank_transaction_list_on_days[i] = intermediary_list.copy()
    if any_modifications_made:
        history_transactions_list.append([])
        history_transactions_list[len(history_transactions_list) - 1] = bank_transaction_list_on_days.copy()
    else:
        raise ValueError('No modifications were made!')


def filter_transactions_list(history_transaction_list, bank_transaction_list_on_days, parameters):
    """
    This function will filter bank_transaction_list_on_days according to the content of parameters
    :param history_transaction_list: list of all previous versions of bank_transaction_list_on_days
    :param bank_transaction_list_on_days: list of all previous versions of bank_transaction_list_on_days
    :param parameters: either type or type value; type must be either in or out, value must be an integer > 0
    :return:
    """
    parameters.strip(' ')
    tokens = parameters.split(' ', 2)
    transaction_type = tokens[0]
    strip_tokens_list(tokens)
    if len(tokens) == 1:
        filter_transactions_list_for_type(history_transaction_list, bank_transaction_list_on_days, transaction_type)
    elif not tokens[1].isalnum():
        raise ValueError('Invalid parameter! The value must be a positive integer!')
    else:
        amount_for_comparison = tokens[1]
        filter_transactions_list_for_type_and_value(history_transaction_list, bank_transaction_list_on_days, transaction_type+' '+amount_for_comparison)


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
            print('Good job! Until this day of the month, you earned', balance_until_day, 'RON!')
        elif balance_until_day < 0:
            print('You are not doing great pal... You lost', -int(balance_until_day), 'RON so far, and the month is not even over. You gotta get some money management lessons asap!')
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


# TESTS STARTING HERE ! ! !


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


def test_filter_transactions_list_for_type():
    testing_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    test_init(testing_list)
    filter_transactions_list_for_type([], testing_list, 'in')
    assert testing_list == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '4000', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'recovered_debt'}], [], [], [], [], [], [], [], [], []]


test_filter_transactions_list_for_type()


def test_filter_transactions_list_for_type_and_value():
    testing_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    test_init(testing_list)
    filter_transactions_list_for_type_and_value([], testing_list, 'in 5000')
    assert testing_list == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '4000', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'recovered_debt'}], [], [], [], [], [], [], [], [], []]
    filter_transactions_list_for_type_and_value([], testing_list, 'in 101')
    assert testing_list == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'recovered_debt'}], [], [], [], [], [], [], [], [], []]


test_filter_transactions_list_for_type_and_value()


def test_maximum_type_transaction_on_given_day():
    testing_list = [[]]*31
    test_init(testing_list)
    assert maximum_of_type_transaction_on_given_day(testing_list, 'in 19') == 4000
    assert maximum_of_type_transaction_on_given_day(testing_list, 'out 23') == 1000


test_maximum_type_transaction_on_given_day()


def test_calculate_sum_of_type_transactions():
    testing_list = [[]]*31
    test_init(testing_list)
    assert calculate_sum_of_type_transactions(testing_list, 'out') == 2410
    assert calculate_sum_of_type_transactions(testing_list, 'in') == 4100


test_calculate_sum_of_type_transactions()


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


def test_add_new_bank_transaction():
    """
    Test function for add_new_bank_transaction()
    """
    # Because I used a function to take the current day, the test will be relevant only on the 20th of the month
    testing_list_to_add = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    add_new_bank_transaction([], testing_list_to_add, '12 in salary')
    # assert testing_list_to_add == [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[{'transferred_amount': '12', 'transaction_type': 'in', 'transaction_description': 'salary'}]]
    assert testing_list_to_add == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'transferred_amount': '12', 'transaction_type': 'in', 'transaction_description': 'salary'}]]
# test_add_new_bank_transaction()


def test_insert_new_bank_transaction():
    """
    Test function for insert_new_bank_transaction()
    """
    testing_list_to_insert = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    insert_new_bank_transaction([], testing_list_to_insert, '2 100 in salary')
    assert testing_list_to_insert == [[], [], [{'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_insert = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    insert_new_bank_transaction([], testing_list_to_insert, '0 100 in salary')
    assert testing_list_to_insert == [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


test_insert_new_bank_transaction()


def test_replace_transaction_amount():
    """
    Test function for replace_transaction_amount()
    """
    testing_list_to_replace = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    replace_transaction_amount([], testing_list_to_replace, '0 out food with 200')
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


def test_remove_from_bank_transactions():
    """
    Test function for remove_from_bank_transactions()
    """
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([], [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0')
    assert testing_list_to_remove == [[], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([], [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0 to 6')
    assert testing_list_to_remove == [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([], [[], [{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0')
    assert testing_list_to_remove == [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    testing_list_to_remove = [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    remove_from_bank_transactions([], [[{'transferred_amount': '320', 'transaction_type': 'out', 'transaction_description': 'food'}, {'transferred_amount': '100', 'transaction_type': 'in', 'transaction_description': 'salary'}], [], [], [], [{'transferred_amount': '75', 'transaction_type': 'out', 'transaction_description': 'movies'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], '0')
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
