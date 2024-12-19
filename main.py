import streamlit as sl
sl.title("Hi! I am Streamlit");
sl.header("Header");
sl.subheader("Subheader");
sl.text("Text (Similar to paragraph in HTML)");
sl.markdown("--------");
sl.markdown("[google](https://www.google.com)");
sl.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}");
json={"a": 12, "b": 13, "c": 14}
sl.json(json);
code = """
print("hello there!");

a=3;
b=2;

def function():
    c=a+b;
    print(5);

function()
"""
sl.code(code);
sl.markdown("------");