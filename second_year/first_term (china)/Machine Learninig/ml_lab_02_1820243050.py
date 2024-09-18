import numpy as np

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris, make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def plot_decision_boundary(model, X, y) -> None:
    h = .02
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)


def main() -> None:
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_binary = X[y != 2]
    y_binary = y[y != 2]

    iris_model = SVC(kernel='linear')
    iris_model.fit(X_binary, y_binary)

    X_m, y_m = make_moons(n_samples=1000, noise=0.2, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(X_m, y_m, test_size=0.3,
                                                        random_state=42)

    moon_model = SVC(kernel='rbf', gamma='auto')
    moon_model.fit(X_train, y_train)

    for i in range(2):
        plt.scatter(X_binary[y_binary == i][:, 0], X_binary[y_binary == i][:, 1], label=f'True Class {i}', edgecolors='k') 

    plt.figure(figsize=(10, 6))
    plot_decision_boundary(moon_model, X_test, y_test)
    plt.show()


if __name__ == "__main__":
    main()
