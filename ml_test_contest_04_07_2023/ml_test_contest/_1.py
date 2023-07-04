# import numpy as np
# import matplotlib.pyplot as plt
# N = 10**3
# r_vec = np.random.uniform(0.0, 1.0, size = N)
# phi_vec = np.random.uniform(0.0, 1.0, size = N)
#
# # plt.scatter(x_r_phi_vev,y_r_phi_vev)
# fig1, axs1 = plt.subplots(nrows=2, ncols=2)
# def p_r_for_xy(r):
#     if (r < 0.0) or (r > 1.0):
#         return 0.0
#     else:
#         return r*2.0
# def p_r_for_rphi(r):
#     if (r<0.0) or (r>1.0):
#         return 0.0
#     else:
#         return 1.0
# def rfunc(x,y):
#     return np.sqrt(np.square(x)+np.square(y))
#
# #
# # def p_cos(z):
# #     if (z <= -1.0) or (z >= 1.0):
# #         return 0.0
# #     else:
# #         return 1.0/np.sqrt(1-np.square(z))/np.pi
# #
# # def p_sin(z):
# #     if (z <= -1.0) or (z >= 1.0):
# #         return 0.0
# #     else:
# #         return 1.0 / np.sqrt(1 - np.square(z)) / np.pi
# #
# # def cos(x,y):
# #     return x/np.sqrt(np.square(x)+np.square(y))
#
# x_vec = []
# y_vec = []
# while len(x_vec)!=N:
#     tmpx = np.random.uniform(low=-1.0, high=1.0)
#     tmpy = np.random.uniform(low=-1.0, high=1.0)
#     if tmpx**2 + tmpy**2 > 1.0:
#         continue
#     x_vec.append(tmpx)
#     y_vec.append(tmpy)
# x_vec = np.asarray(x_vec)
# y_vec = np.asarray(y_vec)
#
# x_r_phi_vec = r_vec*np.cos(2*np.pi*phi_vec)
# y_r_phi_vec = r_vec*np.sin(2*np.pi*phi_vec)
# r_xy = [rfunc(x,y) for x,y in zip(x_vec,y_vec)]
# r_rphi =  [rfunc(x,y) for x,y in zip(x_r_phi_vec,y_r_phi_vec)]
#
# r_ = np.linspace(start = 0.0, stop = 2*np.sqrt(2), num = 101)
# p_xy = [p_r_for_xy(z_i)  for z_i in r_]
# p_rphi = [p_r_for_rphi(z_i)  for z_i in r_]
#
# axs1[0][0].plot(r_,p_xy)
# axs1[0][0].set_title(r'$p_{r},x \sim U[0,1],y \sim U[0,1]$')
# counts, bins = np.histogram(r_xy,density=True)
# print(counts)
# print(bins)
# axs1[0][1].stairs(counts, bins)
# # axs1[0][1].set_title('hist')
#
# axs1[1][0].plot(r_,p_rphi)
# axs1[1][0].set_title(r'$p_{r},r \sim U[0,1]$')
# counts2, bins2 = np.histogram(r_rphi, density=True)
# axs1[1][1].stairs(counts2, bins2)
# print(counts2)
# print(bins)


# plt.scatter()
# plt.show()

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