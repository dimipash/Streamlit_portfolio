"""
Portfolio Website built with Streamlit.
Author: Dimitar Pashev

This module implements a personal portfolio website using Streamlit framework.
It includes sections for skills, projects, contact information, and chat support.
"""

import os
from dataclasses import dataclass
from typing import List, Dict, Union, Optional
from datetime import datetime
import streamlit as st
from PIL import Image
import requests
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from dotenv import load_dotenv
from styles import get_custom_css
from streamlit.components.v1 import html
from chat import Chatbot
from data import PortfolioData

# Set page configuration at the very beginning
st.set_page_config(
    page_title="Dimitar Pashev - Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Type aliases for better code readability
SkillsDict = Dict[str, Dict[str, Union[int, str, float]]]
ProjectDict = Dict[str, str]
JobDict = Dict[str, Union[str, List[str]]]
MetricsDict = Dict[str, Dict[str, Union[int, float, str]]]


@dataclass
class Config:
    """Configuration settings for the portfolio website."""

    PROFILE_IMAGE: str = "photo.jpeg"
    RESUME_PATH: str = "resume.pdf"
    PAGE_TITLE: str = "Dimitar Pashev - Portfolio"
    GITHUB_USERNAME: str = "dimipash"
    CONTACT_EMAIL: str = "dim.pashev@gmail.com"

    @staticmethod
    def load_email_config() -> Dict[str, Union[str, int]]:
        """
        Load email configuration from environment variables.

        Returns:
            Dict[str, Union[str, int]]: Email configuration settings
        """
        load_dotenv()
        return {
            "host": os.getenv("EMAIL_HOST", "smtp.gmail.com"),
            "port": int(os.getenv("EMAIL_PORT", "587")),
            "username": os.getenv("EMAIL_USERNAME"),
            "password": os.getenv("EMAIL_PASSWORD"),
        }

    @staticmethod
    def send_email(subject: str, body: str, from_email: str) -> bool:
        """
        Send email using SMTP configuration.

        Args:
            subject (str): Email subject
            body (str): Email body content
            from_email (str): Sender's email address

        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            email_config = Config.load_email_config()

            if not all([email_config["username"], email_config["password"]]):
                st.error("Email configuration is incomplete. Please check .env file.")
                return False

            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = Config.CONTACT_EMAIL
            msg["Subject"] = f"Portfolio Contact: {subject}"

            full_body = f"""
            From: {from_email}\n\n{body}
            """

            msg.attach(MIMEText(full_body, "plain"))

            with smtplib.SMTP(email_config["host"], email_config["port"]) as server:
                server.starttls()
                server.login(email_config["username"], email_config["password"])
                server.send_message(msg)

            return True
        except Exception as e:
            st.error(f"Failed to send email: {str(e)}")
            return False


class Analytics:
    """Analytics tracking for portfolio interactions."""

    @staticmethod
    def track_project_view(project_name: str) -> None:
        """
        Track when a project is viewed.

        Args:
            project_name (str): Name of the viewed project
        """
        if "project_views" not in st.session_state:
            st.session_state.project_views = {}

        if project_name not in st.session_state.project_views:
            st.session_state.project_views[project_name] = 0
        st.session_state.project_views[project_name] += 1

    @staticmethod
    def track_contact_submission() -> None:
        """Track when contact form is submitted."""
        if "contact_submissions" not in st.session_state:
            st.session_state.contact_submissions = 0
        st.session_state.contact_submissions += 1




class PortfolioUI:
    """UI components and layout for the portfolio website."""

    def __init__(self):
        """Initialize PortfolioUI instance."""
        self.config = Config()

    def setup_page(self) -> None:
        """Configure initial page settings."""
        st.markdown(get_custom_css(), unsafe_allow_html=True)

    def render_skills_section(self, skills_data: SkillsDict) -> None:
        """
        Render skills in a clean, organized format.

        Args:
            skills_data (SkillsDict): Dictionary of skills with their details
        """
        skills_by_category = {}
        for skill, data in skills_data.items():
            category = data["category"]
            if category not in skills_by_category:
                skills_by_category[category] = []
            skills_by_category[category].append((skill, data["proficiency"]))

        for category, skills in skills_by_category.items():
            st.subheader(f"🔹 {category}")
            skill_chunks = [skills[i : i + 3] for i in range(0, len(skills), 3)]
            for chunk in skill_chunks:
                cols = st.columns(len(chunk))
                for i, (skill, proficiency) in enumerate(
                    sorted(chunk, key=lambda x: x[1], reverse=True)
                ):
                    with cols[i]:
                        st.markdown(
                            f"<div style='text-align: center;'><strong>{skill}</strong></div>",
                            unsafe_allow_html=True,
                        )
                        st.progress(proficiency / 100)

    def skills(self) -> None:
        """Render skills section."""
        st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
        st.title("Skills 🛠️")

        skills_data = PortfolioData.get_skills_data()

        st.header("Technical Skills")
        self.render_skills_section(skills_data)

        st.header("Soft Skills")
        soft_skills = PortfolioData.get_soft_skills()
        cols = st.columns(3)
        for i, skill in enumerate(soft_skills):
            with cols[i % 3]:
                st.markdown(f"✨ {skill}")

    def render_contact_form(self) -> None:
        """Render an interactive contact form."""
        st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
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

                if not "@" in email:
                    st.error("Please enter a valid email address")
                    return

                formatted_message = f"""
                Name: {name}
                Message:
                {message}
                """

                if Config.send_email(subject, formatted_message, email):
                    st.success("Thank you for your message! I'll get back to you soon.")
                    Analytics.track_contact_submission()
                    st.session_state.name = ""
                    st.session_state.email = ""
                    st.session_state.subject = ""
                    st.session_state.message = ""

    def render_project_metrics(
        self, project_name: str, metrics: Dict[str, Union[int, float, str]]
    ) -> None:
        """
        Render metrics for a project.

        Args:
            project_name (str): Name of the project
            metrics (Dict[str, Union[int, float, str]]): Project metrics
        """
        cols = st.columns(4)
        with cols[0]:
            st.metric("Code Coverage", f"{metrics['code_coverage']}%")
        with cols[1]:
            st.metric("Commits", metrics["commits"])
        with cols[2]:
            st.metric("GitHub Stars", metrics["stars"])
        with cols[3]:
            st.metric("Status", metrics["status"])

    def projects(self) -> None:
        """Render projects section with enhanced interactivity."""
        st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
        st.title("Personal Projects")

        tech_filter = st.multiselect(
            "Filter by Technology",
            ["Python", "Django", "React", "JavaScript", "PostgreSQL"],
        )

        for project in PortfolioData.get_projects_data():
            if not tech_filter or any(
                tech in project.get("tech_stack", []) for tech in tech_filter
            ):
                with st.expander(f"{project['name']} ({project['date']})"):
                    Analytics.track_project_view(project["name"])

                    st.markdown(project["description"])

                    if "tech_stack" in project:
                        st.write("**Technologies Used:**")
                        for tech in project["tech_stack"]:
                            st.markdown(
                                f"![{tech}](https://img.shields.io/badge/-{tech}-10B981?style=flat-square)"
                            )

                    col1, col2 = st.columns(2)
                    with col1:
                        if project.get("live_demo"):
                            st.markdown(f"[🌐 Live Demo]({project['live_demo']})")
                    with col2:
                        if project.get("github_link"):
                            st.markdown(f"[💻 Source Code]({project['github_link']})")

                    metrics = PortfolioData.get_project_metrics().get(
                        project["name"].split()[0], None
                    )
                    if metrics:
                        st.write("**Project Metrics:**")
                        self.render_project_metrics(project["name"], metrics)

    def render_navigation(self) -> None:
        """Render top navigation menu."""
        menu_items = [
            ("Home", "home", "🏠", self.home),
            ("Skills", "skills", "🛠️", self.skills),
            ("Projects", "projects", "💼", self.projects),
            ("Experience", "experience", "🚀", self.experience),
            ("Education", "education", "📚", self.education),
            ("GitHub", "github", "🔗", self.github),
            ("Courses", "courses", "🎓", self.courses),
            ("Contact", "contact", "📫", self.render_contact_form),
        ]

        nav_html = "".join(
            [
                f'<a href="#{link}" class="nav-link" style="font-size: 18px;">{icon} {name}</a>'
                for name, link, icon, _ in menu_items
            ]
        )

        st.markdown(
            f"""
            <div class="nav-container">
                <div class="navigation">{nav_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def download_resume(self) -> None:
        """Add resume download button."""
        with open(Config.RESUME_PATH, "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="resume.pdf",
                mime="application/pdf",
            )

    def home(self) -> None:
        """Render home section."""
        st.markdown("<div id='home'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])

        with col1:
            if os.path.exists(Config.PROFILE_IMAGE):
                image = Image.open(Config.PROFILE_IMAGE)
                st.image(image, width=250)
            else:
                st.error(
                    "Profile picture not found. Please add 'photo.jpeg' to the project root."
                )

        with col2:
            st.title("Dimitar Pashev")
            st.subheader("Junior Developer")
            st.write("Burgas, Bulgaria | dim.pashev@gmail.com | 0876386033")
            st.write(
                "Links: [GitHub](https://github.com/dimipash) | "
                "[LinkedIn](https://www.linkedin.com/in/dimitar-pashev-994174274/)"
            )
            self.download_resume()

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

    def experience(self) -> None:
        """Render experience section."""
        st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
        st.title("Employment History")

        jobs = [
            {
                "title": "MPI Operator",
                "company": "Bifrangi UK",
                "location": "Lincoln, UK",
                "date": "OCT 2017 - SEP 2024",
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
            {
                "title": "Production Worker",
                "company": "Hall Hunter Partnership",
                "location": "Chichester",
                "date": "JAN 2014 - SEP 2014",
                "responsibilities": [
                    "Aggriculture and maintenance of farm equipment",
                ],
            },
            {
                "title": "Phone Agent Debt Collector",
                "company": "Kronos Recovery Management",
                "location": "Sofia",
                "date": "SEP 2012 - DEC 2013",
                "responsibilities": [
                    "Collected debts from customers",
                    "Provided phone support to customers",
                ],                
            },
            {
                "title": "Security Guard",
                "company": "Bodu SOD",
                "location": "Sofia",
                "date": "SEP 2010 - SEP 2011",
                "responsibilities": [
                    "Collected debts from customers",
                    "Provided phone support to customers",
                ],                
            },
        ]

        for job in jobs:
            with st.expander(f"{job['title']} at {job['company']} ({job['date']})"):
                st.write(f"**Location:** {job['location']}")
                st.write("**Key Responsibilities:**")
                for responsibility in job["responsibilities"]:
                    st.write(f"- {responsibility}")

    def education(self) -> None:
        """Render education section."""
        st.markdown("<div id='education'></div>", unsafe_allow_html=True)
        st.title("Education")

        education_data = [
            {
                "degree": "Python Web Developer",
                "school": "SoftUni",
                "date": "2022 - 2024",
                "details": [
                    "Python OOP",
                    "Python Advanced",
                    "Python Web Basics (Django)",
                    "Python Web Framework (Django Advanced)",
                    "HTML & CSS",
                    "JavaScript Front-End",
                    "ReactJS",
                ],
            },
            {
                "degree": "Economics of Defense and Security",
                "school": "University Of National And World Economy",
                "date": "SEP 2006 - JUN 2010",
                "location": "Sofia",
                "details": [
                    "Economics of Defense and Security",
                ],
            },
            {
                "degree": "Mathematics with English",
                "school": "Gymnasium of Natural Sciences and Mathematics",
                "location": "Sliven",
                "date": "SEP 2001 - MAY 2006",
                "details": [
                    "Mathematics with English",
                ],
            },
        ]

        for edu in education_data:
            with st.expander(f"{edu['degree']} - {edu['school']} ({edu['date']})"):
                for detail in edu["details"]:
                    st.write(f"- {detail}")

    def github(self) -> None:
        """Render GitHub section."""
        st.markdown("<div id='github'></div>", unsafe_allow_html=True)
        st.title("My GitHub Repositories")
        st.write("Here are some of my recent GitHub repositories:")
        github_username = self.config.GITHUB_USERNAME
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
                    homepage = repo.get("homepage")
                    if homepage:
                        st.write(f"**Live Version:** [{homepage}]({homepage})")
                    st.write(
                        f"**Languages:** {', '.join(languages) if languages else 'Not specified'}"
                    )
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

    def courses(self) -> None:
        """Render courses section."""
        st.markdown("<div id='courses'></div>", unsafe_allow_html=True)
        st.title("Courses")
        courses = [
            (
                "Python OOP at SoftUni",
                "OCT 2022 - DEC 2022",
                "https://softuni.bg/certificates/details/150462/c3e3696e",
            ),
            (
                "Algorithms with Python at SoftUni",
                "JUL 2023 - AUG 2023",
                "https://softuni.bg/certificates/details/181201/864df479",
            ),
            (
                "Python Web Basics at SoftUni",
                "MAY 2023 - JUN 2023",
                "https://softuni.bg/certificates/details/177835/4657f045",
            ),
            (
                "Python Web Framework at SoftUni",
                "JUN 2023 - AUG 2023",
                "https://softuni.bg/certificates/details/182365/619a7290",
            ),
            (
                "HTML & CSS at SoftUni",
                "JAN 2023 - FEB 2023",
                "https://softuni.bg/certificates/details/163183/5a08c061",
            ),
            (
                "ReactJS at SoftUni",
                "OCT 2023 - DEC 2023",
                "https://softuni.bg/certificates/details/197959/a9d12e96",
            ),
            (
                "Foundational C# with Microsoft at Microsoft at freecodecamp",
                "DEC 2023 - DEC 2023",
                "https://www.freecodecamp.org/certification/dpashev/foundational-c-sharp-with-microsoft",
            ),
        ]
        for course, date, link in courses:
            st.write(f"- **{course}** ({date}) [Certificate]({link})")


    def footer(self) -> None:
        """Render footer section."""
        st.markdown(
            """
        <div class="footer">
            <p> 2024 Dimitar Pashev. All rights reserved.</p>
            <p>Built with ❤️ using Streamlit</p>
            <p>
                <a href="https://github.com/dimipash" target="_blank">GitHub</a> • 
                <a href="https://www.linkedin.com/in/dimitar-pashev-994174274/" target="_blank">LinkedIn</a>
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )


# Function to create the fixed navigation bar
def create_navbar():
    """Create responsive navigation bar with all section links."""
    nav_items = [
        ("🏠 Home", "home"),
        ("🛠️ Skills", "skills"),
        ("💼 Projects", "projects"),
        ("🚀 Experience", "experience"),
        ("📚 Education", "education"),
        ("🔗 GitHub", "github"),
        ("🎓 Courses", "courses"),
        ("📫 Contact", "contact"),
    ]

    nav_links = "\n".join(
        [
            f'<a href="#{section}" class="nav-link">{label}</a>'
            for label, section in nav_items
        ]
    )

    st.markdown(
        f"""
    <nav class="nav-container">
        <div class="navigation">
            {nav_links}
        </div>
    </nav>
    """,
        unsafe_allow_html=True,
    )


# Main function to render the page
def main():
    create_navbar()
    ui = PortfolioUI()
    ui.setup_page()

    # Main content sections
    ui.home()
    ui.skills()
    ui.projects()
    ui.experience()
    ui.education()
    ui.github()
    ui.courses()
    ui.render_contact_form()
    # Footer at the bottom
    ui.footer()
    
    chatbot = Chatbot()
    chatbot.display_chat()


# Ensure smooth scrolling behavior
st.markdown(
    """
<style>
    html {
        scroll-behavior: smooth;
    }
</style>
""",
    unsafe_allow_html=True,
)

if __name__ == "__main__":
    main()
