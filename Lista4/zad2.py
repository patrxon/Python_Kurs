from random import randrange


def change_tree(tree, tab, value, n=0):
    if n < len(tab) - 1:
        change_tree(tree[tab[n]], tab, value, n + 1)
    else:
        tree[tab[n]] = value


def search_tree(tree, tab, n=0):
    if tree[tab[n]] is None:
        return None
    elif n < len(tab) - 1:
        return search_tree(tree[tab[n]], tab, n + 1)
    else:
        return tree[tab[n]]


def binary_shift(tab):
    tab[-1] += 1
    for i in range(len(tab) -1, 0, -1):
        if tab[i] > 2:
            tab[i - 1] += 1
            tab[i] = 1
    if tab[0] > 2:
        tab[0] = 1
        tab.append(1)


def bfs_numerate(tree):
    search_tab = [1]
    depth = 1
    number = 2
    empty = False

    while True:
        if search_tree(tree, search_tab+[0]) is not None:
            change_tree(tree, search_tab+[0], number)
            number += 1
            empty = False

        binary_shift(search_tab)

        if len(search_tab) > depth:
            depth += 1
            if empty:
                break
            else:
                empty = True


def generate_tree(height):
    tree = [1, None, None]
    temp = tree

    while temp[0] <= height:
        temp = tree
        depth = 2
        path_arr = []
        path = randrange(1, 3)
        path_arr.append(path)

        while temp[path] is not None:
            temp = temp[path]
            path = randrange(1, 3)
            path_arr.append(path)
            depth += 1

        if depth <= height:
            change_tree(tree, path_arr, [depth, None, None])
        else:
            bfs_numerate(tree)
            return tree


def bfs_search_tree(tree):
    print(tree[0])
    search_tab = [1]
    depth = 1
    empty = False

    while True:
        check = search_tree(tree, search_tab+[0])
        if check is not None:
            print(check)
            empty = False
        binary_shift(search_tab)

        if len(search_tab) > depth:
            depth += 1
            if empty:
                break
            else:
                empty = True


def dfs_search_tree(tree):
    print(tree[0])
    search_tab = [1]

    while search_tab[0] < 3:
        check = search_tree(tree, search_tab+[0])
        if check is not None:
            print(check)
            search_tab.append(1)
        else:
            if search_tab[-1] == 1:
                search_tab[-1] += 1
            elif len(search_tab) > 1:
                del search_tab[-1]
                search_tab[-1] += 1
                while len(search_tab) > 1 and search_tab[-1] > 2:
                    del search_tab[-1]
                    search_tab[-1] += 1
            else:
                break


tree_ = generate_tree(3)

print(tree_)

dfs_search_tree(tree_)