"""
    Service class includes functionalities for implementing program features
"""
from src.domain.entity import Book, BookException
from random import choice


class ManageListBooks:

    def __init__(self):
        self._BooksList = []

    def get_books_list(self):
        """
        This function returns the list of the books
        :return: self._BooksList
        """
        return self._BooksList

    def __len__(self):
        """
        This functions returns the length of the list self._BooksList containing elements of class Book
        :return: the length of the list self._BooksList
        """
        return len(self._BooksList)

    def add_book_to_list(self, new_book):
        """
        This function will add, if possible, a new book to self._BookList
        :param new_book: the new book we want to add, having the format new_book = Book(isbn, author, title)
        :return: -
        """
        for a_book in self._BooksList:
            if new_book.isbn == a_book.isbn:
                raise BookException('There is already a book having that ISBN in the list!')
            if new_book.author == a_book.author and new_book.title == a_book.title:
                raise BookException('This book is already in the list!')
        self._BooksList.append(new_book)

    def filter_book_title(self, word_in_title):
        """
        This function will remove the books which will contain the word: word_in_title in their title
        :param word_in_title: the word which will determine which books will be removed
        :return: -
        """
        initial_length = len(self._BooksList)  # the initial length of the list, necessary to check if any modifications
        any_removed_books = True
        while any_removed_books:
            any_removed_books = False
            for a_book in self._BooksList:
                title_copy = a_book.title
                title_copy = title_copy.lower()
                if title_copy.find(word_in_title) == 0:
                    self._BooksList.remove(a_book)
                    any_removed_books = True
                elif ' '+word_in_title+' ' in title_copy:
                    self._BooksList.remove(a_book)
                    any_removed_books = True
                elif title_copy.find(word_in_title) == len(title_copy) - len(word_in_title):
                    self._BooksList.remove(a_book)
                    any_removed_books = True
            if initial_length == len(self._BooksList):
                raise BookException('There were no books to remove from the list!')


def test_init():
    """
    This 'test' function will generate the first 10 elements of the ._BooksList
    :return: test_list, which will be the first ._BooksList
    """
    test_list = ManageListBooks()
    list_isbns = ['978-4-4140-9666-8', '978-2-5316-7621-3', '978-7-5124-6274-8', '978-1-1102-5620-4',
                  '978-4-9276-3464-7', '978-3-6421-7960-0', '978-3-6402-6903-7', '978-6-8324-6183-7',
                  '978-4-9532-3076-9', '978-6-9213-6459-9']
    list_authors = []
    list_titles = []
    for i in range(0, 10):
        author_test = choice(['Thomas Edison', 'Bob Ross', 'Michael Myers', 'Gordon Ramsay', 'Usain Volt',
                              'Adolf Hitler', 'Napoleon Bonaparte', 'Vincent Van Gogh', 'Isaac Newton',
                              'Galileo Galilei', 'Humzah Blake', 'Tyriq Chambers', 'Phoenix Carpenter',
                              'Faisal Lyon', 'Layla-Rose Salter', 'Iona Merritt', 'Rayyan Benson', 'Tasha Melendez',
                              'Leoni Nash', 'Solomon Drew', 'Veronika Hutchinson', 'Ioana Nairn', 'Marni Lin'])
        while author_test in list_authors:
            author_test = choice(['Thomas Edison', 'Bob Ross', 'Michael Myers', 'Gordon Ramsay', 'Usain Volt',
                                  'Adolf Hitler', 'Napoleon Bonaparte', 'Vincent Van Gogh', 'Isaac Newton',
                                  'Galileo Galilei', 'Humzah Blake', 'Tyriq Chambers', 'Phoenix Carpenter',
                                  'Faisal Lyon', 'Layla-Rose Salter', 'Iona Merritt', 'Rayyan Benson', 'Tasha Melendez',
                                  'Leoni Nash', 'Solomon Drew', 'Veronika Hutchinson', 'Ioana Nairn', 'Marni Lin'])
        list_authors.append(author_test)
        title_test = choice(['The light at the end of the tunnel', 'Everyone needs a friend', 'You donkey',
                             'On the edge of the knife', 'Why Tesla was wrong', 'Mein Kampf', 'The life of a baguette',
                             'A quiet place', 'Cookin with apples', 'Straight architecture', 'Clue of the Concave Tuba',
                             'Court of the Rogue', 'The Blighted Needle', '2105: Turncoat', 'Abyss Falling',
                             'Case of the Filthy Boa', 'Primed for Sin', 'The Counterfeit Daffodil', '2132: Nirvana'])
        while title_test in list_titles:
            title_test = choice(['The light at the end of the tunnel', 'Everyone needs a friend', 'You donkey',
                                 'On the edge of the knife', 'Why Tesla was wrong', 'Mein Kampf',
                                 'The life of a baguette',
                                 'A quiet place', 'Cookin with apples', 'Straight architecture',
                                 'Clue of the Concave Tuba',
                                 'Court of the Rogue', 'The Blighted Needle', '2105: Turncoat', 'Abyss Falling',
                                 'Case of the Filthy Boa', 'Primed for Sin', 'The Counterfeit Daffodil',
                                 '2132: Nirvana'])
        list_titles.append(title_test)
        test_list.add_book_to_list(Book(list_isbns[i], author_test, title_test))

    # test_list.add_book_to_list(Book('353-54245-124-26', 'Thomas Edison', 'The light at the end of the tunnel'))
    # test_list.add_book_to_list(Book('6546-23325-6541', 'Bob Ross', 'Everyone needs a friend'))
    # test_list.add_book_to_list(Book('543-7651-5-436-21', 'Michael Myers', 'On the edge of the knife'))
    # test_list.add_book_to_list(Book('765-3293-065-431', 'Gordon Ramsay', 'You donkey'))
    # test_list.add_book_to_list(Book('795-39773-6027-5', 'Usain Volt', 'Why Tesla was wrong'))
    # test_list.add_book_to_list(Book('5799-8455-5643-0', 'Adolf Hitler', 'Mein Kampf'))
    # test_list.add_book_to_list(Book('65-267-2958-5903', 'Napoleon Bonaparte', 'The life of a baguette'))
    # test_list.add_book_to_list(Book('8793-486-19619-2', 'Vincent Van Gogh', 'A quiet place'))
    # test_list.add_book_to_list(Book('95-493-296-481-51', 'Isaac Newton', 'Cooking with apples'))
    # test_list.add_book_to_list(Book('643-6531-6593-76', 'Galileo Galilei', 'Straight architecture'))
    return test_list


def test_add_to_list():
    """
    Testing function for add_to_list
    :return:
    """
    testing_list = test_init()
    test_book_to_add = Book('978-5-5654-6542-0', 'Mustard Eminem', 'Rap god')
    testing_list.add_book_to_list(test_book_to_add)
    assert len(testing_list) == 11


test_add_to_list()


def test_filter_book_title():
    test_list = ManageListBooks()
    test_list.add_book_to_list(Book('978-4-4140-9666-8', 'Thomas Edison', 'The light at the end of the tunnel'))
    test_list.add_book_to_list(Book('978-2-5316-7621-3', 'Bob Ross', 'Everyone needs a friend'))
    test_list.add_book_to_list(Book('978-7-5124-6274-8', 'Michael Myers', 'On the edge of the knife'))
    test_list.add_book_to_list(Book('978-1-1102-5620-4', 'Gordon Ramsay', 'You donkey'))
    test_list.add_book_to_list(Book('978-4-9276-3464-7', 'Usain Volt', 'Why Tesla was wrong'))
    test_list.add_book_to_list(Book('978-3-6421-7960-0', 'Adolf Hitler', 'Mein Kampf'))
    test_list.add_book_to_list(Book('978-3-6402-6903-7', 'Napoleon Bonaparte', 'The life of a baguette'))
    test_list.add_book_to_list(Book('978-6-8324-6183-7', 'Vincent Van Gogh', 'A quiet place'))
    test_list.add_book_to_list(Book('978-4-9532-3076-9', 'Isaac Newton', 'Cooking with apples'))
    test_list.add_book_to_list(Book('978-6-9213-6459-9', 'Galileo Galilei', 'Straight architecture'))
    test_list.filter_book_title('the')
    assert len(test_list) == 7


test_filter_book_title()
