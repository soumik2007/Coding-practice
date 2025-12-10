from datetime import date

today = date.today()
import streamlit as st 
st.title("Age Finder 🤔")
st.subheader("Write Your Date of Birth ✍🏻")
dob = st.date_input(
    "Your Date of Birth 🗓️",      
    min_value=date(1900, 1, 1),         
    max_value=date.today()            
)
today = date.today()

days_lived = (today - dob).days
age = days_lived//365
st.subheader(f"Your Age: {age}")

st.markdown(
    """
    <style>
    .blue-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: #000000;
        color: white;
        padding: 1rem 2rem;
        text-align: center;
        font-size: 14px;
        font-weight: 500;
        z-index: 1000;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        margin-bottom: 0;
    }
    .footer-heart {
        color: #ff6b6b;
        animation: heartbeat 1.5s ease-in-out infinite alternate;
    }
    @keyframes heartbeat {
        from { transform: scale(1); }
        to { transform: scale(1.1); }
    }
    </style>
    <div class="blue-footer">
        @ 2025 Age Finder made by Soumik De, made with <span class="footer-heart">❤️</span>
    </div>
    """,
    unsafe_allow_html=True
)