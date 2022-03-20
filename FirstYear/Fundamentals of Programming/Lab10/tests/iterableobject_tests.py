from repositories.iterableobject import IterableObject, SortAndFilter
import unittest


class TestIterableObject(unittest.TestCase):
    def setUp(self):
        self._iterable_object = IterableObject()

    def test_instance(self):
        self.assertIsInstance(self._iterable_object, IterableObject)

    def test_len(self):
        self._iterable_object = IterableObject([1, 2, 6, 7, 3, 4])
        assert len(self._iterable_object) == 6

    def test_getitem(self):
        self._iterable_object = IterableObject([1, 2, 6, 7, 3, 4])
        some_number = self._iterable_object[3]
        assert some_number == 7

    def test_setitem(self):
        self._iterable_object = IterableObject([1, 2, 6, 7, 3, 4])
        some_number = self._iterable_object[3]
        self._iterable_object[2] = some_number
        assert self._iterable_object[2] == 7

    def test_add(self):
        self._iterable_object = IterableObject([1, 2, 6, 7, 3, 4])
        self._iterable_object.append(10)
        assert self._iterable_object[-1] == 10

    def test_del_remove(self):
        self._iterable_object = IterableObject([1, 2, 6, 7, 3, 4])
        self._iterable_object.remove(0)
        assert self._iterable_object[0] == 2

    def test_iter(self):
        iterator = iter(self._iterable_object)
        with self.assertRaises(StopIteration):
            next(iterator)
        self._iterable_object = [4, 20]
        iterator = iter(self._iterable_object)
        assert next(iterator) == 4
        assert next(iterator) == 20


class TestSortAndFilter(unittest.TestCase):
    def setUp(self):
        self._sort_and_filter = SortAndFilter()
        self._some_list = [1, 2, 6, 7, 3, 4]

    def test_sort(self):
        self._sort_and_filter.sort(self._some_list, function=lambda x, y: x > y)
        assert self._some_list == [1, 2, 3, 4, 6, 7]

    def test_filter(self):
        self._sort_and_filter.filter(self._some_list, function=lambda x: x < 4)
        assert self._some_list == [1, 2, 3]
