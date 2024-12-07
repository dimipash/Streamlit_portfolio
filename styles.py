"""
Module for managing custom CSS styles for the portfolio website.
This module provides functions to generate and manage CSS styles for the Streamlit portfolio application.
"""

def get_custom_css() -> str:
    """
    Generate custom CSS styles for the portfolio website.
    
    Returns:
        str: A string containing all custom CSS styles for the website.
    """
    return """
<style>
    /* CSS Variables for consistent theming */
    :root {
        --bg-primary: #0d1117;
        --bg-secondary: #161b22;
        --accent-primary: #00ff7f;  /* Vibrant green */
        --accent-secondary: #ffa500; /* Vibrant orange */
        --gradient-start: #00ff7f;
        --gradient-mid: #ffa500;
        --gradient-end: #00d4ff;
        --text-primary: #f9fafb;
        --text-secondary: #9ca3af;
        --border-color: #1f2937;
    }

    /* Base Styles */
    html {
        scroll-behavior: smooth;
    }

    .main .block-container {
        padding-top: 4rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    [id] {
        scroll-margin-top: 4rem;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }

    /* Navigation Styles */
    .stApp > header {
        background: linear-gradient(90deg, var(--bg-primary), var(--bg-secondary));
        border-bottom: 1px solid var(--border-color);
        padding: 0.5rem 1rem;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 100;
        height: 3rem;
    }

    .nav-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        padding: 0.5rem;
        background: rgba(31, 41, 55, 0.8);
        backdrop-filter: blur(8px);
        border-radius: 8px;
        margin: 0.5rem auto;
        max-width: fit-content;
        position: fixed;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1000;
    }

    .nav-link {
        color: var(--text-primary);
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        transition: all 0.2s ease;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        font-size: 1.1rem;
    }

    .nav-link svg {
        width: 1.5em;
        height: 1.5em;
    }

    .nav-link:hover {
        background: linear-gradient(90deg, rgba(var(--gradient-start), 0.1), rgba(var(--gradient-mid), 0.1));
        color: var(--gradient-start);
        transform: translateY(-1px);
    }

    .nav-link.active {
        background: linear-gradient(90deg, var(--gradient-start), var(--gradient-mid));
        color: white;
    }

    /* Typography */
    h1 {
        background: linear-gradient(90deg, var(--gradient-start), var(--gradient-mid), var(--gradient-end));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -0.025em;
        line-height: 1.2;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        background: linear-gradient(90deg, var(--gradient-start), var(--gradient-mid));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        letter-spacing: -0.025em;
        line-height: 1.3;
        margin-top: 2rem;
    }
    
    h3 {
        color: var(--text-primary);
        font-weight: 700;
        letter-spacing: -0.025em;
        line-height: 1.3;
        margin-top: 2rem;
    }

    /* Components */
    .stButton>button {
        background: linear-gradient(135deg, var(--gradient-start), var(--gradient-mid));
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem 1.5rem;
        font-size: 15px;
        font-weight: 600;
        letter-spacing: 0.025em;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, var(--gradient-mid), var(--gradient-start));
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--gradient-start), var(--gradient-mid));
        transition: width 0.3s ease-in-out;
    }
    
    .project-card {
        background: rgba(31, 41, 55, 0.4);
        backdrop-filter: blur(8px);
        color: var(--text-primary);
        border-radius: 12px;
        padding: 1.75rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        background: linear-gradient(145deg, 
            rgba(31, 41, 55, 0.4),
            rgba(var(--gradient-start), 0.1)
        );
        border-color: var(--gradient-start);
    }
    
    .streamlit-expanderHeader {
        background-color: rgba(31, 41, 55, 0.4);
        color: var(--text-primary);
        font-weight: 600;
        border-radius: 8px;
        padding: 1rem;
        transition: all 0.2s ease;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(145deg, 
            rgba(31, 41, 55, 0.6),
            rgba(var(--gradient-start), 0.1)
        );
        border-color: var(--gradient-start);
    }

    /* Refined scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(var(--gradient-start), var(--gradient-mid));
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(var(--gradient-mid), var(--gradient-start));
    }

    /* Refined inputs with gradient focus */
    .stTextInput>div>div>input {
        background-color: rgba(31, 41, 55, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: var(--text-primary);
        border-radius: 6px;
        padding: 0.75rem 1rem;
        transition: all 0.2s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: var(--gradient-start);
        box-shadow: 0 0 0 2px rgba(255, 87, 51, 0.2);
    }

    /* Refined text area */
    .stTextArea>div>div>textarea {
        background-color: rgba(31, 41, 55, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: var(--text-primary);
        border-radius: 6px;
        padding: 0.75rem 1rem;
        transition: all 0.2s ease;
    }
    
    .stTextArea>div>div>textarea:focus {
        border-color: var(--gradient-start);
        box-shadow: 0 0 0 2px rgba(255, 87, 51, 0.2);
    }

    /* Enhanced links */
    a {
        color: var(--accent-primary);
        text-decoration: none;
        transition: all 0.2s ease;
    }
    
    a:hover {
        color: var(--accent-secondary);
    }

    /* Refined sidebar navigation */
    .css-1d391kg .streamlit-button {
        width: 100%;
        text-align: left;
        padding: 0.5rem 1rem;
        margin: 0.25rem 0;
        background: transparent;
        border: none;
        color: var(--text-primary);
        transition: all 0.2s ease;
    }
    
    .css-1d391kg .streamlit-button:hover {
        background: linear-gradient(90deg, 
            rgba(var(--gradient-start), 0.1),
            transparent
        );
        color: var(--gradient-start);
    }

    /* Chat Interface Styles */
    .chat-container {
        padding: 1rem;
        max-height: 500px;
        overflow-y: auto;
    }
    
    .chat-container .stRadio {
        background: #f0f2f6;
        padding: 0.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    .chat-container .stChatMessage {
        margin: 0.5rem 0;
    }
    
    .chat-container .stChatInputContainer {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 0.5rem;
        border-top: 1px solid #e0e0e0;
    }
    
    .chat-message {
        margin: 0.5rem 0;
        padding: 0.5rem;
        border-radius: 8px;
    }

    .chat-message.user {
        background: rgba(0, 255, 127, 0.1);
        margin-left: 1rem;
    }

    .chat-message.assistant {
        background: rgba(255, 165, 0, 0.1);
        margin-right: 1rem;
    }

    .chat-input {
        background: rgba(31, 41, 55, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 6px;
        padding: 0.5rem;
        margin-top: 1rem;
    }

    .chat-button {
        background: linear-gradient(135deg, var(--gradient-start), var(--gradient-mid));
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        margin-top: 0.5rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .chat-button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* Hide the default Streamlit menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""