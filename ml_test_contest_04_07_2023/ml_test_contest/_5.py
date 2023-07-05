import numpy as np
# from scipy.optimize import curve_fit
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import odr
import matplotlib.pyplot as plt
def func(x: np.array, params: np.array):
    # params 1x195
    # x 1x5
    X =  np.zeros(shape=(5, 3), dtype=np.single)
    for i in range(5):
        for j in range(3):
            X[i][j] = np.power(x[i], j)

    f_ = 0.0
    l_=0
    for i in range(5):
        for u in range(3):
            f_ += params[l_]*X[i][u]
            l_+=1
        for j in range(5):
            if i!=j:
                # заф степень в первой строке
                for k in range(3):
                    # перебираем стeпени во  второй строке
                    for p in range(3):
                        f_ += params[l_]*X[i][k]*X[j][p]
                        l_ += 1
    return f_

if __name__ == '__main__':
    ifstream  = open('input.txt','r')
    ofstream  = open('output.txt','w')
    N = 100000
    dim = 5
    X_train = np.zeros(shape=(N, dim),dtype=np.single)
    Y_train = np.zeros(shape=(N,), dtype = np.single)
    for i in range(N):
        line = ifstream.readline().replace('\n', '').split('\t')
        for j in range(dim):
            X_train[i][j] = np.single(line[j])
        Y_train[i] = np.single(line[-1])
    # params = np.ones(shape=(195,), dtype = np.single)
    poly = PolynomialFeatures(degree=2, include_bias=True)
    poly_features = poly.fit_transform(X_train)
    poly_reg_model = LinearRegression()
    # poly_reg_model = odr.polynomial(2)
    # data = odr.Data(poly_features, Y_train)
    poly_reg_model.fit(poly_features, Y_train)
    # odr_obj = odr.ODR(data, poly_reg_model)
    # output = odr_obj.run()  # running ODR fitting
    # print(poly_reg_model.coef_)


    X_test = np.zeros(shape=(N, dim), dtype=np.single)
    for i in range(N):
        line = ifstream.readline().replace('\n', '').split('\t')
        for j in range(dim):
            X_test[i][j] = np.single(line[j])

    # def fitted_f(point):
    #     tr_ = poly.transform([point])
    #     ans_= poly_reg_model.predict(tr_)
    #     return ans_[0]
    # from make_poly_dataset import plotsurf
    #
    # Y__ = np.linspace(-1.0,1.0,100)
    # X__ = np.linspace(-1.0,1.0,100)
    # plotsurf(X__,Y__,fitted_f)
    # plt.show()

    poly_reg_y_predicted = poly_reg_model.predict(poly.transform(X_test))
    print(np.sqrt(mean_squared_error(Y_train, poly_reg_y_predicted)))

    for i in range(N):
        ofstream.write(str(poly_reg_y_predicted[i])+'\n')

    ifstream.close()
    ofstream.close()