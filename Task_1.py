nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator(list):

    def __init__(self, list):
        self.list = list
        self.result = []

    def __iter__(self):
        for some_list in self.list:
            for some_item in some_list:
                self.result.append(some_item)
        return self

    def __next__(self):
        if len(self.result) > 0:
            return self.result.pop(0)
        else:
            raise StopIteration


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
