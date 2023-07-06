# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
# from matplotlib import cm
#
# def plot_rect(ax, x_1, x_2, y_1, y_2, color):
#     h_1 = x_2 - x_1
#     h_2 = y_2 - y_1
#     rect = matplotlib.patches.Rectangle((x_1, y_1), h_1, h_2, color=color)
#     ax.add_patch(rect)
#
# def plotsurf(x_vec, y_vec, func_):
#
#     plt.rcParams["figure.figsize"] = [14, 7]
#     plt.rcParams["figure.autolayout"] = True
#     fig = plt.figure()
#     axs = fig.add_subplot(111)
#
#     rects_info = []
#
#     x = []
#     y = []
#     highs = []
#
#     for j in range(len(x_vec)-1):
#         for k in range(len(y_vec)-1):
#             x_1 = x_vec[j]
#             x_2 = x_vec[j+1]
#             y_1 = y_vec[k]
#             y_2 = y_vec[k+1]
#             x.append((x_2 + x_1) / 2)
#             y.append((y_2 + y_1) / 2)
#             rects_info.append([x_1, x_2, y_1, y_2])
#             point_ = [(x_2 + x_1) / 2, (y_2 + y_1) / 2]
#             highs.append(func_(point_))
#     norm = matplotlib.colors.Normalize(vmin=min(highs), vmax=max(highs))
#     m = cm.ScalarMappable(norm=norm, cmap=cm.viridis)
#
#     tmp_len = len(rects_info)
#     for i in range(len(rects_info)):
#         # print("\r interation {} of {}".format(i, tmp_len), end='')
#         plot_rect(axs, rects_info[i][0], rects_info[i][1], rects_info[i][2], rects_info[i][3],
#                   m.to_rgba(highs[i]))
#     print('')
#
#     plt.colorbar(m, ax=axs)
#     axs.set_xlim([-1.0, 1.0])
#     axs.set_ylim([-1.0, 1.0])
#     axs.set_xlabel(r"$x$")
#     axs.set_ylabel(r'$y$')
#     plt.title(r'$\varphi(x,y)$')
#
#     # axs.scatter(x_, y_, color='r')
#     # plot_graph2D(search_points, adj_matrix, axs,
#     #              plot_vertexes=True,
#     #              plot_edges=False)
#     # plot_clusters(all_groups, list(clusters.keys()), axs, plot_edges=True)
#
#     argmin_ = np.argmin(highs)
#     print('min value = {} x= {}, y={}'.format(highs[argmin_], x[argmin_], y[argmin_]))
#
#     print("plot response surface done")
#     return axs
#
# def f(p):
#     x1 = p[0]
#     x2 = p[1]
#     return 1.0+ x1**2 +x2**2+ x1*x2
#
# N = 1000
# X1 = np.random.uniform(-1.0,1.0,N)
# X2 = np.random.uniform(-1.0,1.0,N)
#
# F = [f(p)for p in zip(X1,X2)]
# ofstream = open('input.txt','w')
# for i in range(len(F)):
#     o_str = str(X1[i]) + '\t' +str(X2[i]) + '\t' +str(F[i]) +'\n'
#
#     ofstream.write(o_str)
# X1 = np.random.uniform(-1.0,1.0,N)
# X2 = np.random.uniform(-1.0,1.0,N)
# for i in range(len(F)):
#     o_str = str(X1[i]) + '\t' +str(X2[i]) + '\n'
#
#     ofstream.write(o_str)
#
#
#
# ofstream.close()
# axs = plotsurf(X,Y,f)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm

def plot_rect(ax, x_1, x_2, y_1, y_2, color):
    h_1 = x_2 - x_1
    h_2 = y_2 - y_1
    rect = matplotlib.patches.Rectangle((x_1, y_1), h_1, h_2, color=color)
    ax.add_patch(rect)

def plotsurf(x_vec, y_vec, func_):

    plt.rcParams["figure.figsize"] = [14, 7]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    axs = fig.add_subplot(111)

    rects_info = []

    x = []
    y = []
    highs = []

    for j in range(len(x_vec)-1):
        for k in range(len(y_vec)-1):
            x_1 = x_vec[j]
            x_2 = x_vec[j+1]
            y_1 = y_vec[k]
            y_2 = y_vec[k+1]
            x.append((x_2 + x_1) / 2)
            y.append((y_2 + y_1) / 2)
            rects_info.append([x_1, x_2, y_1, y_2])
            point_ = [(x_2 + x_1) / 2, (y_2 + y_1) / 2]
            highs.append(func_(point_))
    norm = matplotlib.colors.Normalize(vmin=min(highs), vmax=max(highs))
    m = cm.ScalarMappable(norm=norm, cmap=cm.viridis)

    tmp_len = len(rects_info)
    for i in range(len(rects_info)):
        # print("\r interation {} of {}".format(i, tmp_len), end='')
        plot_rect(axs, rects_info[i][0], rects_info[i][1], rects_info[i][2], rects_info[i][3],
                  m.to_rgba(highs[i]))
    print('')

    plt.colorbar(m, ax=axs)
    axs.set_xlim([-1.0, 1.0])
    axs.set_ylim([-1.0, 1.0])
    axs.set_xlabel(r"$x$")
    axs.set_ylabel(r'$y$')
    plt.title(r'$\varphi(x,y)$')

    # axs.scatter(x_, y_, color='r')
    # plot_graph2D(search_points, adj_matrix, axs,
    #              plot_vertexes=True,
    #              plot_edges=False)
    # plot_clusters(all_groups, list(clusters.keys()), axs, plot_edges=True)

    argmin_ = np.argmin(highs)
    print('min value = {} x= {}, y={}'.format(highs[argmin_], x[argmin_], y[argmin_]))

    print("plot response surface done")
    return axs

def f(p):
    x1 = p[0]
    x2 = p[1]
    x3 = p[2]
    x4 = p[3]
    x5 = p[4]
    return 1.0+ x1**2 +x2**2+x3**2+x4**2+x5**2+ x1*(x2+x3+x4+x5)

N = 1000
X1 = np.random.uniform(-1.0,1.0,N)
X2 = np.random.uniform(-1.0,1.0,N)
X3 = np.random.uniform(-1.0,1.0,N)
X4 = np.random.uniform(-1.0,1.0,N)
X5 = np.random.uniform(-1.0,1.0,N)

# Y = np.linspace(-1.0,1.0,100)
# X = np.linspace(-1.0,1.0,100)


F = [f(p)for p in zip(X1,X2,X3,X4,X5)]
ofstream = open('input.txt','w')
for i in range(len(F)):
    o_str = str(X1[i]) + '\t' +str(X2[i]) +'\t'+str(X3[i]) +'\t'+str(X4[i]) +'\t'+str(X5[i]) +'\t' +str(F[i]) +'\n'

    ofstream.write(o_str)
X1 = np.random.uniform(-1.0,1.0,N)
X2 = np.random.uniform(-1.0,1.0,N)
X3 = np.random.uniform(-1.0,1.0,N)
X4 = np.random.uniform(-1.0,1.0,N)
X5 = np.random.uniform(-1.0,1.0,N)
F = [f(p)for p in zip(X1,X2,X3,X4,X5)]
for i in range(len(F)):
    o_str = str(X1[i]) + '\t' +str(X2[i]) +'\t'+str(X3[i]) +'\t'+str(X4[i]) +'\t'+str(X5[i]) + '\t' +str(F[i]) +'\n'

    ofstream.write(o_str)



ofstream.close()
# axs = plotsurf(X,Y,f)
# plt.show()