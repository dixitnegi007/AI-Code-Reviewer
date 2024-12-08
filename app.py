import streamlit as st
import google.generativeai as genai

# Directly configure your API key (for testing purposes, though it's not recommended to expose it in production)
api_key = "Your Api Key"

# Configure your API key
genai.configure(api_key=api_key)

# Set Streamlit page configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for lighter background and black text
st.markdown(
    """
    <style>
        /* Background styling with a softer, lighter gradient */
        .stApp {
            background: linear-gradient(to right, #f0f8ff, #e6f7ff, #d9f2ff, #cce6ff) !important;
            color: #000 !important;  /* Ensure text is black */
        }

        /* Title styling */
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #000000;
            text-shadow: 2px 2px 5px #000;
            margin-bottom: 10px;
        }

        /* Text area styling */
        textarea {
            background: rgba(255, 255, 255, 0.8) !important;
            border: 1px solid #ddd !important;
            color: #000 !important;
            border-radius: 5px !important;
            font-size: 16px !important;
        }

        /* Button styling */
        button[kind="primary"] {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 18px !important;
            padding: 10px 20px !important;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }

        /* Sidebar styling */
        .css-1d391kg {
            background: linear-gradient(to bottom, #e0ffff, #d6f7ff, #bce7ff) !important;
            color: black !important;
        }

        /* Subheader styling */
        .stMarkdown h2 {
            color: #000000;
            text-shadow: 1px 1px 2px #000;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("AI Code Reviewer Features")
st.sidebar.subheader("How to use?")
st.sidebar.write(" Enter Python code for review.")
st.sidebar.write(" Get a bug report and feedback.")

st.sidebar.markdown("---")
st.sidebar.write("📌 **Take the time to review your code for improvements**.")

# Title
st.markdown('<div class="title">AI Code Reviewer 🤖</div>', unsafe_allow_html=True)

# Description
st.write("Welcome to the **AI Code Reviewer**! Paste your Python code below, and let the AI help you identify bugs and provide useful feedback.")

# Input for the human prompt
human_code = st.text_area("📝 Enter your code here for review:")

# Button to trigger code review
if st.button("✨ Generate"):
    if human_code:
        # Initialize the generative model
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        
        # Send the user code for review
        chatbot = model.start_chat(history=[])
        response = chatbot.send_message(f"Review the following Python code and identify any bugs:\n{human_code}")
        
        # Display the AI-generated response
        st.subheader("🧐 Code Review")
        st.markdown("**Bug Report:**")
        st.write(response.text)  # Display AI response
    else:
        st.error("❌ Please enter some code before generating the review!")

# Footer
st.markdown("---")
