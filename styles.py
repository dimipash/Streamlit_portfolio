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
    :root {
        --accent-green: #00ff7f;
        --accent-orange: #ff7f00;
        --accent-blue: #00bfff;
        --accent-purple: #8a2be2;

        --bg-primary: #000000;
        --bg-secondary: #111111;
        --bg-tertiary: #1a1a1a;
        --text-primary: #ffffff;
        --text-secondary: #b0c4de;
        --border-color: rgba(0, 255, 127, 0.2);

        --gradient-primary: linear-gradient(135deg, var(--accent-green), var(--accent-blue));

        --spacing-xs: 0.25rem;
        --spacing-sm: 0.5rem;
        --spacing-md: 1rem;
        --spacing-lg: 2rem;
        --spacing-xl: 4rem;
    }

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

    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: rgba(0, 0, 0, 0.9);
        backdrop-filter: blur(10px);
        padding: 0.25rem;
        border-bottom: 1px solid var(--border-color);
        height: 50px;
    }

    .navigation {
        display: flex;
        justify-content: center;
        gap: 1rem;
        max-width: 1400px;
        margin: 0 auto;
        height: 100%;
        align-items: center;
    }

    .nav-link {
        color: var(--text-secondary);
        text-decoration: none;
        padding: 0.25rem 0.75rem;
        margin: 0;
        border-radius: 4px;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        border-bottom: 2px solid transparent;
    }

    .nav-link:hover {
        color: var(--accent-green) !important;
        border-bottom-color: var(--accent-green);
        transform: translateY(-2px);
    }

    .navigation {
        gap: 2rem;
        padding: 1rem 0;
    }

    .main-content {
        margin-top: 80px;
        padding: 20px;
    }

    @media (max-width: 768px) {
        .nav-container {
            padding: 0.5rem;
        }
    }

    .profile-container {
        display: flex;
        align-items: center;
        gap: 2rem;
        padding: 2rem;
    }

    .profile-photo {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        border: 3px solid var(--accent-green);
        object-fit: cover;
    }

    .profile-info {
        max-width: 600px;
    }

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
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .home-section:hover,
    .skills-section:hover,
    .projects-section:hover,
    .experience-section:hover,
    .education-section:hover,
    .github-section:hover,
    .courses-section:hover,
    .contact-section:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 255, 127, 0.1);
    }

    .nav-link:focus,
    a:focus,
    button:focus {
        outline: 2px solid var(--accent-blue);
        outline-offset: 2px;
    }

    .sr-only {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
    }

    .theme-toggle {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        z-index: 1000;
    }

    .theme-toggle:hover {
        background: var(--bg-tertiary);
        transform: scale(1.1);
    }

    @media (max-width: 768px) {
        .profile-container {
            flex-direction: column;
            text-align: center;
            gap: 1.5rem;
        }

        .profile-photo {
            width: 150px;
            height: 150px;
        }
    }

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

    a {
        color: var(--accent-green) !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
    }

    a:hover {
        color: var(--accent-orange) !important;
    }

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

    .stTable {
        background: var(--bg-secondary) !important;
        border-radius: 8px !important;
        overflow: hidden !important;
    }

    .stTable th {
        background: var(--bg-tertiary) !important;
        color: var(--accent-green) !important;
    }

    .stCodeBlock {
        background: var(--bg-tertiary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
    }

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

    .footer {
        text-align: center;
        padding: var(--spacing-lg);
        margin-top: var(--spacing-xl);
        border-top: 1px solid var(--border-color);
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes loading {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .block-container > div {
        animation: fadeIn 0.5s ease forwards;
    }

    .loading-spinner {
        display: inline-block;
        width: 40px;
        height: 40px;
        border: 4px solid var(--accent-green);
        border-top-color: transparent;
        border-radius: 50%;
        animation: loading 1s linear infinite;
    }

    html {
        scroll-behavior: smooth;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--accent-green);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-blue);
    }

    .user-message {
        color: white;
    }

    .bot-message {
        color: #00ff7f;
    }
</style>
"""
