nested_list = [
    ['a', 'b', 'c'],
    ['d', ['a', 'b', 'c'], 'f', 'h', False],
    [1, 2, ['a', ['a', None, 'c'], 'c']],
]


class FlatIterator:

    def __init__(self, list_some, result=[]):
        self.list_some = list_some
        self.result = result

    def list_nesting(self, some_list):
        for some_item in some_list:
            if type(some_item) is list:
                self.list_nesting(some_item)
            else:
                self.result.append(some_item)

    def __iter__(self):
        self.list_nesting(self.list_some)
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
