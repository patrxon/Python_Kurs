from random import randrange


class Node:
    def __init__(self, name, height):
        self.height = height
        self.name = name
        self.children = []
        self.size = 0

    def change_name(self, name):
        self.name = name

    def add_child(self, name):
        self.size += 1
        self.children.append(Node(name, self.height))

    def get_child(self, index):
        if index < self.size:
            return self.children[index]
        else:
            return False

    def print_children(self):
        for child in self.children:
            print(child.name, "-", child.size, end="|")


def generate_tree(height):
    root = Node(1, height)
    temp = root
    depth = 2

    while temp.name != height:
        path = randrange(-1, temp.size)
        if path == -1:
            temp.add_child(depth)
            temp = root
            depth = 2
        else:
            temp = temp.get_child(path)
            depth += 1

    return root


def get_branch(tree, tab, n=0):
    if len(tab) == 0:
        return tree
    elif tree.get_child(tab[n]) is False:
        return False
    elif n < len(tab) - 1:
        return get_branch(tree.get_child(tab[n]), tab, n + 1)
    else:
        return tree.get_child(tab[n])


def print_tree(root):
    print(root.name, end="~")
    root.print_children()
    print("")

    tree_path = [0]

    while len(tree_path) < root.height:
        branch = get_branch(root, tree_path)
        if branch:
            tree_path[-1] += 1

        print(tree_path)

        for index_ in range(len(tree_path), 1, -1):
            while not get_branch(root, tree_path[0:index_]):
                tree_path[index_] += 1
                if tree_path[index_] > get_branch(root, tree_path[0:(index_ - 1)]):
                    break




tree_ = generate_tree(3)

print_tree(tree_)
