import os
import json

cwd_path = os.getcwd()
file_path = 'files'


def read_data(file_name, key='ordered_numbers'):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, string),
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(os.path.join(cwd_path, file_path, file_name), 'r') as json_file:
        seqs = json.load(json_file)

    return seqs[key]


def binary_search(seq, number):
    """
    Function performs binary search on !!ordered!! sequence and stores position of match if found.
    :param seq: (list): list on numbers
    :param number: (int): number to match within sequence
    :return: (int, None): index of match if found, None otherwise
    """
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return middle
    return


def recursive_binary_search(seznam, hodnota, left_idx, right_idx):
    """
    Fce vrátí pozici hledaného prvku v seřazenám seznamu.
    :param seznam: (list) Seřazený seznam čísel
    :param hodnota: (int) Hledaná hodnota
    :param left_idx: (int) index levého okraje prohledávaného prostoru
    :param right_idx: (int) index pravého okraje prohledávaného prostoru
    :return: (int) Pozice hledaného prvku
    """
    middle = (left_idx + right_idx) // 2
    if (left_idx - right_idx) == 0:
        return None
    elif hodnota < seznam[middle]:
        return recursive_binary_search(seznam, hodnota, left_idx, middle)
    elif hodnota > seznam[middle]:
        return recursive_binary_search(seznam, hodnota, middle + 1, right_idx)
    else :
        return middle


def main(file_name, number):
    sequence = read_data(file_name=file_name, key='ordered_numbers')

    # iterative binary search
    pozice_iterativne = binary_search(sequence, number=number)
    print(pozice_iterativne)

    pozice_rekurze = recursive_binary_search(sequence, number, 0, len(sequence)-1)
    print(pozice_rekurze)


if __name__ == '__main__':
    my_file = 'sequential.json'
    my_number = 90
    main(my_file, my_number)
