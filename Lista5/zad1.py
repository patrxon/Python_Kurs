import numpy as np
import matplotlib.pyplot as plt


def get_data(file_name):
    arr = []
    with open(file_name, "r") as file_:
        for line in file_:
            arr.append(line.split(",")[0:3])
    del (arr[0])
    return arr


def extract_data(arr):
    user = 0
    has_rating = False
    i = 0
    while i < len(arr):
        if int(arr[i][0]) > user:
            user = int(arr[i][0])
            if arr[i][1] == '1':
                has_rating = True
            else:
                has_rating = False

        if not has_rating:
            del (arr[i])
            i -= 1
        i += 1
    return arr


def trim_users(arr, n):
    user = 0
    i = 0
    count = -1
    arr_x = []
    arr_y = []
    full = False
    while len(arr_y) <= n:
        if i >= len(arr):
            full = True
            break
        if int(arr[i][0]) > user:
            user = int(arr[i][0])
            temp = [float(arr[i][2])]
            arr_y.append(temp)
            arr_x.append({})
            count += 1
        else:
            arr_x[count][int(arr[i][1])] = float(arr[i][2])
        i += 1

    if not full:
        del (arr_y[-1])
        del (arr_x[-1])
    return arr_y, arr_x


def trim_films(arr, m):
    arr_x = []
    i = 0
    for user in arr:
        arr_x.append([])
        for j in range(2, m + 2):
            if j in user:
                arr_x[i].append(user[j])
            else:
                arr_x[i].append(0.0)
        i += 1

    return arr_x


def make_data_set(file_name, n, m):
    arr = get_data(file_name)
    arr = extract_data(arr)
    arr_y, arr_x = trim_users(arr, n)
    arr_x = trim_films(arr_x, m)

    return arr_y, arr_x


def add_full_regression(arr_x, arr_y):
    arr_x = np.array(arr_x)
    arr_y = np.array(arr_y)
    data = np.linalg.lstsq(arr_x, arr_y, rcond=None)[0]

    predictions = []

    for user in arr_x:
        temp = 0
        for i in range(len(data)):
            temp += user[i] * data[i]
        predictions.append(temp)

    axis_x = np.arange(len(arr_y)).reshape(len(arr_y), 1)
    error = np.array(predictions) - np.array(arr_y)

    name = 'error' + str(len(arr_x[0]))
    size = str(7 - np.log10(len(arr_x[0])))

    plt.plot(axis_x, error, 'o', label=name, markersize=size)


def test_full_regression(file_name, test_set):
    for size in test_set:
        arr_y, arr_x = make_data_set(file_name, 215, size)
        add_full_regression(arr_x, arr_y)
    plt.legend()
    plt.show()


def add_partial_regression(arr_x, arr_y, divider):
    arr_x = np.array(arr_x)
    arr_y = np.array(arr_y)
    data = np.linalg.lstsq(arr_x[0:divider], arr_y[0:divider], rcond=None)[0]

    test_x = arr_x[divider:]
    test_y = arr_y[divider:]
    predictions = []

    for user in test_x:
        temp = 0
        for i in range(len(data)):
            temp += user[i] * data[i]
        predictions.append(temp)

    axis_x = np.arange(len(test_y)).reshape(len(test_y), 1)
    error = np.array(predictions) - np.array(test_y)

    name = 'error' + str(len(test_x[0]))
    size = str(15 - np.log10(len(test_x[0]))*2)

    plt.plot(axis_x, error, 'o', label=name, markersize=size)


def test_partial_regression(file_name, test_set):
    for size in test_set:
        arr_y, arr_x = make_data_set(file_name, 215, size)
        add_partial_regression(arr_x, arr_y, 200)
        if size == 200:
            plt.legend()
            plt.show()
            plt.figure()

    plt.legend()
    plt.show()


test_full_regression("ratings.csv", [10, 100, 1000, 10000])
plt.figure()
test_partial_regression("ratings.csv", [10, 100, 200, 500, 1000, 10000])

