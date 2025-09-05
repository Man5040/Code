
import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

x, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
plt.scatter(x[:,0], y) # Scatter plot of the data points

y = y.reshape(y.shape[0], 1)  # Reshape y to be a 2D array

#Matrix X
X = np.hstack((x, np.ones((x.shape[0],1))))  # Add a bias term

theta = np.random.rand(3, 1)  # Initialize theta with random values

#Define the model function




