import streamlit as st
from sympy import sympify, lambdify
from quadraticinterpolation import quadratic_interpolation

def quadratic_interpolation_app():
    st.header("Quadratic Interpolation Solver")
    st.write("This app performs quadratic interpolation using the specified formula to estimate \( x_3 \).")

    # Input for function
    equation = st.text_input(
        "Enter the function f(x):",
        value="x**3 - 6*x + 8",
        help="Use 'x' for the variable and '**' for exponents. Example: x**3 - 6*x + 8"
    )
    
    # Input for x0, x1, x2
    x0 = st.number_input("Enter x0:", value=0.0)
    x1 = st.number_input("Enter x1:", value=1.0)
    x2 = st.number_input("Enter x2:", value=2.0)

    if st.button("Solve Quadratic Interpolation"):
        try:
            # Convert the function to a callable form
            f = lambdify("x", sympify(equation))
            
            # Perform quadratic interpolation
            result = quadratic_interpolation(f, x0, x1, x2)
            
            # Display results
            st.success("Quadratic Interpolation Results:")
            st.write(f"f(x0) = {result['f(x0)']}")
            st.write(f"f(x1) = {result['f(x1)']}")
            st.write(f"f(x2) = {result['f(x2)']}")
            st.write(f"Estimated x3 = {result['x3']}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    quadratic_interpolation_app()
