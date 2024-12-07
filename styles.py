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
    /* CSS Variables for Theme Configuration
    ---------------------------------------- */
    :root {
        /* Professional Blues */
        --blue-darker: #0a1525;
        --blue-dark: #152238;
        --blue-medium: #1e3253;
        --blue-light: #2c4c7c;
        
        /* Vivid Accents */
        --accent-green: #00ff7f;
        --accent-orange: #ff7f00;
        
        /* Base Colors */
        --bg-primary: var(--blue-darker);
        --bg-secondary: var(--blue-dark);
        --text-primary: #ffffff;
        --text-secondary: #b0c4de;
        --border-color: rgba(255, 255, 255, 0.1);
        
        /* Gradients */
        --gradient-blue: linear-gradient(135deg, var(--blue-dark), var(--blue-light));
        --gradient-accent: linear-gradient(90deg, var(--accent-green), var(--accent-orange));
        --gradient-hover: linear-gradient(90deg, var(--accent-orange), var(--accent-green));
        
        /* Shadows */
        --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
        --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
        
        /* Spacing */
        --spacing-xs: 0.5rem;
        --spacing-sm: 1rem;
        --spacing-md: 2rem;
        --spacing-lg: 3rem;
        --spacing-xl: 4rem;
        
        /* Border Radius */
        --radius-sm: 0.25rem;
        --radius-md: 0.5rem;
        --radius-lg: 1rem;
        
        /* Transitions */
        --transition-fast: 0.2s ease;
        --transition-normal: 0.3s ease;
    }

    /* Base Styles
    ---------------------------------------- */
    html {
        scroll-behavior: smooth;
        background: var(--bg-primary);
    }

    .main .block-container {
        padding-top: var(--spacing-xl) !important;
        max-width: 1200px;
        margin: 0 auto;
    }

    [id] {
        scroll-margin-top: var(--spacing-xl);
    }

    /* Hide Streamlit Default Elements
    ---------------------------------------- */
    .stDeployButton,
    header[data-testid="stHeader"],
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    /* Navigation
    ---------------------------------------- */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: var(--blue-darker);
        padding: var(--spacing-sm);
        z-index: 9999;
        border-bottom: 1px solid var(--border-color);
        box-shadow: var(--shadow-md);
    }

    .navigation {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: var(--spacing-sm);
        padding: var(--spacing-xs) var(--spacing-md);
        background: var(--blue-dark);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-sm);
        max-width: 1200px;
        margin: 0 auto;
    }

    .nav-link {
        color: var(--text-primary);
        text-decoration: none;
        padding: var(--spacing-xs) var(--spacing-sm);
        border-radius: var(--radius-md);
        transition: var(--transition-normal);
        font-size: 0.9rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        position: relative;
        overflow: hidden;
    }

    .nav-link::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: var(--gradient-accent);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform var(--transition-normal);
    }

    .nav-link:hover::before {
        transform: scaleX(1);
        transform-origin: left;
    }

    .nav-link:hover {
        color: var(--accent-green);
        background: rgba(255, 255, 255, 0.1);
    }

    /* Chat Section
    ---------------------------------------- */
    .chat-section {
        margin: var(--spacing-lg) 0;
        padding: var(--spacing-md);
        background: var(--blue-medium);
        border-radius: var(--radius-md);
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow-lg);
    }

    .chat-section h1 {
        background: var(--gradient-accent);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }

    /* Footer
    ---------------------------------------- */
    .footer {
        position: relative;
        bottom: 0;
        left: 0;
        right: 0;
        padding: var(--spacing-md);
        background: var(--blue-dark);
        border-top: 1px solid var(--border-color);
        text-align: center;
        color: var(--text-secondary);
        margin-top: var(--spacing-lg);
    }

    .footer a {
        color: var(--accent-green);
        text-decoration: none;
        margin: 0 var(--spacing-xs);
        transition: var(--transition-normal);
        font-weight: 500;
    }

    .footer a:hover {
        color: var(--accent-orange);
    }

    /* Typography
    ---------------------------------------- */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
        margin-bottom: var(--spacing-sm);
    }

    h1 {
        background: var(--gradient-accent);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        letter-spacing: -0.02em;
    }

    h2 {
        color: var(--blue-light);
        font-weight: bold;
    }

    p {
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: var(--spacing-sm);
    }

    /* Animations
    ---------------------------------------- */
    @keyframes glow {
        0% { box-shadow: var(--shadow-sm); }
        50% { box-shadow: var(--shadow-md); }
        100% { box-shadow: var(--shadow-sm); }
    }

    .nav-container {
        animation: glow 4s infinite;
    }

    /* Responsive Design
    ---------------------------------------- */
    @media (max-width: 768px) {
        .navigation {
            padding: var(--spacing-xs);
            gap: var(--spacing-xs);
            flex-wrap: wrap;
            justify-content: center;
        }

        .nav-link {
            font-size: 0.8rem;
            padding: var(--spacing-xs);
        }

        .nav-link::before {
            display: none;
        }

        .chat-section,
        .footer {
            padding: var(--spacing-sm);
            margin: var(--spacing-sm) 0;
        }
    }
</style>
"""