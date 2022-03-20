class IterableObject:
    def __init__(self, data=None):
        if data is None:
            self._data = []
        else:
            self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def append(self, element):
        self._data.append(element)

    def remove(self, element):
        self.__delitem__(element)

    def __iter__(self):
        yield from self._data


class SortAndFilter:

    @staticmethod
    def sort(some_list, function=lambda number1, number2: number1 > number2):
        index = 0
        while index < len(some_list):
            if index == 0 or not function(some_list[index-1], some_list[index]):
                index += 1
            else:
                some_list[index], some_list[index-1] = some_list[index-1], some_list[index]
                index -= 1

    @staticmethod
    def filter(data, function):
        data[:] = [element for element in data if function(element)]
