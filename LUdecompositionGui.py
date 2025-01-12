import streamlit as st
import numpy as np
from LUdecomposition import lu_decomposition


def lu_app():
    st.header("LU Decomposition and Advanced Options")
    st.write("Decompose a matrix into Lower (L) and Upper (U) triangular matrices, and choose an operation.")

    # Input matrix
    st.write("Enter the square matrix (A):")
    size = st.number_input("Matrix size (n x n):", min_value=2, max_value=10, value=3)
    A = []
    for i in range(int(size)):
        row = st.text_input(f"Row {i + 1} of A (use commas to separate values):", value=", ".join(["1"] * int(size)))
        A.append([float(x.strip()) for x in row.split(",")])
    A = np.array(A)

    # Dropdown menu for operation selection
    operation = st.selectbox(
        "Choose an operation:",
        ["Solve Ax = b", "Compute a column of A inverse"]
    )

    if operation == "Solve Ax = b":
        # Input constants vector b
        st.write("Enter the constants vector (b):")
        b_input = st.text_input("Vector b (use commas to separate values):", value=", ".join(["1"] * int(size)))
        b = np.array([float(x.strip()) for x in b_input.split(",")])

        if st.button("Decompose and Solve"):
            try:
                # Perform LU decomposition and solve
                result = lu_decomposition(A, b)
                L, U, x, y, steps = result["L"], result["U"], result["x"], result["y"], result["steps"]

                st.success("LU Decomposition Completed:")
                st.write("Lower Triangular Matrix (L):")
                st.write(L)
                st.write("Upper Triangular Matrix (U):")
                st.write(U)

                st.write("### Step-by-Step Forward Substitution (L * y = b):")
                for i in range(len(y)):
                    st.write(f"Step {i + 1}:")
                    st.write("Matrix L (current state):")
                    st.write(L[:i + 1, :i + 1])  # Submatrix of L being used
                    st.write("Vector b:")
                    st.write(b[:i + 1])  # Relevant portion of b
                    st.write("Intermediate Vector y:")
                    st.write(y[:i + 1])  # Partial solution for y

                st.write("### Step-by-Step Backward Substitution (U * x = y):")
                for i in range(len(x) - 1, -1, -1):
                    st.write(f"Step {len(x) - i}:")
                    st.write("Matrix U (current state):")
                    st.write(U[i:, i:])  # Submatrix of U being used
                    st.write("Vector y:")
                    st.write(y[i:])  # Relevant portion of y
                    st.write("Intermediate Vector x:")
                    st.write(x[i:])  # Partial solution for x

                # Final solutions
                st.success("Solution to Ax = b:")
                st.write("Intermediate Solution (y):")
                st.write(y)
                st.write("Final Solution (x):")
                st.write(x)

            except Exception as e:
                st.error(f"Error: {e}")

    elif operation == "Compute a column of A inverse":
        # Select column number to compute
        col_index = st.number_input(
            "Choose the column of the inverse to compute (1-based index):",
            min_value=1,
            max_value=size,
            value=1
        ) - 1  # Convert to 0-based index

        if st.button("Decompose and Compute Column"):
            try:
                # Identity matrix
                I = np.eye(size)
                b = I[:, col_index]  # Take the corresponding column of the identity matrix

                # Perform LU decomposition and solve for this column
                result = lu_decomposition(A, b)
                L, U, x, y, steps = result["L"], result["U"], result["x"], result["y"], result["steps"]

                st.success("LU Decomposition Completed:")
                st.write("Lower Triangular Matrix (L):")
                st.write(L)
                st.write("Upper Triangular Matrix (U):")
                st.write(U)

                st.write(f"### Step-by-Step Computation of Column {col_index + 1} of A Inverse:")
                st.write("#### Forward Substitution (L * y = b):")
                for i in range(len(y)):
                    st.write(f"Step {i + 1}:")
                    st.write("Matrix L (current state):")
                    st.write(L[:i + 1, :i + 1])  # Submatrix of L being used
                    st.write("Vector b (Identity column):")
                    st.write(b[:i + 1])  # Relevant portion of b
                    st.write("Intermediate Vector y:")
                    st.write(y[:i + 1])  # Partial solution for y

                st.write("#### Backward Substitution (U * x = y):")
                for i in range(len(x) - 1, -1, -1):
                    st.write(f"Step {len(x) - i}:")
                    st.write("Matrix U (current state):")
                    st.write(U[i:, i:])  # Submatrix of U being used
                    st.write("Vector y:")
                    st.write(y[i:])  # Relevant portion of y
                    st.write("Intermediate Vector x:")
                    st.write(x[i:])  # Partial solution for x

                # Final solution
                st.success(f"Column {col_index + 1} of A Inverse:")
                st.write(x)

            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    lu_app()
