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
    if isinstance(value, complex):  # Check if the number is complex
        # If the imaginary part is effectively zero, display as a real number
        if np.isclose(value.imag, 0):
            return f"{value.real:.3f}".rstrip('0').rstrip('.')  # Remove trailing zeros if real
        # Otherwise, display as a complex number
        real_part = f"{value.real:.3f}".rstrip('0').rstrip('.')
        imag_part = f"{value.imag:+.3f}".rstrip('0').rstrip('.')
        return f"{real_part}{imag_part}i"
    else:
        # For purely real numbers, ensure trailing zeros are stripped
        return f"{value:.3f}".rstrip('0').rstrip('.')





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
    dict: Solutions for the system and intermediate steps or an error message.
    """
    try:
        # Validate input dimensions
        n = A.shape[0]
        if A.shape[1] != n or len(b) != n:
            return {"error": "Matrix A must be square and match the size of vector b."}

        # Compute determinant of A
        det_A = np.linalg.det(A)
        if np.isclose(det_A, 0):
            return {"error": "The determinant of A is zero or very close to zero. The system has no unique solution."}

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

    except ValueError as e:
        # Handle input validation errors
        return {"error": f"Input validation error: {e}"}

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": f"Unexpected computation error: {e}"}
