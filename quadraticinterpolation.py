def quadratic_interpolation(f, x0, x1, x2):
    """
    Perform quadratic interpolation to estimate x3 based on the given formula.

    Parameters:
    f (function): The function f(x) to interpolate.
    x0, x1, x2 (float): Initial guesses.

    Returns:
    dict: Contains f(x0), f(x1), f(x2), and x3.
    """
    # Compute function values
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)

    # Compute numerator and denominator of x3
    numerator = (
        f0 * (x1**2 - x2**2)
        + f1 * (x2**2 - x0**2)
        + f2 * (x0**2 - x1**2)
    )
    denominator = (
        2 * f0 * (x1 - x2)
        + 2 * f1 * (x2 - x0)
        + 2 * f2 * (x0 - x1)
    )

    if denominator == 0:
        raise ValueError("Denominator is zero. Interpolation failed.")

    x3 = numerator / denominator

    return {
        "f(x0)": f0,
        "f(x1)": f1,
        "f(x2)": f2,
        "x3": x3
    }
