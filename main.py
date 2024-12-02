"""
Portfolio Website built with Streamlit.
Author: Dimitar Pashev
"""

import os
from dataclasses import dataclass
from typing import List, Dict, Union
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
import plotly.express as px
from PIL import Image
import requests
import json
from styles import get_custom_css
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Type definitions
SkillsDict = Dict[str, int]
ProjectDict = Dict[str, str]
JobDict = Dict[str, Union[str, List[str]]]

@dataclass
class Config:
    """Configuration settings for the portfolio website."""
    PROFILE_IMAGE: str = "photo.jpeg"
    RESUME_PATH: str = "resume.pdf"
    PAGE_TITLE: str = "Dimitar Pashev - Portfolio"
    GITHUB_USERNAME: str = "dimipash"
    CONTACT_EMAIL: str = "dim.pashev@gmail.com"

    @staticmethod
    def load_email_config():
        """Load email configuration from environment variables."""
        load_dotenv()
        return {
            'host': os.getenv('EMAIL_HOST', 'smtp.gmail.com'),
            'port': int(os.getenv('EMAIL_PORT', '587')),
            'username': os.getenv('EMAIL_USERNAME'),
            'password': os.getenv('EMAIL_PASSWORD')
        }

    @staticmethod
    def send_email(subject: str, body: str, from_email: str) -> bool:
        """Send email using SMTP configuration."""
        try:
            email_config = Config.load_email_config()
            
            if not all([email_config['username'], email_config['password']]):
                st.error("Email configuration is incomplete. Please check .env file.")
                return False

            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = Config.CONTACT_EMAIL
            msg['Subject'] = f"Portfolio Contact: {subject}"

            # Add sender's email to the body
            full_body = f"From: {from_email}\n\n{body}"
            msg.attach(MIMEText(full_body, 'plain'))

            # Create SMTP session
            with smtplib.SMTP(email_config['host'], email_config['port']) as server:
                server.starttls()
                server.login(email_config['username'], email_config['password'])
                server.send_message(msg)
            
            return True
        except Exception as e:
            st.error(f"Failed to send email: {str(e)}")
            return False

# Initialize configuration
config = Config()

class Analytics:
    """Analytics tracking for portfolio interactions."""
    
    @staticmethod
    def track_project_view(project_name: str) -> None:
        """Track when a project is viewed."""
        if 'project_views' not in st.session_state:
            st.session_state.project_views = {}
        
        if project_name not in st.session_state.project_views:
            st.session_state.project_views[project_name] = 0
        st.session_state.project_views[project_name] += 1

    @staticmethod
    def track_contact_submission() -> None:
        """Track when contact form is submitted."""
        if 'contact_submissions' not in st.session_state:
            st.session_state.contact_submissions = 0
        st.session_state.contact_submissions += 1

class PortfolioData:
    """Data container for portfolio content."""
    
    @staticmethod
    def get_skills_data() -> Dict[str, Dict[str, Union[int, str]]]:
        """Returns technical skills with proficiency levels and categories."""
        return {
            "Python": {"proficiency": 90, "category": "Languages", "experience_years": 2},
            "Django": {"proficiency": 85, "category": "Frameworks", "experience_years": 1.5},
            "ReactJS": {"proficiency": 75, "category": "Frontend", "experience_years": 1},
            "JavaScript": {"proficiency": 70, "category": "Languages", "experience_years": 1},
            "CSS": {"proficiency": 75, "category": "Frontend", "experience_years": 1.5},
            "HTML": {"proficiency": 80, "category": "Frontend", "experience_years": 1.5},
            "Linux": {"proficiency": 70, "category": "Tools", "experience_years": 2},
            "API Development": {"proficiency": 80, "category": "Backend", "experience_years": 1.5},
            "PostgreSQL": {"proficiency": 75, "category": "Databases", "experience_years": 1},
            "Version Control": {"proficiency": 85, "category": "Tools", "experience_years": 2},
            "Bash": {"proficiency": 70, "category": "Tools", "experience_years": 1},
            "Database Management": {"proficiency": 80, "category": "Databases", "experience_years": 1.5},
        }
    
    @staticmethod
    def get_project_metrics() -> Dict[str, Dict[str, Union[int, float, str]]]:
        """Returns project metrics and statistics."""
        return {
            "Online Shop": {
                "code_coverage": 85,
                "commits": 120,
                "stars": 15,
                "complexity": "Medium",
                "status": "Active"
            },
            "SaaS Platform": {
                "code_coverage": 90,
                "commits": 200,
                "stars": 25,
                "complexity": "High",
                "status": "Active"
            },
            "Notes App": {
                "code_coverage": 75,
                "commits": 50,
                "stars": 8,
                "complexity": "Low",
                "status": "Completed"
            }
        }
    
    @staticmethod
    def get_soft_skills() -> List[str]:
        """Returns list of soft skills."""
        return [
            "Communication",
            "Team Player",
            "Problem-Solving",
            "Adaptability",
            "Attention To Detail",
        ]
    
    @staticmethod
    def get_projects_data() -> List[ProjectDict]:
        """Returns list of project information."""
        return [
            {
                "name": "Online Shop Django Project",
                "date": "03/2024 - 04/2024",
                "description": "[Online Shop](https://dimipi.pythonanywhere.com/) - a comprehensive set of features for managing an online shopping platform. Custom user model, categories and products, shopping cart, orders, inventory, user account management, PayPal payments.",
                "tech_stack": ["Python", "Django", "PostgreSQL", "JavaScript", "Bootstrap"],
                "live_demo": "https://dimipi.pythonanywhere.com/",
                "github_link": "https://github.com/dimipash/OnlineShop",
            },
            {
                "name": "SaaS Django Project",
                "date": "08/2024 - 10/2024",
                "description": "[SaaS](https://saas-dlp.up.railway.app/) - a foundational Software as a Service (SaaS) solution built with Django, featuring user authentication, subscription management, and custom commands.",
                "tech_stack": ["Python", "Django", "PostgreSQL", "Stripe API"],
                "live_demo": "https://saas-dlp.up.railway.app/",
                "github_link": "https://github.com/dimipash/SaaS",
            },
            {
                "name": "Django Projects",
                "date": "09/2023 - 03/2024",
                "description": "Various Django projects, including e-commerce site, web-based CV generator, link scraper, social media app, advanced expense tracker, calorie tracker, movie list, food app",
            },
            {
                "name": "Python Projects",
                "date": "01/2024 - ongoing",
                "description": "This repository contains various Python projects, each in its own directory.",
            },
            {
                "name": "Django & React Notes App",
                "date": "02/2024 - 03/2024",
                "description": "Full-stack application built with Django and React, allowing users to create, read, and delete notes. Follows a RESTful API architecture and utilizes JSON Web Tokens (JWT) for authentication.",
            },
            {
                "name": "Books React E-commerce App",
                "date": "11/2023 - 12/2023",
                "description": "E-commerce web app with React utilizing Vite, JSX, Tailwind CSS. Created reusable component logic with custom hooks, managed state with context API, implemented cart functionality.",
            },
        ]

class PortfolioUI:
    """UI components and layout for the portfolio website."""
    
    @staticmethod
    def render_skills_section(skills_data: Dict[str, Dict[str, Union[int, str]]]) -> None:
        """Render skills in a clean, organized format."""
        # Group skills by category
        skills_by_category = {}
        for skill, data in skills_data.items():
            category = data["category"]
            if category not in skills_by_category:
                skills_by_category[category] = []
            skills_by_category[category].append((skill, data["proficiency"]))

        # Display skills by category
        for category, skills in skills_by_category.items():
            st.subheader(f"🔹 {category}")
            for skill, proficiency in sorted(skills, key=lambda x: x[1], reverse=True):
                col1, col2 = st.columns([3, 7])
                with col1:
                    st.write(f"**{skill}**")
                with col2:
                    st.progress(proficiency / 100)

    @staticmethod
    def skills() -> None:
        """Render skills section."""
        st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
        st.title("Skills 🛠️")
        
        # Get skills data
        skills_data = PortfolioData.get_skills_data()
        
        # Render technical skills
        st.header("Technical Skills")
        PortfolioUI.render_skills_section(skills_data)
        
        # Render soft skills
        st.header("Soft Skills")
        soft_skills = PortfolioData.get_soft_skills()
        cols = st.columns(3)
        for i, skill in enumerate(soft_skills):
            with cols[i % 3]:
                st.markdown(f"✨ {skill}")

    @staticmethod
    def render_contact_form() -> None:
        """Render an interactive contact form."""
        st.header("📫 Contact Me")
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message")
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if not all([name, email, subject, message]):
                    st.error("Please fill in all fields")
                    return
                
                if not '@' in email:
                    st.error("Please enter a valid email address")
                    return
                
                formatted_message = f"""
                Name: {name}
                Message:
                {message}
                """
                
                if config.send_email(subject, formatted_message, email):
                    st.success("Thank you for your message! I'll get back to you soon.")
                    Analytics.track_contact_submission()

    @staticmethod
    def render_project_metrics(project_name: str, metrics: Dict[str, Union[int, float, str]]) -> None:
        """Render metrics for a project."""
        cols = st.columns(4)
        with cols[0]:
            st.metric("Code Coverage", f"{metrics['code_coverage']}%")
        with cols[1]:
            st.metric("Commits", metrics['commits'])
        with cols[2]:
            st.metric("GitHub Stars", metrics['stars'])
        with cols[3]:
            st.metric("Status", metrics['status'])

    @staticmethod
    def projects() -> None:
        """Render projects section with enhanced interactivity."""
        st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
        st.title("Personal Projects")
        
        # Filter projects
        tech_filter = st.multiselect(
            "Filter by Technology",
            ["Python", "Django", "React", "JavaScript", "PostgreSQL"]
        )
        
        for project in PortfolioData.get_projects_data():
            if not tech_filter or any(tech in project.get('tech_stack', []) for tech in tech_filter):
                with st.expander(f"{project['name']} ({project['date']})"):
                    Analytics.track_project_view(project['name'])
                    
                    # Project description
                    st.markdown(project["description"])
                    
                    # Tech stack badges
                    if 'tech_stack' in project:
                        st.write("**Technologies Used:**")
                        for tech in project['tech_stack']:
                            st.markdown(f"![{tech}](https://img.shields.io/badge/-{tech}-10B981?style=flat-square)")
                    
                    # Links
                    col1, col2 = st.columns(2)
                    with col1:
                        if project.get('live_demo'):
                            st.markdown(f"[🌐 Live Demo]({project['live_demo']})")
                    with col2:
                        if project.get('github_link'):
                            st.markdown(f"[💻 Source Code]({project['github_link']})")
                    
                    # Project metrics
                    metrics = PortfolioData.get_project_metrics().get(project['name'].split()[0], None)
                    if metrics:
                        st.write("**Project Metrics:**")
                        PortfolioUI.render_project_metrics(project['name'], metrics)

    @staticmethod
    def render_navigation() -> None:
        """Render top navigation menu."""
        st.markdown("""
            <div class="nav-container">
                <a href="#home" class="nav-link">🏠 Home</a>
                <a href="#skills" class="nav-link">🛠️ Skills</a>
                <a href="#projects" class="nav-link">💼 Projects</a>
                <a href="#experience" class="nav-link">🚀 Experience</a>
                <a href="#education" class="nav-link">📚 Education</a>
                <a href="#contact" class="nav-link">📫 Contact</a>
            </div>
            """, unsafe_allow_html=True)

    @staticmethod
    def setup_page() -> None:
        """Configure initial page settings."""
        st.set_page_config(
            page_title=config.PAGE_TITLE,
            page_icon="🚀",
            layout="wide",
            initial_sidebar_state="collapsed"
        )
        
        # Apply custom CSS
        st.markdown(get_custom_css(), unsafe_allow_html=True)
        
        # Render navigation menu
        PortfolioUI.render_navigation()

    @staticmethod
    def download_resume() -> None:
        """Add resume download button."""
        with open(config.RESUME_PATH, "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="resume.pdf",
                mime="application/pdf",
            )

    @staticmethod
    def home() -> None:
        """Render home section."""
        st.markdown("<div id='home'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if os.path.exists(config.PROFILE_IMAGE):
                image = Image.open(config.PROFILE_IMAGE)
                st.image(image, width=250)
            else:
                st.error("Profile picture not found. Please add 'photo.jpeg' to the project root.")
        
        with col2:
            st.title("Dimitar Pashev")
            st.subheader("Junior Developer")
            st.write("Burgas, Bulgaria | dim.pashev@gmail.com | 0876386033")
            st.write(
                "Links: [GitHub](https://github.com/dimipash) | "
                "[LinkedIn](https://www.linkedin.com/in/dimitar-pashev-994174274/)"
            )
            PortfolioUI.download_resume()

        st.markdown("---")
        st.header("Professional Summary")
        st.write(
            """
            Junior Developer with 2+ years of hands-on experience in software engineering.
            Proficient in Python and Django, with a keen eye for detail and a passion for
            creating seamless user experiences. Eager to leverage my technical skills and
            problem-solving abilities to contribute to a thriving IT team in Bulgaria.
            """
        )

    @staticmethod
    def experience() -> None:
        """Render experience section."""
        st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
        st.title("Employment History")
        
        jobs = [
            {
                "title": "MPI Operator",
                "company": "Bifrangi UK",
                "location": "Lincoln, UK",
                "date": "OCT 2017 - SEP 2022",
                "responsibilities": [
                    "Ensured quality control via MPI equipment operation",
                    "Boosted product quality by maintaining defect detection rates",
                    "Interpreted MPI results for process enhancements",
                    "Collaborated for swift quality issue resolutions",
                    "Implemented safety protocols, reducing workplace incidents",
                ],
            },
            {
                "title": "Production Operative",
                "company": "Parkacre",
                "location": "Lincoln",
                "date": "APR 2017 - SEP 2017",
                "responsibilities": [
                    "Operated machinery to ensure smooth production flow",
                    "Collaborated with team to meet daily production targets",
                ],
            },
            {
                "title": "Production Operative",
                "company": "Moypark",
                "location": "Lincoln",
                "date": "JAN 2015 - MAR 2017",
                "responsibilities": [
                    "Operated machinery to ensure smooth production flow",
                    "Collaborated with team to meet daily production targets",
                ],
            },
        ]
        
        for job in jobs:
            with st.expander(f"{job['title']} at {job['company']} ({job['date']})"):
                st.write(f"**Location:** {job['location']}")
                st.write("**Key Responsibilities:**")
                for responsibility in job["responsibilities"]:
                    st.write(f"- {responsibility}")

    @staticmethod
    def education() -> None:
        """Render education section."""
        st.markdown("<div id='education'></div>", unsafe_allow_html=True)
        st.title("Education")
        
        education_data = [
            {
                "degree": "Python Web Development",
                "school": "SoftUni",
                "date": "2023 - 2024",
                "details": [
                    "Python OOP",
                    "Python Web Basics (Django)",
                    "Python Web Framework (Django Advanced)",
                    "HTML & CSS",
                    "JavaScript Front-End",
                    "ReactJS",
                ],
            },
            {
                "degree": "Python Advanced",
                "school": "SoftUni",
                "date": "2023",
                "details": [
                    "Python Advanced",
                    "Python OOP",
                ],
            },
        ]
        
        for edu in education_data:
            with st.expander(f"{edu['degree']} - {edu['school']} ({edu['date']})"):
                for detail in edu["details"]:
                    st.write(f"- {detail}")

    @staticmethod
    def github() -> None:
        """Render GitHub section."""
        st.markdown("<div id='github'></div>", unsafe_allow_html=True)
        st.title("My GitHub Repositories")
        st.write("Here are some of my recent GitHub repositories:")
        github_username = "dimipash"
        url = f"https://api.github.com/users/{github_username}/repos"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes

            try:
                repos = response.json()
            except json.JSONDecodeError:
                st.error(f"Failed to decode JSON. Response content: {response.text}")
                return

            if not repos:
                st.warning("No repositories found.")
                return

            repos.sort(key=lambda r: r["updated_at"], reverse=True)

            for repo in repos[:20]:
                repo_languages_url = repo["languages_url"]
                languages_response = requests.get(repo_languages_url)
                languages = languages_response.json().keys()

                with st.expander(repo["name"]):
                    st.write(
                        f"**Description:** {repo.get('description', 'No description available')}"
                    )                 
                    homepage = repo.get('homepage')
                    if homepage:
                        st.write(f"**Live Version:** [{homepage}]({homepage})")
                    st.write(f"**Languages:** {', '.join(languages) if languages else 'Not specified'}")
                    # st.write(f"**Stars:** {repo['stargazers_count']}")
                    # st.write(f"**Forks:** {repo['forks_count']}")
                    last_updated = datetime.strptime(
                        repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ"
                    )
                    st.write(f"**Last Updated:** {last_updated.strftime('%Y-%m-%d')}")
                    st.write(
                        f"**Repository URL:** [{repo['html_url']}]({repo['html_url']})"
                    )              

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while fetching GitHub repositories: {str(e)}")
            if hasattr(e, "response") and e.response is not None:
                st.error(f"Response status code: {e.response.status_code}")
                st.error(f"Response content: {e.response.text}")
            st.error("Please check your internet connection and try again later.")

def main() -> None:
    """Main function to run the portfolio website."""
    ui = PortfolioUI()
    
    # Initialize page
    ui.setup_page()
    
    # Render main content sections
    ui.home()
    ui.skills()
    ui.projects()
    ui.experience()
    ui.education()
    ui.render_contact_form()

if __name__ == "__main__":
    main()
