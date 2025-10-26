import streamlit as st
import streamlit as st
from main import finalText

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #AEC6CF, #FFB347);
}

.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    margin-top: 20px;
}

h2 {
    color: #333333;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}
    
h1 {
    color: #333333;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;      
}

.stButton>button {
    background-color: #6AA84F;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
}
            
.stButton>button:hover {
    background-color: #38761D;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("FinScout AI")
st.markdown("""<h2>What is FinScout?</h2>
            <b>FinScout is your personal financial assistant. FinScout uses the power of Ai to determine ways you can save money
             based on your spending history. FinScout shows you where you spend your money and provides 
            3 ways to optimize your spending.</b>
            <b></b>""", unsafe_allow_html=True)

st.write(finalText)
 
