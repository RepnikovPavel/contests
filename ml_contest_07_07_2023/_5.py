import numpy as np
# from scipy.optimize import curve_fit
# from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import mean_absolute_error
# from scipy import odr
# import matplotlib.pyplot as plt

def get_features_of_poly(x:np.array,p,d)->np.array:
    features = np.zeros(shape=((p+1)**2 * (d-1)*d + (p+1)*d,))
    X = np.zeros(shape=(d, p+1), dtype=np.single)
    for i in range(d):
        for j in range(p+1):
            X[i][j] = np.power(x[i], j)
    l_ = 0
    for i in range(d):
        for u in range(p+1):
            features[l_] = X[i][u]
            l_+=1
        for j in range(d):
            if i!=j:
                # заф степень в первой строке
                for k in range(p+1):
                    # перебираем стeпени во  второй строке
                    for e in range(p+1):
                        features[l_] = X[i][k]*X[j][e]
                        l_ += 1
    return features

def transform_input(X:np.array,p,d)->np.array:
    output = np.zeros(shape=(len(X), (p+1)**2 * (d-1)*d + (p+1)*d))
    for i in range(len(X)):
        output[i] = get_features_of_poly(X[i],p,d)
    return output

if __name__ == '__main__':
    ifstream  = open('input.txt','r')
    ofstream  = open('output.txt','w')
    N = 1000
    dim = 5
    X_train = np.zeros(shape=(N, dim),dtype=np.single)
    Y_train = np.zeros(shape=(N,), dtype = np.single)
    for i in range(N):
        line = ifstream.readline().replace('\n', '').split('\t')
        for j in range(dim):
            X_train[i][j] = np.single(line[j])
        Y_train[i] = np.single(line[-1])
    # print(transform_input(X_train))
    # raise SystemExit
    # params = np.ones(shape=(195,), dtype = np.single)
    # poly = PolynomialFeatures(degree=2, include_bias=True)
    # poly_features = poly.fit_transform(X_train)
    # new_features =
    lr_model = LinearRegression()
    # poly_reg_model = odr.polynomial(2)
    # data = odr.Data(poly_features, Y_train)
    # X_ = transform_input(X_train,d=5,p=2)
    # beta = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X_), X_)),np.transpose(X_)),Y_train)


    lr_model.fit(transform_input(X_train,d=5,p=2), Y_train)
    # odr_obj = odr.ODR(data, poly_reg_model)
    # output = odr_obj.run()  # running ODR fitting
    # print(poly_reg_model.coef_)

    X_test = np.zeros(shape=(N, dim), dtype=np.single)
    # Y_test =  np.zeros(shape=(N,), dtype = np.single)
    for i in range(N):
        line = ifstream.readline().replace('\n', '').split('\t')
        for j in range(dim):
            X_test[i][j] = np.single(line[j])
        # Y_test[i] = np.single(line[-1])

    # def fitted_f(point):
    #     tr_ = get_features(transform_input([point]))
    #     ans_= lr_model.predict(tr_)
    #     return ans_[0]
    # from make_poly_dataset import plotsurf
    #
    # Y__ = np.linspace(-1.0,1.0,100)
    # X__ = np.linspace(-1.0,1.0,100)
    # plotsurf(X__,Y__,fitted_f)
    # plt.show()

    poly_reg_y_predicted = lr_model.predict(transform_input(X_test,d=5,p=2))
    # print(np.max(np.abs(Y_test-poly_reg_y_predicted)))

    for i in range(N):
        ofstream.write(str(poly_reg_y_predicted[i])+'\n')

    ifstream.close()
    ofstream.close()