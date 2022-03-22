nested_list = [
    ['a', 'b', 'c'],
    ['d', ['a', 'b', 'c'], 'f', 'h', False],
    [1, 2, ['a', ['a', None, 'c'], 'c']],
]


def flat_generator(some_list):
    for next_item in some_list:
        if type(next_item) is list:
            flat_generator(next_item)
        else:
            yield next_item


for item in flat_generator(nested_list):
    print(item)
