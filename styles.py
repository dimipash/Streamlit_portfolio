def get_custom_css():
    return """
<style>
    /* Main page */
    .main {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #4CAF50;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #252525;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    
    /* Progress bars */
    .stProgress .st-bo {
        background-color: #2196F3;
    }
    
    /* Cards */
    .project-card {
        background-color: #2C2C2C;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        border-left: 5px solid #4CAF50;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #2C2C2C;
        color: #E0E0E0;
    }
    .streamlit-expanderContent {
        background-color: #252525;
        color: #E0E0E0;
    }
    
    /* Links */
    a {
        color: #2196F3;
    }
    a:hover {
        color: #64B5F6;
    }
    
    /* Form inputs */
    .stTextInput>div>div>input {
        background-color: #2C2C2C;
        color: #E0E0E0;
    }
    .stTextArea>div>div>textarea {
        background-color: #2C2C2C;
        color: #E0E0E0;
    }
</style>
"""