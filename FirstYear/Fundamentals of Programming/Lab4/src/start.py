"""
Assemble the program and start the user interface here
"""


from src.functions.functions import *
from src.ui.console import greeting_function, help_with_commands, split_user_command


def start_menu_ui():
    bank_transaction_list_on_days = [[]]*31  # the list which will contain all the transactions for this month
    test_init(bank_transaction_list_on_days)  # adding to the list 10 transactions
    intermediary_list = [[]]*31
    test_init(intermediary_list)
    history_transactions_list = [intermediary_list]
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
                if command_word == 'undo':
                    if len(history_transactions_list) == 1:
                        raise ValueError("You don't have any operations to undo!")
                    else:
                        history_transactions_list.pop(len(history_transactions_list)-1)
                        bank_transaction_list_on_days = history_transactions_list[len(history_transactions_list)-1].copy()
                elif command_word == 'sum':
                    print('The sum of all', parameters, 'transactions is =', calculate_sum_of_type_transactions(bank_transaction_list_on_days, parameters), 'RON')
                elif command_word == 'max':
                    maximum_amount = maximum_of_type_transaction_on_given_day(bank_transaction_list_on_days, parameters)
                    if maximum_amount == -1:
                        print('There were no transactions matching the requested type during that day!')
                    else:
                        print('The maximum amount processed during the requested day and having the requested type is =', maximum_amount, 'RON')
                elif command_word == 'filter':
                    filter_transactions_list(history_transactions_list, bank_transaction_list_on_days, parameters)
                elif command_word not in command_dict:
                    raise ValueError('Invalid command!')
                else:
                    command_dict[command_word](history_transactions_list, bank_transaction_list_on_days, parameters)

        except ValueError as ve:
            print(ve)


start_menu_ui()
