import streamlit as st
def display_help():
    st.write("### How to Write Mathematical Equations")
    st.markdown(
        """
        This app uses **Python syntax** for mathematical functions. Below are examples to help you input your equation correctly:

        #### Supported Operations:
        - **Addition:** Use `+`.  
          Example: `x + 3`
        - **Subtraction:** Use `-`.  
          Example: `x - 2`
        - **Multiplication:** Use `*`.  
          Example: `2 * x`
        - **Division:** Use `/`.  
          Example: `x / 4`
        - **Powers:** Use `**`.  
          Example: `x**2` for \(x^2\)

        #### Supported Functions:
        - **Square Root:** Use `sqrt(x)` for \( \\sqrt{x} \).  
          Example: `sqrt(x**2 + 1)` for \( \\sqrt{x^2 + 1} \).
        - **Sine:** Use `sin(x)` for \( \\sin(x) \).  
        - **Cosine:** Use `cos(x)` for \( \\cos(x) \).  
        - **Tangent:** Use `tan(x)` for \( \\tan(x) \).  
        - **Exponential:** Use `exp(x)` for \( e^x \).  
        - **Logarithm:** Use `log(x)` for natural log (\( \\ln(x) \)).

        #### Angle Inputs:
        - Angles are in **radians** by default.  
          To use degrees, convert to radians using \( \\text{radians} = \\text{degrees} \\cdot \\frac{\\pi}{180} \):  
          Example: `sin(x * pi / 180)`.

        #### Example Equations:
        - \( f(x) = x^2 - 4x + 4 \):  
          Input: `x**2 - 4*x + 4`
        - \( f(x) = \\sin(x) + \\cos(x) \):  
          Input: `sin(x) + cos(x)`
        - \( f(x) = \\sqrt{x^2 + 1} \):  
          Input: `sqrt(x**2 + 1)`
        - \( f(x) = \\log(x) + e^x \):  
          Input: `log(x) + exp(x)`
        """
    )


