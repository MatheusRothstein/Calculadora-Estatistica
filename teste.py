from matplotlib import pyplot as plt
import numpy as np

def estimate_coef(x, y):
# number of observations/points
    n = np.size(x)

# mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

# calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)

# calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)

def plot_regression_line(xs, ys):
# dev stands for deviation
    dev = estimate_coef(xs, ys)

    y_pred = []
    for x in xs:
        y_pred.append(dev[0] + dev[1] * x)

# plotting the regression line
    plt.plot(xs, y_pred, color = "g")

def main():
# Defining points.
    xarr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    yarr = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]

# Setting points as numpy arrays.
# It is more convenient this way for further process.
    x = np.array(xarr)
    y = np.array(yarr)

# Plotting points.
    plt.scatter(x, y)

    plot_regression_line(x, y)
    plt.show()

if __name__ == "__main__":
    main()