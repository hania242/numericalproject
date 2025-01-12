import numpy as np

def format_number(value):
    """
    Format a number to display either as a real or complex number depending on necessity.

    Parameters:
    value: The number to format.

    Returns:
    str: Formatted number as a string.
    """
    if np.isclose(value.imag, 0):
        return f"{value.real:.6g}"  # Display as real with up to 6 significant digits
    return f"{value:.6g}"  # Display as complex

def format_matrix(matrix):
    """
    Format a matrix to display its elements using format_number.

    Parameters:
    matrix: The matrix to format.

    Returns:
    list: Formatted matrix as a list of lists.
    """
    return [[format_number(value) for value in row] for row in matrix]

def cramers(A, b):
    """
    Solve a system of linear equations using Cramer's Rule with support for complex numbers.

    Parameters:
    A (numpy.ndarray): Coefficient matrix (2x2 or 3x3).
    b (numpy.ndarray): Constants vector.

    Returns:
    dict: Solutions for the system and intermediate steps.
    """
    # Validate input dimensions
    n = A.shape[0]
    if A.shape[1] != n or len(b) != n:
        raise ValueError("Matrix A must be square and match the size of vector b.")

    # Compute determinant of A
    det_A = np.linalg.det(A)
    if np.isclose(det_A, 0):
        raise ValueError("The determinant of A is zero. The system has no unique solution.")

    solutions = {}
    steps = {"det_A": format_number(det_A), "matrices": []}

    for i in range(n):
        # Create Ai by replacing the i-th column of A with b
        Ai = A.copy()
        Ai[:, i] = b
        det_Ai = np.linalg.det(Ai)

        # Store the intermediate matrix and determinant
        steps["matrices"].append({
            "column_replaced": i + 1,
            "matrix": format_matrix(Ai),
            "det_Ai": format_number(det_Ai)
        })

        # Calculate solution and format it
        solution = det_Ai / det_A
        solutions[f"x{i+1}"] = format_number(solution)

    return {"solutions": solutions, "steps": steps}

# Example Usage
if __name__ == "__main__":
    A = np.array([[2, -1], [1, 3]])
    b = np.array([1, 4])

    result = cramers(A, b)
    print("Solutions:", result["solutions"])
    print("Steps:", result["steps"])
