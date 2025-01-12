import streamlit as st
import numpy as np
from cramers import cramers

def cramers_app():
    st.header("Cramer's Rule Solver")
    st.write("Solve systems of linear equations using Cramer's Rule. Supports real and complex numbers.")

    # Select matrix size
    size = st.selectbox("Select the size of the system:", [2, 3])

    # Input coefficient matrix
    st.write("Enter the coefficient matrix (A):")
    A = []
    rows_valid = True  # Flag to track whether all rows are valid
    user_started = False  # Check if user has clicked "Solve"

    # Store raw row inputs for later validation
    raw_rows = []
    for i in range(size):
        row = st.text_input(
            f"Row {i + 1} (use format a or a+bi for numbers):",
            placeholder="Example: 2 3+2i 4-5i"
        ).strip()
        raw_rows.append(row)

    # Input constants vector
    st.write("Enter the constants vector (b):")
    b_input = st.text_input(
        "b (use format a or a+bi for numbers):",
        placeholder="Example: 2 3+2i"
    ).strip()

    if st.button("Solve"):
        user_started = True  # User has clicked "Solve"

        # Process matrix A
        for i, row in enumerate(raw_rows):
            if row:  # Only process if row is not empty
                try:
                    A.append([
                        complex(x.strip().replace("i", "j")) if "i" in x else float(x.strip())
                        for x in row.split()
                    ])
                except ValueError:
                    st.error(f"Row {i + 1} contains invalid numbers. Please use the correct format.")
                    rows_valid = False
            else:
                st.error(f"Row {i + 1} cannot be empty.")
                rows_valid = False

        if rows_valid:
            try:
                A = np.array(A, dtype=complex)
            except ValueError as e:
                st.error(f"Matrix A input error: {e}")
                rows_valid = False

        # Process vector b
        b_valid = True
        if b_input:  # Only process if the input is not empty
            try:
                b = np.array([
                    complex(x.strip().replace("i", "j")) if "i" in x else float(x.strip())
                    for x in b_input.split()
                ], dtype=complex)
                if len(b) != size:
                    st.error(f"Vector b must have exactly {size} values.")
                    b_valid = False
            except ValueError as e:
                st.error(f"Constants vector (b) contains invalid numbers. Error: {e}")
                b_valid = False
        else:
            st.error("Constants vector (b) cannot be empty.")
            b_valid = False

        # Solve only if all inputs are valid
        if rows_valid and b_valid:
            try:
                # Solve using Cramer's Rule
                result = cramers(A, b)

                if "error" in result:
                    st.error(result["error"])
                else:
                    solutions = result["solutions"]
                    steps = result["steps"]

                    st.success("Solutions:")
                    for var, value in solutions.items():
                        st.write(f"{var} = {value}")

                    st.write("### Step-by-Step Process:")
                    st.write(f"Determinant of A: {steps['det_A']}")
                    for matrix_info in steps["matrices"]:
                        st.write(f"Matrix A_{matrix_info['column_replaced']}:")
                        st.write(np.array(matrix_info["matrix"]))
                        st.write(f"Det(A_{matrix_info['column_replaced']}) = {matrix_info['det_Ai']}")

            except Exception as e:
                st.error(f"An unexpected error occurred in computation: {e}")

if __name__ == "__main__":
    cramers_app()
