def sum_bits(file_name):
    with open(file_name, "r") as file_:
        print(sum([int(line.split()[-1]) for line in file_]))


sum_bits("text.txt")
