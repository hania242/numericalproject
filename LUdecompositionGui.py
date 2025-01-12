import streamlit as st
import numpy as np
from LUdecomposition import lu_decomposition

def lu_app():
    st.header("LU Decomposition and Advanced Options")
    st.write("Decompose a matrix into Lower (L) and Upper (U) triangular matrices, and choose an operation.")

    # Input matrix
    st.write("Enter the square matrix (A) (supports complex numbers in a+bi format):")
    size = st.number_input("Matrix size (n x n):", min_value=2, max_value=10, value=3)

    A = []
    b = None  # Initialize constants vector
    operation = None
    errors = []  # Collect errors only after the button is clicked

    # Collect rows of the matrix
    for i in range(int(size)):
        row = st.text_input(
            f"Row {i + 1} of A (use spaces to separate values):",
            placeholder="e.g., 1+2i 3 4-5i"
        )
        A.append(row)

    # Dropdown menu for operation selection
    operation = st.selectbox(
        "Choose an operation:",
        ["Solve Ax = b", "Compute a column of A inverse"]
    )

    # Input for vector b if the user selects "Solve Ax = b"
    if operation == "Solve Ax = b":
        b_input = st.text_input("Vector b (use spaces to separate values):", placeholder="e.g., 4+3i 5 6-2i")

    # Process inputs and perform calculations only after the button is clicked
    if st.button("Decompose and Solve"):
        errors = []  # Reset errors for each button click
        matrix = []  # To hold parsed matrix values

        # Validate matrix input
        for i, row in enumerate(A):
            if row.strip():
                try:
                    values = [complex(x.strip().replace("i", "j")) for x in row.split(" ")]
                    if len(values) != size:
                        errors.append(f"Row {i + 1} must have exactly {size} values.")
                    else:
                        matrix.append(values)
                except ValueError:
                    errors.append(f"Invalid input in Row {i + 1}. Please ensure correct formatting.")
            else:
                errors.append(f"Row {i + 1} cannot be empty.")

        if len(matrix) == size and not errors:
            A = np.array(matrix, dtype=complex)

        # Validate vector b if the user selected "Solve Ax = b"
        if operation == "Solve Ax = b":
            if b_input.strip():
                try:
                    b = [complex(x.strip().replace("i", "j")) for x in b_input.split(" ")]
                    if len(b) != size:
                        errors.append(f"Vector b must have exactly {size} values.")
                    else:
                        b = np.array(b, dtype=complex)
                except ValueError:
                    errors.append("Invalid input for vector b. Please ensure correct formatting.")
            else:
                errors.append("Constants vector (b) cannot be empty.")

        # Show errors if any
        if errors:
            for error in errors:
                st.error(error)
            return

        # Perform calculations if there are no errors
        try:
            if operation == "Solve Ax = b":
                result = lu_decomposition(A, b)
                L, U, x, y, steps = result["L"], result["U"], result["x"], result["y"], result["steps"]

                st.success("LU Decomposition Completed:")
                st.write("Lower Triangular Matrix (L):")
                st.write(np.array(L))
                st.write("Upper Triangular Matrix (U):")
                st.write(np.array(U))

                st.success("Solution to Ax = b:")
                st.write("Intermediate Solution (y):")
                st.write(np.array(y))
                st.write("Final Solution (x):")
                st.write(np.array(x))

            elif operation == "Compute a column of A inverse":
                col_index = st.number_input(
                    "Choose the column of the inverse to compute (1-based index):",
                    min_value=1,
                    max_value=size,
                    value=1
                ) - 1  # Convert to 0-based index

                I = np.eye(size, dtype=complex)
                b = I[:, col_index]  # Take the corresponding column of the identity matrix

                result = lu_decomposition(A, b)
                L, U, x, y, steps = result["L"], result["U"], result["x"], result["y"], result["steps"]

                st.success("LU Decomposition Completed:")
                st.write("Lower Triangular Matrix (L):")
                st.write(np.array(L))
                st.write("Upper Triangular Matrix (U):")
                st.write(np.array(U))

                st.success(f"Column {col_index + 1} of A Inverse:")
                st.write(np.array(x))

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    lu_app()
