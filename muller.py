import numpy as np

def muller(f, x0, x1, x2, max_iter=10, true_root=None):
    """
    Muller method with step-by-step details, formatting complex outputs, and error calculations.

    Parameters:
    f (function): The function for which roots are to be found.
    x0, x1, x2 (complex): Initial guesses for the root (can be real or complex).
    max_iter (int): Maximum number of iterations.
    true_root (complex, optional): The true root for calculating Et.

    Returns:
    list: A list of dictionaries containing intermediate values for each iteration.
    """
    steps = []

    def format_number(num):
        """Converts a complex number to real if imaginary part is negligible."""
        if np.isclose(num.imag, 0):
            return num.real
        return num

    for i in range(max_iter):
        h0 = x1 - x0
        h1 = x2 - x1
        s0 = (f(x1) - f(x0)) / h0
        s1 = (f(x2) - f(x1)) / h1

        a = (s1 - s0) / (h1 + h0)
        b = a * h1 + s1
        c = f(x2)

        discriminant = np.sqrt(b**2 - 4 * a * c)
        x3 = x2 - (2 * c) / (b + np.sign(b.real) * discriminant)
        fx3 = f(x3)

        # Calculate errors
        Ea = None
        Et = None
        if i > 0:  # Ea can only be calculated after the first iteration
            Ea = abs((x3 - x2) / x3) * 100
        if true_root is not None:  # Et requires a known true root
            Et = abs((true_root - x3) / true_root) * 100

        # Store all calculated values for this iteration, formatting numbers
        steps.append({
            "iteration": i + 1,
            "h0": format_number(h0),
            "h1": format_number(h1),
            "s0": format_number(s0),
            "s1": format_number(s1),
            "a": format_number(a),
            "b": format_number(b),
            "c": format_number(c),
            "x3": format_number(x3),
            "f(x3)": format_number(fx3),
            "Ea (%)": format_number(Ea) if Ea is not None else None,
            "Et (%)": format_number(Et) if Et is not None else None,
        })

        # Update guesses for the next iteration
        x0, x1, x2 = x1, x2, x3

    return steps
