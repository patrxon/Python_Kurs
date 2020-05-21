from os import walk, path
import hashlib
import sys

def get_hash(file_name):
    with open(file_name, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

        return file_hash.hexdigest()


def get_size(file_name):
    return path.getsize(file_name)


def search_copy(dir_name):
    copy_dir = {}

    for root, dirs, files in walk(dir_name):
        for file_ in files:
            path_ = root + "\\" + file_
            hash_ = get_hash(path_)
            size_ = get_size(path_)

            if (size_, hash_) not in copy_dir:
                copy_dir[(size_, hash_)] = [path_]
            else:
                copy_dir[(size_, hash_)].append(path_)

    for hash_ in copy_dir:
        if len(copy_dir[hash_]) > 1:
            print("-------------------------------------")
            for file_ in copy_dir[hash_]:
                print(file_)


dir_name_ = sys.argv[1]
search_copy(dir_name_)
