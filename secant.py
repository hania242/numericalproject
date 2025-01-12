def secant_method_fixed_iterations(f, x0, x1, iterations=10):
    """
    Perform the Secant Method with a fixed number of iterations to solve f(x) = 0.

    Parameters:
    f (function): The function for which the root is being calculated.
    x0 (float): Initial guess x0.
    x1 (float): Initial guess x1.
    iterations (int): Number of iterations to perform.

    Returns:
    dict: Contains the root approximation, iteration details, and the function value at each step.
    """
    iteration_details = []

    for i in range(iterations):
        # Calculate f(x0) and f(x1)
        fx0 = f(x0)
        fx1 = f(x1)

        # Avoid division by zero
        if fx1 - fx0 == 0:
            raise ValueError("Division by zero encountered in the Secant Method.")

        # Calculate x2
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

        # Store iteration details
        iteration_details.append({
            "Iteration": i + 1,
            "x0": x0,
            "f(x0)": fx0,
            "x1": x1,
            "f(x1)": fx1,
            "x2": x2,
            "f(x2)": f(x2),
        })

        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x2

    return {
        "root": x2,
        "iterations": iteration_details
    }
