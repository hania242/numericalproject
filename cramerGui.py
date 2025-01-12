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
        row = st.text_input(f"Row {i+1} (use format a+bI for complex numbers):")
        if row.strip():  # Ensure the row isn't empty before parsing
            A.append([complex(x.strip().replace("I", "j")) for x in row.split(",")])
        else:
            st.error(f"Row {i+1} cannot be empty.")
            return
    A = np.array(A, dtype=complex)

    # Input constants vector
    st.write("Enter the constants vector (b):")
    b_input = st.text_input("b (use format a+bI for complex numbers):")
    if b_input.strip():  # Ensure the input isn't empty before parsing
        b = np.array([complex(x.strip().replace("i", "j")) for x in b_input.split(",")], dtype=complex)
    else:
        st.error("Constants vector (b) cannot be empty.")
        return

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
            st.error("An unexpected error occurred. Please check your inputs.")

if __name__ == "__main__":
    cramers_app()
