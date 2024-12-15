"""
Module for managing custom CSS styles for the portfolio website.
This module provides functions to generate and manage CSS styles for the Streamlit application.
"""

def get_custom_css() -> str:
    """
    Generate custom CSS styles for the portfolio website.
    
    Returns:
        str: A string containing all custom CSS styles for the website.
    """
    return """
<style>
    /* Modern Theme Configuration */
    :root {
        /* Vivid Accents */
        --accent-green: #00ff7f;
        --accent-orange: #ff7f00;
        
        /* Professional Colors */
        --bg-primary: #000000;
        --bg-secondary: #111111;
        --bg-tertiary: #1a1a1a;
        --text-primary: #ffffff;
        --text-secondary: #b0c4de;
        --border-color: rgba(0, 255, 127, 0.2);
        
        /* Spacing */
        --spacing-xs: 0.25rem;
        --spacing-sm: 0.5rem;
        --spacing-md: 1rem;
        --spacing-lg: 2rem;
        --spacing-xl: 4rem;
    }

    /* Global Styles */
    .stApp {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
        margin-top: 0;
        padding-top: 0;
    }

    .main .block-container {
        padding-top: 4rem !important;
        margin-top: 0;
    }

    /* Navigation */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(0, 0, 0, 0.9);
        backdrop-filter: blur(10px);
        padding: 0.5rem;
        border-bottom: 1px solid var(--border-color);
    }

    .navigation {
        display: flex;
        justify-content: center;
        gap: 1rem;
        max-width: 1400px;
        margin: 0 auto;
    }

    .nav-link {
        color: var(--text-secondary);
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        transition: background-color 0.3s;
    }

    .nav-link:hover {
        background-color: #f0f0f0;
    }

    /* Main Content Spacing */
    .main-content {
        margin-top: 80px;  /* Space for fixed navbar */
        padding: 20px;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .nav-container {
            padding: 0.5rem;
        }
    }

    /* Section Containers */
    .home-section,
    .skills-section,
    .projects-section,
    .experience-section,
    .education-section,
    .github-section,
    .courses-section,
    .contact-section {
        max-width: 1400px;
        margin: var(--spacing-xl) auto;
        padding: var(--spacing-lg);
        background: var(--bg-secondary);
        border-radius: 12px;
        border: 1px solid var(--border-color);
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
        margin-bottom: var(--spacing-md);
        background: linear-gradient(45deg, var(--accent-green), var(--accent-orange));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    h1 {
        font-size: 2.5rem;
        font-weight: 700;
    }

    h2 {
        font-size: 2rem;
        font-weight: 600;
    }

    h3 {
        font-size: 1.5rem;
        font-weight: 600;
    }

    p {
        font-size: 1.1rem;
        line-height: 1.6;
        color: var(--text-secondary);
        margin-bottom: var(--spacing-md);
    }

    /* Links */
    a {
        color: var(--accent-green) !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
    }

    a:hover {
        color: var(--accent-orange) !important;
    }

    /* Input Fields */
    .stTextInput > div > div > input {
        background: var(--bg-tertiary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 4px !important;
        color: var(--text-primary) !important;
        transition: all 0.2s ease !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--accent-green) !important;
        box-shadow: 0 0 0 1px var(--accent-green) !important;
    }

    /* Tables */
    .stTable {
        background: var(--bg-secondary) !important;
        border-radius: 8px !important;
        overflow: hidden !important;
    }

    .stTable th {
        background: var(--bg-tertiary) !important;
        color: var(--accent-green) !important;
    }

    /* Code Blocks */
    .stCodeBlock {
        background: var(--bg-tertiary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
    }

    /* Metrics and KPIs */
    .metric-container {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 600;
        color: var(--accent-green);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: var(--spacing-lg);
        margin-top: var(--spacing-xl);
        border-top: 1px solid var(--border-color);
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .block-container > div {
        animation: fadeIn 0.5s ease forwards;
    }
</style>
"""
