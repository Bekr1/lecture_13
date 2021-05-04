import os
import csv
import matplotlib.pyplot as plt
import math

cwd_path = os.getcwd()
file_path = 'files'


def read_file(file_name):
    """
    Reads csv file from given folder
    :param file_name: (str) the name of csv file
    :return:
    """
    data_points = []
    with open(os.path.join(cwd_path, file_path, file_name), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # skip header
        next(csv_reader)

        # read each row
        for row in csv_reader:
            data_points.append([float(number) for number in row])

    return data_points


def draw_data(data_points, closest_pair=[]):
    """
    Function creates new figure and draw data points into scatter plot.
    :param data_points: (list of lists): each sublist is 1x2 list with x and y coordinate of a point.
    :param closest_pair: (tuple of ints): indices of the closest pair of points, default = empty list
    :return:
    """

    plt.scatter(
        x=[point[0] for point in data_points],
        y=[point[1] for point in data_points],
        color=['blue' if point not in closest_pair else 'red' for point in data_points]
    )
    plt.show()
    
def closest_pair_BF(array):
    min_dist = math.dist(array[0], array[1])
    point_1 = array[0]
    point_2 = array[1]
    num_points = len(array)

    if num_points == 2:
        return point_1, point_2, min_dist
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            if i != 0 and j != 1:
                dist = math.dist(array[i], array[j])
                if dist < min_dist:
                    min_dist = dist
                    point_1, point_2 = array[i], array[j]
    return point_1, point_2, min_dist


def closest_pair(seznam_dle_x, seznam_dle_y):
    """
    Fce zjistí 2 body s nejmenší vzájemnou vzdáleností.
    :param seznam_dle_x: (list) Seznam bodů seřazený podle x-ové souřadnice.
    :param seznam_dle_y: (list) Seznam bodů seřazený podle y-ové souřadnice.
    :return:
    """
    pocet_bodu = len(seznam_dle_x)
    middle_idx = len(seznam_dle_x) // 2

    if pocet_bodu <= 3:
        bod1, bod2, vzdalenost = closest_pair_BF(seznam_dle_x)
        return bod1, bod2, vzdalenost

    left_X = seznam_dle_x[:middle_idx]
    right_X = seznam_dle_x[middle_idx:]

    middle_point = seznam_dle_x[middle_idx][0]
    left_Y = []
    right_Y = []

    for bod in seznam_dle_y:
        if bod[0] <= middle_point:
            left_Y.append(bod)
        else:
            right_Y.append(bod)

    p1, q1, vzdalenost1 = closest_pair(left_X, left_Y)
    p2, q2, vzdalenost2 = closest_pair(right_X, right_Y)

    if vzdalenost1 <= vzdalenost2:
        min_vzdalenost = vzdalenost1
        body = (p1, q1)
    else:
        min_vzdalenost = vzdalenost2
        body = (p2, q2)

    p3, q3, vzdalenost3 = closest_split_pair(seznam_dle_x, seznam_dle_y, min_vzdalenost, body)
    if min_vzdalenost <= vzdalenost3:
        return body[0], body[1], min_vzdalenost
    else:
        return p3, q3, vzdalenost3


def closest_split_pair(seznam_dle_x, seznam_dle_y, min_vzdalenost, body):
    pocet_bodu = len(seznam_dle_x)
    midpoint_x = seznam_dle_x[pocet_bodu // 2][0]
    bod1, bod2 = body[0], body[1]

    subarray_y = []
    for i in seznam_dle_y:
        if (midpoint_x - min_vzdalenost) <= i[0] <= (midpoint_x + min_vzdalenost):
            subarray_y.append(i)

    len_y = len(subarray_y)
    for j in range(len_y - 1):
        for k in range(j + 1, min(j + 7, len_y)):    #3 prvky z každé strany jsou již ošetřeny brutal force, proto j + 7
            vzdalenost = math.dist(subarray_y[j], subarray_y[k])
            if vzdalenost < min_vzdalenost:
                min_vzdalenost = vzdalenost
                bod1, bod2 = subarray_y[j], subarray_y[k]

    return bod1, bod2, min_vzdalenost


def main(file_name):
    # read data points
    data_points = read_file(file_name)

    # draw points
    draw_data(data_points)

    serazeno_x = sorted(data_points, key=lambda x: x[0])
    serazeno_y = sorted(data_points, key=lambda x: x[1])

    #nejmenší vzdálenost pomocí brutal force
    bod1, bod2, vzdalenost = closest_pair_BF(data_points)
    print(bod1, bod2, vzdalenost)

    # nejmenší vzdálenost pomocí rekurze
    point1, point2, dist = closest_pair(serazeno_x, serazeno_y)
    print(point1, point2, dist)

if __name__ == '__main__':
    my_file = 'points.csv'
    main(my_file)
