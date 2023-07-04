import sys

import numpy as np


def throw_repeats_and_sum(permutation: np.array):
    for i in range(len(permutation) - 1, 0, -1):
        if permutation[i] == permutation[i - 1]:
            permutation[i] = 0
    return np.sum(permutation)


def addone(indexes: np.array, pos_to_add: int, max_index: int) -> None:
    if pos_to_add == -1:
        return
        # print('+ overflow')
        # for j in range(len(indexes)):
        #     indexes[j] = 0
        # return
    if indexes[pos_to_add] < max_index:
        indexes[pos_to_add] += 1
        # обнулить младшие разряды
        for j in range(pos_to_add + 1, len(indexes)):
            indexes[j] = 0
        return
    if indexes[pos_to_add] == max_index:
        addone(indexes, pos_to_add - 1, max_index)


def adding_with_overflow(indexes, max_index):
    addone(indexes, len(indexes) - 1, max_index)


def calc_expectation(a_vec, k):
    placeholder = np.zeros(shape=(k,), dtype=np.intc)
    n_outcomes = len(a_vec) ** k
    S = 0
    max_index = len(a_vec) - 1
    indexes = np.zeros(shape=(k,), dtype=np.intc)
    for j in range(n_outcomes):
        for i in range(k):
            placeholder[i] = a_vec[indexes[i]]
        # print(placeholder)
        S += throw_repeats_and_sum(placeholder)
        adding_with_overflow(indexes, max_index=max_index)
    E = float(S) / n_outcomes
    return E


if __name__ == '__main__':
    ifstream = open('input.txt', 'r')
    A_str = ifstream.readline().replace('\n', '')
    ofstream = open('output.txt', 'w')
    if len(A_str) == 0:
        ofstream.write(str(0.0))
        sys.exit()
    a_vec = [np.intc(el) for el in A_str.split(sep=' ')]
    if len(a_vec) > 6:
        a_vec = a_vec[:6]
    for i in range(len(a_vec)):
        if not (1 <= a_vec[i] <= 1000):
            ofstream.write(str(0.0))
            sys.exit()
    k_str = ifstream.readline().replace('\n', '')
    if len(k_str) == 0:
        ofstream.write(str(0.0))
        sys.exit()
    k = np.intc(k_str)
    if not (1 <= k <= 1000):
        ofstream.write(str(0.0))
        sys.exit()
    ofstream.write(str(np.around(calc_expectation(a_vec, k), decimals=10)))
    ofstream.close()
    ifstream.close()
