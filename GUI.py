import streamlit as st
from muller import muller
def inject_custom_css():
    st.markdown(
        """
        <style>
        /* Style headers within markdown */
        .stMarkdown h1, .stMarkdown h2 {
            color: #00A1FF !important; /* Primary blue for headers in markdown */
        }

        /* Style buttons */
        div.stButton > button {
            background-color: #00A1FF !important;  /* Primary blue */
            color: white !important;
            border-radius: 8px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            border: none !important;
            transition: 0.3s !important;
        }
        div.stButton > button:hover {
            background-color: #007ACC !important; /* Darker blue on hover */
        }

        /* Style input fields */
        input[type="text"], input[type="number"], textarea {
            border: 2px solid #00A1FF !important;
            border-radius: 5px !important;
            padding: 8px !important;
            font-size: 14px !important;
        }
        input[type="text"]:focus, input[type="number"]:focus, textarea:focus {
            outline: none !important;
            border: 2px solid #007ACC !important; /* Darker blue on focus */
        }

        /* Adjust block container for visual improvement */
        .block-container {
            background-color: #F5F5F5 !important;
            padding: 20px !important;
            border-radius: 10px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Inject the CSS at the start of the app
inject_custom_css()

# Streamlit App
def muller_app():
    st.title("Numerical Methods Solver: Muller Method (Step-by-Step)")
    st.write("This app calculates the intermediate values for each iteration using the Muller method.")

    # User inputs
    equation = st.text_input(
        "Enter the function f(x):",
        value="x**3 - 6*x + 8",
        help="Use 'x' for the variable and '**' for exponents. Example: x**3 - 6*x + 8",
    )
    x0 = st.number_input("Enter the first initial guess (x0):", value=0.0)
    x1 = st.number_input("Enter the second initial guess (x1):", value=1.0)
    x2 = st.number_input("Enter the third initial guess (x2):", value=2.0)
    max_iter = st.number_input("Maximum Iterations:", value=10, step=1)
    true_root = st.text_input(
        "Enter the true root (optional):",
        value="",
        help="If known, enter the true root to calculate Et (%) for each iteration.",
    )

    if st.button("Solve Step-by-Step"):
        try:
            # Clean and validate the equation
            equation = equation.strip()  # Remove extra spaces
            f = lambda x: eval(equation.replace("^", "**"))  # Replace ^ with ** for exponentiation
            f(1)  # Test the equation with a sample value to validate correctness

            # Parse true root if provided
            true_root = complex(true_root) if true_root else None

            # Solve using the Muller method
            steps = muller(f, complex(x0), complex(x1), complex(x2), max_iter=max_iter, true_root=true_root)

            st.success("Calculation complete. See step-by-step results below.")
            st.write("### Step-by-Step Results:")
            for step in steps:
                st.write(f"**Iteration {step['iteration']}:**")
                st.json(step)

        except SyntaxError:
            st.error("The equation syntax is incorrect. Please check your input.")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    muller_app()
