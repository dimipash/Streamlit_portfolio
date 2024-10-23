def get_custom_css():
    return """
<style>
    /* Main page */
    .main {
        background-color: #0d1117; /* Dark background for the whole page */
        color: #c9d1d9; /* Light text color */
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #58a6ff; /* Light blue for headings */
        font-weight: 600;
    }
    
    /* Responsive adjustments */
    @media (max-width: 1024px) {
        .stApp .stColumn {
            flex-direction: column;
        }
    }
    
    /* Sidebar */
    
    
    /* Buttons */
    .stButton>button {
        background-color: #238636; /* Green button color */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2ea043; /* Darker green on hover */
    }
    
    /* Progress bars */
    .stProgress .st-bo {
        background-color: #58a6ff; /* Light blue for progress bars */
    }
    
    /* Cards */
    .project-card {
        background-color: #161b22; /* Dark background for cards */
        color: #c9d1d9; /* Light text color */
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid #30363d; /* Dark border */
        box-shadow: 0 1px 3px rgba(27,31,35,0.12), 0 1px 2px rgba(27,31,35,0.24);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #0d1117;
        color: #c9d1d9;
        font-weight: 600;
    }
    .streamlit-expanderContent {
        background-color: #161b22;
        color: #c9d1d9;
    }
    
    /* Links */
    a {
        font-size: 20px;
        font-weight: bold;
        color: #58a6ff;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    a:hover {
        color: #0ADD08; /* Lighter blue on hover */
    }
    
    /* Form inputs */
    .stTextInput>div>div>input {
        background-color: #0d1117;
        color: #c9d1d9;
        border: 1px solid #30363d;
        border-radius: 5px;
        padding: 0.5rem;
    }
    .stTextArea>div>div>textarea {
        background-color: #0d1117;
        color: #c9d1d9;
        border: 1px solid #30363d;
        border-radius: 5px;
        padding: 0.5rem;
    }
</style>
"""