import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm
N = 1000

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


def f(x1,x2):
    return 1.0 + np.square(x1) + np.square(x2) + x1*x2



X1 = np.random.uniform(-1.0,1.0,N)
X2 = np.random.uniform(-1.0,1.0,N)
X_train = np.array([[
  X1[i], X2[i]
] for i in range(N)])

Y_train = [f(p[0], p[1]) for p in zip(X1, X2)]

lr_model = LinearRegression()
lr_model.fit(transform_input(X_train,d=2,p=2), Y_train)
poly_reg_y_predicted = lr_model.predict(transform_input(X_train,d=2,p=2))


x_vec = np.linspace(-1.0, 1.0, N)
y_vec = np.linspace(-1.0, 1.0, N)
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={"projection": "3d"})

X, Y = np.meshgrid(x_vec, y_vec)
Z = f(X, Y)
surf = axs[0][0].plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

X1test = np.random.uniform(-1.0,1.0,N)
X2test = np.random.uniform(-1.0,1.0,N)
X_test = np.array([[
  X1test[i], X2test[i]
] for i in range(N)])
Y_test = [f(p[0], p[1]) for p in zip(X1test, X2test)]
Y_pred = lr_model.predict(transform_input(X_test,d=2,p=2))
print(np.sqrt(mean_squared_error(Y_test, Y_pred)))

axs[0][1].scatter(X1test,X2test,Y_pred)
axs[0][1].set_title('on test data')

# axs[0][0].colorbar(surf, shrink=0.5, aspect=5)
plt.show()


X1 = np.random.uniform(-1.0,1.0,N)
X2 = np.random.uniform(-1.0,1.0,N)
Y_test = [f(p[0],p[1]) for p in zip(X1,X2)]








