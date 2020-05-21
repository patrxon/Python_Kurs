from os import walk, rename
import sys


def search_dir(dir_name):
    for root, dirs, files in walk(dir_name):

        for dir_ in dirs:
            name = root + "\\" + dir_
            rename(name, name.lower())

        for file_ in files:
            name = root + "\\" + file_
            rename(name, name.lower())


dir_name_ = sys.argv[1]
print(dir_name_)
search_dir(dir_name_)
