import numpy as np

def find_theta(X, y):
	
	term  = np.matmul(X.transpose(), X)                # X transpose * X
	term1 = np.linalg.inv(term)
	term2 = np.matmul(X.transpose(), y)

	return np.matmul(term1, term2)


X = np.random.normal(0, 1, (20, 20))
y = np.random.randint(low=0, high=10, size=20)

Theta = find_theta(X, y)
print(Theta)
