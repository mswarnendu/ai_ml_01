import numpy as np

def householder_reflections(A):
  A = A.astype(float)
  m, n = A.shape
  Q = np.eye(m)

  for i in range(n):
    x = A[i:, i]
    norm_x = np.linalg.norm(x)
    if norm_x == 0:
      continue

    sign = -1 if x[0] < 0 else 1
    v = x.copy()
    u1 = x[0] + sign * norm_x
    v[0] = u1
    v = v / np.linalg.norm(v)

    H = np.eye(m)
    H[i:, i:] =- 2.0 * np.outer(v, v)

    A = H @ A
    Q = Q @ H

    R = A
    return Q, H

A = np.array([[12, -51], [6, 167]])
Q, R = householder_reflections(A)

np.set_printoptions(precision=4, suppress=True)
print("A:\n")
print(A)
print("Q\n")
print(Q)
print("R:\n")
print(R)


    