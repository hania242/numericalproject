import streamlit as st
import numpy as np
import pandas as pd
from gaussseidel import gauss_seidel_fixed_iterations

def gauss_seidel_app():
    st.header("Gauss-Seidel Method Solver")
    st.write("This app solves 2x2 or 3x3 systems of linear equations using the Gauss-Seidel method with a fixed number of iterations.")

    # Input for the coefficient matrix (A)
    A_input = st.text_area(
        "Enter the coefficient matrix (A):",
        value="4 -1 0\n-1 4 -1\n0 -1 3",
        help="Enter the rows of the matrix, separated by newlines. Separate elements in a row by spaces."
    )

    # Input for the constant vector (b)
    b_input = st.text_area(
        "Enter the constant vector (b):",
        value="15\n10\n10",
        help="Enter the elements of the vector, separated by newlines."
    )

    # Initial guess
    initial_guess_input = st.text_input(
        "Enter the initial guess (optional, default is zero):",
        value="0,0,0",
        help="Enter the initial guess as a comma-separated list (e.g., 0,0,0)."
    )

    # Input for the number of iterations
    iterations = st.number_input("Enter the number of iterations:", value=10, step=1)

    if st.button("Solve with Gauss-Seidel Method"):
        try:
            # Parse inputs
            A = np.array([[float(num) for num in row.split()] for row in A_input.strip().split("\n")])
            b = np.array([float(num) for num in b_input.strip().split("\n")])
            initial_guess = [float(num) for num in initial_guess_input.split(",")]

            # Validate input dimensions
            if A.shape[0] != A.shape[1]:
                raise ValueError("Matrix A must be square.")
            if len(b) != A.shape[0]:
                raise ValueError("Vector b must have the same number of rows as matrix A.")

            # Solve using Gauss-Seidel
            result = gauss_seidel_fixed_iterations(A, b, initial_guess, iterations)

            # Extract results
            solution = result["solution"]
            iterations = result["iterations"]

            # Display results
            st.success("Gauss-Seidel Method Completed!")
            st.write("Solution:")
            for i, value in enumerate(solution):
                st.write(f"x{i + 1} = {value:.6f}")

            # Display iteration table
            st.write("### Iteration Details:")
            df = pd.DataFrame(iterations)
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    gauss_seidel_app()
