import numpy as np

def lu_decomposition(A, b):
    """
    Perform LU decomposition of a square matrix A using Doolittle's method,
    and solve for x in Ax = b using the decomposed matrices L and U.

    Parameters:
    A (numpy.ndarray): The input square matrix.
    b (numpy.ndarray): The constants vector.

    Returns:
    dict: Contains L, U matrices, x, and step-by-step decomposition details.
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    steps = []

    # LU Decomposition
    for i in range(n):
        # Upper Triangular Matrix U
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        # Lower Triangular Matrix L
        for j in range(i, n):
            if i == j:
                L[i, i] = 1  # Diagonal as 1
            else:
                L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

        # Store intermediate matrices
        steps.append({
            "Step": f"After processing row {i + 1}",
            "L": L.copy(),
            "U": U.copy()
        })

    # Forward substitution to solve L * y = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, k] * y[k] for k in range(i)))

    # Backward substitution to solve U * x = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, k] * x[k] for k in range(i + 1, n))) / U[i, i]

    return {"L": L, "U": U, "x": x, "steps": steps, "y": y}
