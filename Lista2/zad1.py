import os
import sys

def check_file(file_name):
    file = open(file_name, 'r')

    byte_num = os.stat(file_name).st_size
    word_num = 0
    line_num = 0
    longest_line = 0

    if byte_num > 0:
        line_num += 1
        for line in file:

            print("-", line)

            if len(line) > longest_line:
                longest_line = len(line)
                if "\n" in line:
                    longest_line -= 1

            if "\n" in line:
                line_num += 1

            word_list = line.split()

            word_num += len(word_list)

    print("bytes: ", byte_num)
    print("words: ", word_num)
    print("lines: ", line_num)
    print("longest: ", longest_line)


name = sys.argv[1]
check_file(name)
