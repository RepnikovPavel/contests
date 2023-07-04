import copy

import numpy as np
import math

def throw_repeats_and_sum(permutation: np.array):
    # if repeat mask with zero
    # k is a number of masked elements
    k_=0
    for i in range(len(permutation)-1, 0, -1):
        if permutation[i] == permutation[i-1]:
            permutation[i] = 0.0
            k_+=1
    return k_, np.sum(permutation)


def addone(indexes:np.array, pos_to_add:int, max_index:int) -> None:
    if pos_to_add == -1:
        print('+ overflow')
        for j in range(len(indexes)):
            indexes[j] = 0
        return
    if indexes[pos_to_add] < max_index:
        indexes[pos_to_add] += 1
        # обнулить младшие разряды
        for j in range(pos_to_add+1,len(indexes)):
            indexes[j]=0
        return
    if indexes[pos_to_add] == max_index:
        addone(indexes, pos_to_add-1, max_index)




def adding_with_overflow(indexes, max_index):
    addone(indexes,len(indexes)-1,max_index)
    # print(indexes)

def calc_expectation(a_vec, k):
    if k == 0:
        return 0.0
    placeholder = np.zeros(shape=(k,), dtype=np.intc)
    # fix element in current cell move to next cell if end
    np.sort(a_vec)
    n_outcomes = len(a_vec)**k

    l_ = 0
    K = 0
    S = 0

    indexes = np.zeros(shape=(k,),dtype=np.intc)
    while True:
        for i in range(k):
            placeholder[i] = a_vec[indexes[i]]
        k_, s_ = throw_repeats_and_sum(placeholder)
        S += s_
        K += k_
        l_ += 1
        if l_ == n_outcomes:
            break
        adding_with_overflow(indexes,max_index=len(a_vec)-1)
    # print(K)
    E = S/(n_outcomes*k-K)
    return E

if __name__ == '__main__':
    ifstream = open('input.txt','r')
    A_str = ifstream.readline().replace('\n','')
    a_vec = [float(el) for el in A_str.split(sep = ' ')]
    k = int(ifstream.readline().replace('\n',''))
    ofstream = open('output.txt', 'w')
    ofstream.write(str(calc_expectation(a_vec, k)))
    ofstream.close()
