import streamlit as st
import numpy as np
import pandas as pd
from sympy import sympify, lambdify, symbols
from secant import secant_method_fixed_iterations

def secant_method_app():
    st.header("Secant Method Solver")
    st.write("This app finds the root of f(x) = 0 using the Secant Method with a fixed number of iterations.")

    # Input for the function
    equation = st.text_input(
        "Enter the function f(x):",
        value="x**3 - x - 2",
        help="Use 'x' for the variable and '**' for exponents. Example: x**3 - x - 2"
    )

    # Inputs for x0, x1, and number of iterations
    x0 = st.number_input("Enter the initial guess x0:", value=1.0)
    x1 = st.number_input("Enter the initial guess x1:", value=2.0)
    iterations = st.number_input("Enter the number of iterations:", value=5, step=1)

    if st.button("Solve with Secant Method"):
        try:
            # Convert the function to a callable form
            x = symbols('x')
            symbolic_f = sympify(equation)
            f = lambdify(x, symbolic_f, modules=["numpy"])

            # Solve using the Secant Method
            result = secant_method_fixed_iterations(f, x0, x1, iterations)

            # Extract results
            root = result["root"]
            iteration_table = result["iterations"]

            # Display results
            st.success("Secant Method Completed!")
            st.write(f"Approximated root: {root:.6f}")
            st.write(f"f(root): {f(root):.6e}")

            # Display iteration table
            st.write("### Iteration Details:")
            df = pd.DataFrame(iteration_table)
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    secant_method_app()
