def mat_dims(M):
    return (len(M), len(M[0]))


def mat_add(A, B):
    if mat_dims(A) != mat_dims(B):
        raise ValueError("Matrices must have the same dimensions")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scalar_mul(k, A):
    return [[k * x for x in row] for row in A]


def mat_mul(A, B):
    m, n = mat_dims(A)
    n2, p = mat_dims(B)
    if n != n2:
        raise ValueError("Inner dimensions must match: columns of A = rows of B")
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)]
            for i in range(m)]


if __name__ == "__main__":
    A = [[2, -1], [0, 3]]
    B = [[1, 4], [-2, 5]]
    C = [[1, 2, 3], [4, 5, 6]]
    D = [[1, 0], [0, 1], [2, 2]]
    print(mat_add(A, B))        # expect [[3, 3], [-2, 8]]
    print(scalar_mul(3, A))     # expect [[6, -3], [0, 9]]
    print(mat_mul(A, B))        # expect [[4, 3], [-6, 15]]
    print(mat_mul(B, A))        # expect [[2, 11], [-4, 17]]
    print(mat_mul(C, D))        # expect [[7, 8], [16, 17]]
    try:
        mat_add(C, D)
    except ValueError as e:
        print("Caught:", e)

    # Verify with NumPy (optional)
    import numpy as np
    print(np.array_equal(np.array(mat_mul(A, B)), np.array(A) @ np.array(B)))   # True