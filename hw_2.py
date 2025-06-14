import numpy as np

def power_iterations(A, max_iterations=1000, tol=1e-10):
    n, i = A.shape
    b_k = np.random.rand(n)
    b_k = b_k / np.linalg.norm(b_k)

    for i in range(max_iterations):
        b_k1 = A @ b_k
        b_k1_norm = np.linalg.norm(b_k1)
        b_k1 = b_k1 / b_k1_norm

        if np.linalg.norm(b_k1 - b_k) < tol:
            break

        b_k = b_k1

        lambda_max = A @ b_k.T @ b_k

    return lambda_max, b_k1

A = np.array([[2, 1], [1, 3]])
lambda_max, eigenvector = power_iterations(A)
print("Maximum eigen value\n")
print(lambda_max)
print("Eigen vectors:\n")
print(eigenvector)