
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

#Set database
x, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
plt.scatter(x, y) 

y = y.reshape(y.shape[0], 1)  # Reshape y to be a 2D array

print("x shape:", x.shape)
print("y shape:", y.shape)

X = np.hstack((x, np.ones(x.shape)))  # Add a bias term

theta = np.random.rand(2, 1)  # Initialize theta with random values


# Define the model function
def model(X, theta):
    return X.dot(theta)

plt.scatter(x, y)
plt.plot(x, model(X,theta), c="Red")


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
    cost_history = np.zeros
    for _ in range(n_iterations):
        gradient = grad(X, y, theta)
        theta -= learning_rate * gradient
        cost_history = cost_function(X, y, theta)
    return theta, cost_history


#Run
theta_final = gradient_descent(X, y, theta, learning_rate=0.01, n_iterations=1000)
theta_final

predictions = model(X, theta_final)
plt.scatter(x, y)
plt.plot(x, predictions, c="Red")


#Learning curve
##plt.plot(np.arange(1000), cost_history)


#Coefficient of determination (R^2)
def coef_determination(y, predictions):
    u = np.sum((y - predictions) ** 2)
    v = np.sum((y - np.mean(y)) ** 2)
    return 1 - (u / v)
