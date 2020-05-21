from functools import reduce


def generate(n):
    return [reduce(lambda x, y: x + " " + y, [str(i) + "." + str(j) for i in range(1, n + 1)]) for j in range(1, n + 1)]


def transpose(arr):
    return [" ".join([[elem.split() for elem in arr][i][j] for i in range(len(arr))]) for j in range(len(arr))]


tab = generate(4)
print("original:\n" + "\n".join(tab))
tab = transpose(tab)
print("transposed:\n" + "\n".join(tab))
tab = transpose(tab)
print("reversed:\n" + "\n".join(tab))
