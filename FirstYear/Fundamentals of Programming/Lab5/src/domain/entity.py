"""
    Entity class should be coded here
"""


class BookException(Exception):
    def __init__(self, message):
        self._message = message


class Book:
    def __init__(self, isbn, author, title):
        isbn_copy = isbn
        isbn_copy = isbn_copy.replace('-', '')
        if not isbn_copy.isalnum():
            raise BookException('Invalid ISBN! It must respect the format: 978-x-xxxx-xxxx-x, with x int btw [0,9]')
        else:
            if len(isbn_copy) != 13:
                raise BookException('Invalid ISBN! It must respect the format: 978-x-xxxx-xxxx-x, with x int btw [0,9]')
            first_hyphen = 3  # The position where the first hyphen should be
            second_hyphen = 5  # The position where the second hyphen should be
            third_hyphen = 10  # The position where the third hyphen should be
            fourth_hyphen = 15  # The position where the fourth hyphen should be
            if isbn[first_hyphen] != '-' or isbn[second_hyphen] != '-' or isbn[third_hyphen] != '-' or isbn[fourth_hyphen] != '-':
                raise BookException('Invalid ISBN! It must respect the format: 978-x-xxxx-xxxx-x, with x int btw [0,9]')
            if isbn_copy.find('978') != 0:
                raise BookException('Invalid ISBN! It must respect the format: 978-x-xxxx-xxxx-x, with x int btw [0,9]')

        author_copy = author
        author_copy = author_copy.replace(' ', '')
        author_copy = author_copy.replace('-', '')
        if not author_copy.isalpha():
            raise BookException('Invalid author name! The name must contain only letters and spaces!')
        self._isbn = isbn
        self._author = author
        self._title = title

    @property
    def isbn(self):
        """
        Returns the isbn of the book
        :return: self._isbn
        """
        return self._isbn

    @property
    def author(self):
        """
        Returns the author of the book
        :return: self._author
        """
        return self._author

    @property
    def title(self):
        """
        Returns the title of the book
        :return: return self._title
        """
        return self._title
