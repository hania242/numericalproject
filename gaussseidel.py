import numpy as np
def gauss_seidel_fixed_iterations(A, b, initial_guess=None, iterations=10):
    """
    Perform the Gauss-Seidel method with a fixed number of iterations to solve Ax = b.

    Parameters:
    A (2D array): Coefficient matrix.
    b (1D array): Constant vector.
    initial_guess (1D array): Initial guess for the solution (default is a zero vector).
    iterations (int): Number of iterations to perform.

    Returns:
    dict: Contains the solution and iteration details.
    """
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64) if initial_guess is None else np.array(initial_guess, dtype=np.float64)
    iteration_details = []

    for iteration in range(iterations):
        x_old = x.copy()

        for i in range(n):
            # Compute the sum for all elements except the current one
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            # Update x[i] using the most recent values
            x[i] = (b[i] - sigma) / A[i][i]

        # Compute percentage errors for each variable
        errors = np.zeros_like(x)
        for i in range(n):
            if x[i] != 0:  # Avoid division by zero
                errors[i] = abs((x[i] - x_old[i]) / x[i]) * 100
            else:
                errors[i] = 0

        # Set errors to 100% for the first iteration
        if iteration == 0:
            errors[:] = 100

        # Store details of this iteration
        iteration_details.append({
            "Iteration": iteration + 1,
            "x1": x[0],
            "x2": x[1],
            "x3": x[2] if n == 3 else None,
            "Ea1": errors[0],
            "Ea2": errors[1],
            "Ea3": errors[2] if n == 3 else None,
        })

    return {
        "solution": x,
        "iterations": iteration_details
    }
