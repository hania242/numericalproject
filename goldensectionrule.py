import streamlit as st
from sympy import symbols, sympify, lambdify
import pandas as pd

def golden_section_fixed_iterations(f, xl, xu, iterations, find_max=True):
    phi = 0.618  # Golden ratio constant
    table = []

    for i in range(iterations):
        d = phi * (xu - xl)
        x1 = xl + d
        x2 = xu - d

        # Ensure numerical evaluation
        fx1 = f(x1)
        fx2 = f(x2)

        # Store iteration details
        table.append({
            "Iteration": i + 1,
            "xl": xl,
            "f(xl)": f(xl),
            "x2": x2,
            "f(x2)": fx2,
            "x1": x1,
            "f(x1)": fx1,
            "xu": xu,
            "f(xu)": f(xu),
            "d": d
        })

        # Update bounds based on optimization goal
        if find_max:
            if fx1 > fx2:  # Compare numerical values
                x1 = x2
            else:
                xu = x1
        else:  # Minimization
            if fx1 < fx2:  # Compare numerical values
                xl = x2
            else:
                xu = x1

    # Determine optimal point
    x_opt = (xu + xl) / 2
    f_opt = f(x_opt)

    return {
        "iterations": table,
        "x_opt": x_opt,
        "f_opt": f_opt
    }

def golden_section_app():
    st.header("Golden Section Rule Solver")
    st.write("This app performs the Golden Section Rule to find the maximum or minimum of a function.")

    # Input for function
    equation = st.text_input(
        "Enter the function f(x):",
        value="e**-x * (x**2 - 3*x + 2)",
        help="Use 'x' for the variable and '**' for exponents. Example: e**-x * (x**2 - 3*x + 2)"
    )

    # Input for xl, xu, and number of iterations
    xl = st.number_input("Enter the lower bound (xl):", value=0.0)
    xu = st.number_input("Enter the upper bound (xu):", value=2.0)
    iterations = st.number_input("Enter the number of iterations:", value=10, step=1, min_value=1)
    find_max = st.selectbox("Optimization Goal:", ["Find Maximum", "Find Minimum"]) == "Find Maximum"

    if st.button("Solve with Golden Section Rule"):
        try:
            # Convert the function to a callable numerical function
            x = symbols('x')  # Symbol for x
            symbolic_f = sympify(equation)  # Parse the equation
            f = lambdify(x, symbolic_f, modules=["numpy"])  # Convert to numerical function

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
