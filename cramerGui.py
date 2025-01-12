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
    for i in range(size):
        row = st.text_input(f"Row {i+1} (use format a+bj for complex numbers):", value=", ".join(["1"] * size))
        A.append([complex(x.strip()) for x in row.split(",")])
    A = np.array(A, dtype=complex)

    # Input constants vector
    st.write("Enter the constants vector (b):")
    b_input = st.text_input("b (use format a+bj for complex numbers):", value=", ".join(["1"] * size))
    b = np.array([complex(x.strip()) for x in b_input.split(",")], dtype=complex)

    if st.button("Solve"):
        try:
            # Solve using Cramer's Rule
            result = cramers(A, b)
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

        except ValueError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")
