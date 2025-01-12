import streamlit as st
from GUI import muller_app
from cramerGui import cramers_app
from LUdecompositionGui import lu_app  # Import the LU Decomposition app
from quadraticinterpolationGui import quadratic_interpolation_app  # Import the Quadratic Interpolation app
from goldensectionruleGui import golden_section_app  # Import the Golden Section Rule app
from gaussseidelGui import gauss_seidel_app  # Import the Gauss-Seidel Method app
from secantGui import secant_method_app  # Import the Secant Method app
from help import display_help  # Import the Help app

def main():
    st.title("Numerical Methods Solver")
    st.write("Choose a method to solve numerical problems:")

    if "show_help" not in st.session_state:
        st.session_state.show_help = False

    # Help Toggle Button
    if st.button("Toggle Help: How to Write Mathematical Equations"):
        st.session_state.show_help = not st.session_state.show_help  # Toggle state

    # Show or hide the help section
    if st.session_state.show_help:
        display_help()

    # Sidebar menu
    menu = st.selectbox(
        "Select a method:",
        [
            "Muller's Method",
            "Cramer's Rule",
            "LU Decomposition",
            #"Quadratic Interpolation",
            #"Golden Section Rule",
            #"Gauss-Seidel Method",
            #"Secant Method",
        ]
    )

    # Call the appropriate app based on selection
    if menu == "Muller's Method":
        muller_app()  # Call the muller_app function
    elif menu == "Cramer's Rule":
        cramers_app()  # Call the cramers_app function
    elif menu == "LU Decomposition":
        lu_app()  # Call the lu_app function
   # elif menu == "Quadratic Interpolation":
        #quadratic_interpolation_app()  # Call the quadratic_interpolation_app function
    #elif menu == "Golden Section Rule":
        #golden_section_app()  # Call the golden_section_app function
    #elif menu == "Gauss-Seidel Method":
        #gauss_seidel_app()  # Call the gauss_seidel_app function
    #elif menu == "Secant Method":
        #secant_method_app()  # Call the secant_method_app function

if __name__ == "__main__":
    main()
