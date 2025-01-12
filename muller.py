import numpy as np

def muller(f, x0, x1, x2, max_iter=10, true_root=None):
    """
    Muller method with step-by-step details, formatting outputs, and error calculations.

    Parameters:
    f (function): The function for which roots are to be found.
    x0, x1, x2 (complex): Initial guesses for the root (can be real or complex).
    max_iter (int): Maximum number of iterations.
    true_root (complex, optional): The true root for calculating Et.

    Returns:
    list: A list of dictionaries containing intermediate values for each iteration or an error message.
    """
    try:
        steps = []

        def format_number(num):
            """
            Converts a complex number to formatted string with 3 decimal places.
            Replaces `j` with `i` for complex numbers.
            """
            if np.isclose(num.imag, 0):  # Check if it's approximately real
                return f"{num.real:.3f}"  # Format real part
            return f"{num:.3f}".replace("j", "i")  # Format complex number with small 'i'

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

            # Store all calculated values for this iteration
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
                "Ea (%)": f"{Ea:.3f}" if Ea is not None else None,
                "Et (%)": f"{Et:.3f}" if Et is not None else None,
            })

            # Update guesses for the next iteration
            x0, x1, x2 = x1, x2, x3

        return steps

    except Exception:
        # Return a user-friendly error message if something goes wrong
        return {"error": "An error occurred during the Muller calculation. Please check your inputs."}


# Example Usage
if __name__ == "__main__":
    try:
        # Define the function
        def f(x):
            return x**3 - 6*x + 8

        # Initial guesses
        x0 = complex(0)
        x1 = complex(1)
        x2 = complex(2)

        # Maximum iterations
        max_iter = 10

        # Run Muller method
        result = muller(f, x0, x1, x2, max_iter=max_iter)

        # Display results
        if isinstance(result, dict) and "error" in result:
            print(result["error"])
        else:
            for step in result:
                print(step)
    except Exception as e:
        print("An unexpected error occurred. Please contact support.")
