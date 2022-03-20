"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


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
