"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from src.domain.entity import Book, BookException
from src.services.service import test_init
import copy


def print_menu_options():
    print('Please choose one of the following:')
    print('1. Add a book')
    print('2. Display the list of books')
    print('3. Filter the list so that book titles starting with a given word are deleted from the list')
    print('4. Undo')
    print('0. Exit')


def print_books_list(list_of_books):
    list_of_books = list_of_books.get_books_list()
    for a_book in list_of_books:
        print("The book " + a_book.title + " written by " + a_book.author + " has the ISBN: " + a_book.isbn)


def start_menu():
    list_of_books = test_init()
    history_list = [copy.deepcopy(list_of_books)]
    are_we_done_yet = False
    while not are_we_done_yet:
        try:
            print_menu_options()
            command_word = input('Please enter your command: ')
            if command_word == '1':
                new_book = Book(input('Please enter the ISBN: '), input('Please enter the name of the author: '), input('Please enter the title of the book: '))
                list_of_books.add_book_to_list(new_book)
                history_list.append(copy.deepcopy(list_of_books))
            elif command_word == '2':
                print_books_list(list_of_books)
            elif command_word == '3':
                given_word = input('Please enter the word for the filter operation: ')
                list_of_books.filter_book_title(given_word)
                history_list.append(copy.deepcopy(list_of_books))
            elif command_word == '4':
                if len(history_list) == 1:
                    print('There are no operation to be undone!')
                else:
                    history_list.pop(len(history_list)-1)
                    list_of_books = copy.deepcopy(history_list[-1])
            elif command_word == '0':
                are_we_done_yet = True
                print('Bye bye! See you next time!')
            else:
                print('Invalid command!')
        except BookException as be:
            print(be)


start_menu()
