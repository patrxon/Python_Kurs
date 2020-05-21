import numpy as np


def get_data(file_name):
    arr = []
    with open(file_name, "r", encoding="utf8") as file_:
        for line in file_:
            arr.append(line.split(",")[0:3])
    del (arr[0])
    return arr


def get_films(file_name):
    arr = {}
    with open(file_name, "r", encoding="utf8") as file_:
        for line in file_:
            film = line.split(",")
            if film[0] != "movieId":
                if int(film[0]) > 10000:
                    break
                arr[int(film[0])] = ','.join(film[1:len(film) - 1])
    return arr


def extract_data(arr):
    new_arr = np.zeros([610, 10000])

    i = 1
    for user in arr:
        if int(user[0]) > i:
            i += 1
        if int(user[1]) <= 10000:
            new_arr[i - 1][int(user[1]) - 1] = float(user[2])

    return new_arr


def calc_recommendations(arr, your_ratings):
    arr_norm = arr / np.linalg.norm(arr, axis=0)
    np.nan_to_num(arr_norm, copy=False)
    your_norm = your_ratings / np.linalg.norm(your_ratings)
    vector = np.dot(arr_norm, your_norm)
    v_norm = vector / np.linalg.norm(vector)
    result = np.dot(arr_norm.T, v_norm)

    return result


def make_your_ratings():
    my_ratings = np.zeros([10000, 1])
    my_ratings[2571] = 5
    my_ratings[32] = 4
    my_ratings[260] = 5
    my_ratings[1097] = 4

    return my_ratings


def get_recommendation_arr(file_name):
    arr = get_data(file_name)
    arr = extract_data(arr)
    your_ratings = make_your_ratings()
    res_ = calc_recommendations(arr, your_ratings)
    return res_


def display_films(res_arr, film_arr):
    final_arr = []

    for i in range(len(res_arr)):
        if i in film_arr:
            final_arr.append([float(res_arr[i]), film_arr[i]])

    final_arr = sorted(final_arr, reverse=True)
    print(*final_arr, sep="\n")


result = get_recommendation_arr("ratings.csv")
films = get_films("movies.csv")
display_films(result, films)
