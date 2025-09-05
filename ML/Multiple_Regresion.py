
import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

#Set database
x, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
y = y + abs(y/2) # Introduce some non-linearity
plt.scatter(x, y) 
y = y.reshape(-1, 1)  # Reshape y to be a 2D array

#Matrix X
X = np.hstack((x, np.ones(x.shape)))  # Add a bias term
X = np.hstack((X, x**2))  # Add a quadratic term
theta = np.random.rand(3, 1)  # Initialize theta with random values

#Define the model function
def model(X, theta):
    return X.dot(theta)

# Define the cost function
def cost_function(X, y, theta):
    m = len(y)
    predictions = model(X, theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

cost_function(X, y, theta)

# Define the gradient descent function
def grad(X, y, theta):
    m = len(y)
    predictions = model(X, theta)
    gradient = (1 / m) * X.T.dot(predictions - y)
    return gradient

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    for i in range(n_iterations):
        gradient = grad(X, y, theta)
        theta -= learning_rate * gradient
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history

theta_final = gradient_descent(X, y, theta, learning_rate=0.01, n_iterations=1000)

y_pred = model(X, theta_final)