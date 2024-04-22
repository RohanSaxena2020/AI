import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import math

def gradient_descent(x,y):
    m_curr = 0
    b_curr = 0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0002

    cost_previous = 0

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([value**2 for value in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print ("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost, i))

    return m_curr, b_curr

df = pd.read_csv("3_gradient_descent/Exercise/test_scores.csv")

x = np.array(df.math)
y = np.array(df.cs)

# Usage example, ensure df columns are clean and appropriate for input
gradient_descent(x, y)

from sklearn import linear_model

reg = linear_model.LinearRegression()
# Reshape the 'math' column to be 2-dimensional
x = df[['math']]  # This keeps it as a DataFrame
y = df['cs']

reg.fit(x, y)

print(reg.coef_)

print(reg.intercept_)