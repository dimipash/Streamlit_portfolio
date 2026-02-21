"""
Portfolio Website built with Streamlit.
Author: Dimitar Pashev

This module implements a personal portfolio website using Streamlit framework.
It includes sections for skills, projects, contact information with improved
performance, security, and maintainability.
"""

import logging

import streamlit as st

from analytics import Analytics
from components import PortfolioComponents
from config import Config
from data import PortfolioData
from styles import get_custom_css

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class PortfolioApp:
    """Main portfolio application class with error handling and performance optimizations."""

    def __init__(self):
        """Initialize portfolio application with configuration and components."""
        self.config = Config()
        self.components = PortfolioComponents()
        self.setup_page()
        self.track_visit()

    def setup_page(self) -> None:
        """Configure initial page settings and styling."""
        try:
            st.set_page_config(
                page_title=self.config.PAGE_TITLE,
                layout="wide",
                initial_sidebar_state="collapsed",
            )
            st.markdown(get_custom_css(), unsafe_allow_html=True)
        except Exception as e:
            logger.error(f"Failed to setup page: {str(e)}")
            st.error("An error occurred while setting up the page. Please refresh.")

    def track_visit(self) -> None:
        """Track website visit if not already tracked in current session."""
        if "visit_tracked" not in st.session_state:
            Analytics.track_visit()
            st.session_state.visit_tracked = True
            logger.info("New visit tracked")

    def create_navbar(self) -> None:
        """Create responsive navigation bar with error handling."""
        try:
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
        except Exception as e:
            logger.error(f"Failed to create navbar: {str(e)}")
            st.error("Navigation menu could not be loaded.")

    def render_sections(self) -> None:
        """Render all portfolio sections with error handling."""
        sections = [
            ("Home", self.render_home),
            ("Skills", self.render_skills),
            ("Projects", self.render_projects),
            ("Experience", self.render_experience),
            ("Education", self.render_education),
            ("GitHub", self.render_github),
            ("Courses", self.render_courses),
            ("Contact", self.render_contact),
        ]

        for section_name, render_func in sections:
            try:
                render_func()
            except Exception as e:
                logger.error(f"Error rendering {section_name} section: {str(e)}")
                st.error(f"Failed to load {section_name} section. Please refresh the page.")

    def render_home(self) -> None:
        """Render home section."""
        st.markdown("<div id='home'></div>", unsafe_allow_html=True)
        self.components.render_profile_section()

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

    def render_skills(self) -> None:
        """Render skills section."""
        st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
        st.title("Skills 🛠️")

        st.header("Technical Skills")
        self.components.render_skills_section(PortfolioData.get_skills_data())

        st.header("Soft Skills")
        soft_skills = PortfolioData.get_soft_skills()
        cols = st.columns(3)
        for i, skill in enumerate(soft_skills):
            with cols[i % 3]:
                st.markdown(f"✨ {skill}")

    def render_projects(self) -> None:
        """Render projects section."""
        st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
        self.components.render_projects_section()

    def render_experience(self) -> None:
        """Render experience section."""
        st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
        st.title("Employment History")

        jobs = PortfolioData.get_employment_history()

        for job in jobs:
            with st.expander(f"{job['title']} at {job['company']} ({job['date']})"):
                st.write(f"**Location:** {job['location']}")
                st.write("**Key Responsibilities:**")
                for responsibility in job["responsibilities"]:
                    st.write(f"- {responsibility}")

    def render_education(self) -> None:
        """Render education section."""
        st.markdown("<div id='education'></div>", unsafe_allow_html=True)
        st.title("Education")

        education_data = PortfolioData.get_education_data()

        for edu in education_data:
            with st.expander(f"{edu['degree']} - {edu['school']} ({edu['date']})"):
                for detail in edu["details"]:
                    st.write(f"- {detail}")

    def render_github(self) -> None:
        """Render GitHub section."""
        st.markdown("<div id='github'></div>", unsafe_allow_html=True)
        self.components.render_github_section()

    def render_courses(self) -> None:
        """Render courses section."""
        st.markdown("<div id='courses'></div>", unsafe_allow_html=True)
        st.title("Courses")
        courses = [
            (
                "Data Analysis with Python",
                "SEP 2025 - OCT 2025",
                "https://www.freecodecamp.org/certification/dpashev/data-analysis-with-python-v7",
            ),
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

    def render_contact(self) -> None:
        """Render contact section."""
        st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
        self.components.render_contact_form()

    def run(self) -> None:
        """Run the portfolio application with error handling."""
        try:
            self.create_navbar()
            self.render_sections()
            self.components.render_footer()

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
        except Exception as e:
            logger.error(f"Application error: {str(e)}")
            st.error(
                """
                An error occurred while running the application.
                Please refresh the page or contact support if the issue persists.
                """
            )


if __name__ == "__main__":
    app = PortfolioApp()
    app.run()

st.markdown(
    """
<iframe src="https://app.vectorshift.ai/chatbots/embedded/67d84b6f7e6f30aec4d9dd9c?openChatbot=true" width="500px" height="500px" style="border: 1px solid var(--border-color); position: fixed; bottom: 0; right: 0; margin: 10px; z-index: 1000; background: transparent;" allow="clipboard-read; clipboard-write; microphone"/>
    """,
    unsafe_allow_html=True,
)
