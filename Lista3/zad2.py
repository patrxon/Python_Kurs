
list_ = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]


def flatten(arr):
    for elem in arr:
        if type(elem) == list:
            for inside in flatten(elem):
                yield inside
        else:
            yield elem


print(list(flatten(list_)))
