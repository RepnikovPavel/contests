import sys
import numpy as np

def is_target(a_i: np.intc, k: int) -> bool:
    return 1 <= a_i <= k

def reset_dict(d: np.array) -> None:
    d.fill(0)
    # print(1)
    # for i in range(len(d)):
    #     d[i] = np.intc

def is_all_found(d: np.array, k: int) -> bool:
    # for el in d.values():
    #     s_ += el
    return np.sum(d) == k

def search_next_seq(a_vec:np.array, start_pos:int, min_s:int, k:int, n:int, have_y_seen_the_k: np.array):
    current_s = 0
    for i in range(start_pos, n):
        a_i = a_vec[i]
        if is_target(a_i, k):
            have_y_seen_the_k[a_i - 1] = 1
        elif (not is_target(a_i, k)) and current_s == 0:
            start_pos += 1
            continue
        current_s += a_i

        # else:
        #     current_s = 0
        #     reset_dict(have_y_seen_the_k)
        #     start_pos = i + 1
        if is_all_found(have_y_seen_the_k, k):
            min_s = min(min_s, current_s)
            reset_dict(have_y_seen_the_k)
            start_pos += 1
            return start_pos, min_s
    return n, min_s


if __name__ == '__main__':
    ifstream = open('input.txt', 'r')
    ofstream = open('output.txt', 'w')
    n, k = tuple([int(el) for el in ifstream.readline().replace('\n', '').split(' ')])
    a_vec = np.array([int(el) for el in ifstream.readline().replace('\n', '').split(' ')], dtype=np.intc)
    # should buy a_i if a_i in 1...k
    # несколько статуэток одного вида можно покупать.
    # задача: покупка статуэток непрерывным куском l...r
    # 1 2 4 5 3
    # хочет купить a_i in 1...3
    # купит все 1 2 4 5 3
    # 1 2 2 3 3 1
    # хочет купить a_i in 1...3
    # купит 1 2 2 3
    # цена статуэтки == a_i
    # найти минимальную по стоимости последовательность {a_j} подряд идущих a_i
    # таких, что  среди a_j есть все 1...k

    # len(a_vec) == n

    # 1. найти очередную последовательность, которая содержит все 1...k
    # 2. посчитать стоимость такой последовательности
    # 3. повторить п. 1-2 выбрать среди всех последовательностей минимальную стоимость
    # если нет подряд идущих то выдать хоть что-то

    # limitations:
    # n >= k

    min_s = int((5 * 10 ** 5 + 1) * (5 * 10 ** 5 + 2) / 2)
    # have_y_seen_the_k = {i: 0 for i in range(1, k+1)}
    have_y_seen_the_k = np.zeros(shape=(k,), dtype=np.intc)
    # reset_dict(have_y_seen_the_k)
    start_pos = 0
    while True:
        start_pos, min_s = search_next_seq(a_vec, start_pos, min_s, k, n, have_y_seen_the_k)
        if start_pos > n - k:
            break

    ofstream.write(str(min_s))
    ifstream.close()
    ofstream.close()
    sys.exit(0)