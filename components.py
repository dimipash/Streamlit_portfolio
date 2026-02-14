"""
UI components module for the portfolio website.
Contains reusable UI components with caching and performance optimizations.
"""

from typing import List, Dict, Union, Optional
import os
import re
import streamlit as st
from PIL import Image
import requests
from datetime import datetime
from functools import lru_cache

from config import Config
from analytics import Analytics
from data import PortfolioData


def is_valid_email(email: str) -> bool:
    """
    Validate email format using regex.

    Args:
        email (str): Email address to validate

    Returns:
        bool: True if email is valid, False otherwise
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


class PortfolioComponents:
    """UI components for the portfolio website with caching."""

    def __init__(self):
        """Initialize PortfolioComponents with configuration."""
        self.config = Config()

    @staticmethod
    @st.cache_data(ttl=3600)  # Cache for 1 hour
    def load_image(image_path: str) -> Optional[Image.Image]:
        """
        Load and cache image.

        Args:
            image_path (str): Path to image file

        Returns:
            Optional[Image.Image]: Loaded image or None if loading fails
        """
        try:
            return Image.open(image_path)
        except Exception as e:
            st.error(f"Failed to load image: {str(e)}")
            return None

    @staticmethod
    @st.cache_data(ttl=3600)
    def fetch_github_data(username: str) -> Dict:
        """
        Fetch and cache GitHub data with optional authentication.

        Args:
            username (str): GitHub username

        Returns:
            Dict: GitHub repository data
        """
        url = f"https://api.github.com/users/{username}/repos"
        try:
            headers = {}
            github_token = os.getenv("GITHUB_TOKEN")
            if github_token:
                headers["Authorization"] = f"token {github_token}"

            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch GitHub data: {str(e)}")
            return {}

    def render_profile_section(self) -> None:
        """Render profile section with image and information."""
        col1, col2 = st.columns([1, 2])

        with col1:
            image = self.load_image(self.config.PROFILE_IMAGE)
            if image:
                st.image(image, width=250)

        with col2:
            st.title("Dimitar Pashev")
            st.subheader("Junior Developer")
            st.write("Bulgaria | dim.pashev@gmail.com | 0876386033")
            st.write(
                "Links: [GitHub](https://github.com/dimipash) | "
                "[LinkedIn](https://www.linkedin.com/in/dimitar-pashev-994174274/)"
            )
            self.render_resume_download()

    def render_resume_download(self) -> None:
        """Render resume download button."""
        try:
            with open(self.config.RESUME_PATH, "rb") as file:
                st.download_button(
                    label="Download Resume",
                    data=file,
                    file_name="resume.pdf",
                    mime="application/pdf",
                )
        except FileNotFoundError:
            st.error("Resume file not found.")

    @staticmethod
    def render_skills_section(
        skills_data: Dict[str, Dict[str, Union[int, str, float]]],
    ) -> None:
        """
        Render skills section with categories and proficiency bars.

        Args:
            skills_data (Dict): Skills data with proficiency levels
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

    @staticmethod
    def render_project_metrics(
        project_name: str, metrics: Dict[str, Union[int, float, str]]
    ) -> None:
        """
        Render project metrics in columns.

        Args:
            project_name (str): Name of the project
            metrics (Dict): Project metrics data
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

    def render_projects_section(self) -> None:
        """Render projects section with filtering and metrics."""
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

    def render_github_section(self) -> None:
        """Render GitHub repositories section with caching."""
        st.title("My GitHub Repositories")

        repos = self.fetch_github_data(self.config.GITHUB_USERNAME)
        if not repos:
            st.warning("No repositories found or unable to fetch data.")
            return

        repos.sort(key=lambda r: r["updated_at"], reverse=True)
        for repo in repos[:20]:  # Show latest 20 repos
            with st.expander(repo["name"]):
                st.write(
                    f"**Description:** {repo.get('description', 'No description available')}"
                )
                if repo.get("homepage"):
                    st.write(
                        f"**Live Version:** [{repo['homepage']}]({repo['homepage']})"
                    )

                # Fetch languages
                languages_url = repo["languages_url"]
                try:
                    languages_response = requests.get(languages_url, timeout=10)
                    languages = languages_response.json().keys()
                    st.write(f"**Languages:** {', '.join(languages)}")
                except requests.exceptions.RequestException:
                    st.write("**Languages:** Unable to fetch languages")

                last_updated = datetime.strptime(
                    repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ"
                )
                st.write(f"**Last Updated:** {last_updated.strftime('%Y-%m-%d')}")
                st.write(
                    f"**Repository URL:** [{repo['html_url']}]({repo['html_url']})"
                )

    @staticmethod
    def render_contact_form() -> None:
        """Render contact form with validation and rate limiting."""
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

                if not is_valid_email(email):
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
                    # Clear form
                    st.session_state.name = ""
                    st.session_state.email = ""
                    st.session_state.subject = ""
                    st.session_state.message = ""

    @staticmethod
    def render_footer() -> None:
        """Render footer section."""
        st.markdown(
            """
            <div class="footer">
                <p>© 2025 Dimitar Pashev. All rights reserved.</p>
                <p>Built with ❤️ using Streamlit</p>
                <p>
                    <a href="https://github.com/dimipash" target="_blank">GitHub</a> • 
                    <a href="https://www.linkedin.com/in/dimitar-pashev-994174274/" target="_blank">LinkedIn</a>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
