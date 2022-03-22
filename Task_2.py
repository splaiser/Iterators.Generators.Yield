nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(lists):
    for list in lists:
        for some_elem in list:
            yield some_elem


for item in flat_generator(nested_list):
    print(item)
