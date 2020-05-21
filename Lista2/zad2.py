import sys

tab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode_file(file_name, code_name):
    file = open(file_name, 'rb')
    cd_file = open(code_name, 'w')

    byte = file.read(1)

    total = ""

    while byte:
        temp = ord(byte)
        temp = bin(temp)[2:].rjust(8, '0')
        print(temp, end=" ")
        byte = file.read(1)

        total += temp

    code = ""

    print("\n", total)

    for index in range(len(total))[0::6]:
        temp = str(total[index:index + 6])
        code += tab[int(temp, 2)]

    print(code)
    cd_file.write(code)


def decode_file(code_name, file_name):
    cd_file = open(code_name, 'rb')
    file = open(file_name, 'w')

    byte = cd_file.read(1)

    total = ""

    while byte:
        temp = byte.decode("utf-8")
        index = tab.index(temp)
        total += bin(index)[2:].rjust(6, '0')
        print(bin(index)[2:].rjust(6, '0'), end=" ")

        byte = cd_file.read(1)

    print("\n", total)

    code = ""

    for index in range(len(total))[0::8]:
        temp = str(total[index:index + 8])
        code += chr(int(temp, 2))

    print(code)
    file.write(code)


if sys.argv[1] == "--encode":
    encode_file(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "--decode":
    decode_file(sys.argv[2], sys.argv[3])
