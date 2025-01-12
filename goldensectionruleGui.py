import streamlit as st
from sympy import sympify, lambdify
import pandas as pd
from goldensectionrule import golden_section_fixed_iterations

def golden_section_app():
    st.header("Golden Section Rule Solver")
    st.write("This app performs the Golden Section Rule to find the maximum or minimum of a function.")

    # Input for function
    equation = st.text_input(
        "Enter the function f(x):",
        value="x**2 - 4*x + 4",
        help="Use 'x' for the variable and '**' for exponents. Example: x**2 - 4*x + 4"
    )

    # Input for xl, xu, number of iterations, and optimization type
    xl = st.number_input("Enter the lower bound (xl):", value=0.0)
    xu = st.number_input("Enter the upper bound (xu):", value=2.0)
    iterations = st.number_input("Enter the number of iterations:", value=10, step=1, min_value=1)
    find_max = st.selectbox("Optimization Goal:", ["Find Maximum", "Find Minimum"]) == "Find Maximum"

    if st.button("Solve with Golden Section Rule"):
        try:
            # Convert the function to a callable form
            f = lambdify("x", sympify(equation))

            # Perform the Golden Section Rule
            result = golden_section_fixed_iterations(f, xl, xu, iterations, find_max)

            # Extract results
            iteration_table = result["iterations"]
            x_opt = result["x_opt"]
            f_opt = result["f_opt"]

            # Display results
            st.success("Golden Section Rule Completed!")
            st.write(f"Optimal x: {x_opt}")
            st.write(f"Optimal f(x): {f_opt}")

            # Display iteration table
            st.write("### Iteration Details:")
            df = pd.DataFrame(iteration_table)
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    golden_section_app()
