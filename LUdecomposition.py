import numpy as np

def format_number(value):
    """
    Format a number to display either as a real or complex number depending on necessity.
    It will display decimals only when needed.
    
    Parameters:
    value: The number to format.
    
    Returns:
    str: Formatted number as a string.
    """
    if np.isclose(value, int(value)):
        return f"{int(value)}"  # Show as integer if value is close to an integer
    else:
        return f"{value:.3f}"  # Show with 3 decimals otherwise

def format_matrix(matrix):
    """
    Format a matrix to display its elements using format_number.

    Parameters:
    matrix: The matrix to format.

    Returns:
    list: Formatted matrix as a list of lists.
    """
    return [[format_number(value) for value in row] for row in matrix]

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
            "L": format_matrix(L),
            "U": format_matrix(U)
        })

    # Forward substitution to solve L * y = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, k] * y[k] for k in range(i)))

    # Backward substitution to solve U * x = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, k] * x[k] for k in range(i + 1, n))) / U[i, i]

    # Return formatted results
    return {"L": format_matrix(L), "U": format_matrix(U), "x": format_matrix([x])[0], "steps": steps, "y": format_matrix([y])[0]}

# Example Usage
if __name__ == "__main__":
    A = np.array([[2.0, -1.0, -2.0], [-4.0, 6.0, 3.0], [-4.0, -2.0, 8.0]])
    b = np.array([3.0, 9.0, -2.0])

    result = lu_decomposition(A, b)
    print("L Matrix:")
    print(result["L"])
    print("U Matrix:")
    print(result["U"])
    print("y Vector:")
    print(result["y"])
    print("x Vector (Solution):")
    print(result["x"])
    for step in result["steps"]:
        print(step["Step"])
        print("L:")
        print(step["L"])
        print("U:")
        print(step["U"])
