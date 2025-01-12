import streamlit as st
import numpy as np

def format_number(value):
    """Format a number to show decimals only when needed."""
    if np.isclose(value, int(value)):
        return f"{int(value)}"  # Show as integer if value is close to an integer
    else:
        return f"{value:.3f}"  # Show with 3 decimals otherwise

def format_matrix(matrix):
    """Format a matrix to display its elements."""
    return [[format_number(value) for value in row] for row in matrix]

def lu_decomposition(A, b):
    """Perform LU decomposition and solve the system of linear equations."""
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    steps = []

    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        for j in range(i, n):
            if i == j:
                L[i, i] = 1
            else:
                L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

        steps.append({
            "Step": f"After processing row {i + 1}",
            "L": L.copy(),
            "U": U.copy()
        })

    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, k] * y[k] for k in range(i)))

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, k] * x[k] for k in range(i + 1, n))) / U[i, i]

    return {"L": format_matrix(L), "U": format_matrix(U), "x": format_matrix([x])[0], "steps": steps, "y": format_matrix([y])[0]}

def lu_app():
    st.header("LU Decomposition and Advanced Options")
    st.write("Decompose a matrix into Lower (L) and Upper (U) triangular matrices, and choose an operation.")

    # Matrix size input
    size = st.number_input("Matrix size (n x n):", min_value=2, max_value=10, value=3)

    # Initialize error message variable
    error_message = ""

    # Input for matrix A
    A = []
    for i in range(int(size)):
        row = st.text_input(f"Row {i + 1} of A (use commas to separate values):")
        if row:
            try:
                A.append([float(x.strip()) for x in row.split(",")])
            except ValueError:
                error_message = f"Invalid values in Row {i + 1}. Please enter numbers only."
                break

    if len(A) != int(size):  # Check if all rows are entered
        error_message = "Please enter all rows for matrix A."

    # Input for vector b
    b_input = st.text_input("Enter the constants vector (b):")
    b = []
    if b_input:
        try:
            b = [float(x.strip()) for x in b_input.split(",")]
            if len(b) != int(size):
                error_message = "The length of vector b must match the matrix size."
        except ValueError:
            error_message = "Invalid values in vector b. Please enter numbers only."

    # If no errors, perform LU decomposition
    if not error_message and len(A) == int(size) and len(b) == int(size):
        A = np.array(A)
        b = np.array(b)
        result = lu_decomposition(A, b)
        st.write("L Matrix:")
        st.write(result["L"])
        st.write("U Matrix:")
        st.write(result["U"])
        st.write("y Vector:")
        st.write(result["y"])
        st.write("x Vector (Solution):")
        st.write(result["x"])
        for step in result["steps"]:
            st.write(step["Step"])
            st.write("L:")
            st.write(step["L"])
            st.write("U:")
            st.write(step["U"])
    else:
        # Display error message under the relevant input field
        if error_message:
            st.error(error_message)

if __name__ == "__main__":
    lu_app()
