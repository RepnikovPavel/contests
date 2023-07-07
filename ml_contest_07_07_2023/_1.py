import numpy as np
def p_r_for_xy(r):
    if (r < 0.0) or (r > 1.0):
        return 0.0
    else:
        return r*2.0
def p_r_for_rphi(r):
    if (r<0.0) or (r>1.0):
        return 0.0
    else:
        return 1.0
def rfunc(x,y):
    return np.sqrt(np.square(x)+np.square(y))

if __name__ == '__main__':
    ifstream = open('input.txt', 'r')
    ofstream = open('output.txt', 'w')
    for i in range(100):
        X_i_str = ifstream.readline().replace('\n', '')
        if len(X_i_str) == 0:
            break
        n_i = [np.float32(el) for el in X_i_str.split(sep=' ')]
        x_i = np.zeros(shape=(1000,), dtype=np.float32)
        y_i = np.zeros(shape=(1000,), dtype=np.float32)
        k_ = 0
        for j in range(0,len(n_i)-1,2):
            x_i[k_]= n_i[j]
            y_i[k_] = n_i[j+1]
            k_ += 1

        r_vec = rfunc(x_i, y_i)
        # r_vec = [rfunc(x,y) for x,y in zip(x_i,y_i)]
        counts, bins = np.histogram(r_vec, density=True)
        # расстояние до треугольника
        d1 = np.sum([np.square(p_r_for_rphi(bins[i])-counts[i]) for i in range(len(bins)-1)])
        # расстояние до равномерного распр
        d2 = np.sum([np.square(p_r_for_xy(bins[i])-counts[i]) for i in range(len(bins)-1)])
        is_first = True
        if d1 >= d2:
            is_first = False
        o_line = ''
        if is_first:
            o_line = str(1)
        else:
            o_line = str(2)
        ofstream.write(o_line+'\n')
    ifstream.close()
    ofstream.close()