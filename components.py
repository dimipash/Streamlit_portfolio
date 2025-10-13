"""
UI components module for the portfolio website.
Contains reusable UI components with caching and performance optimizations.
"""

from typing import List, Dict, Union, Optional
import streamlit as st
from PIL import Image
import requests
from datetime import datetime
from functools import lru_cache

from config import Config
from analytics import Analytics
from data import PortfolioData


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
        Fetch and cache GitHub data.

        Args:
            username (str): GitHub username

        Returns:
            Dict: GitHub repository data
        """
        url = f"https://api.github.com/users/{username}/repos"
        try:
            response = requests.get(url, timeout=10)
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
    def render_skills_section(skills_data: Dict[str, Dict[str, Union[int, str, float]]]) -> None:
        """
        Render skills section with categories and proficiency bars.

        Args:
            skills_data (Dict): Skills data with proficiency levels
        """
        categories = sorted(list(set(skill["category"] for skill in skills_data.values())))

        for category in categories:
            st.subheader(f"🔹 {category}")
            skills_in_category = {
                skill: data
                for skill, data in skills_data.items()
                if data["category"] == category
            }
            sorted_skills = sorted(
                skills_in_category.items(), key=lambda item: item[1]["proficiency"], reverse=True
            )

            skill_chunks = [sorted_skills[i:i + 3] for i in range(0, len(sorted_skills), 3)]

            for chunk in skill_chunks:
                cols = st.columns(len(chunk))
                for i, (skill, data) in enumerate(chunk):
                    with cols[i]:
                        st.markdown(
                            f"<div style='text-align: center;'><strong>{skill}</strong></div>",
                            unsafe_allow_html=True,
                        )
                        st.progress(data["proficiency"] / 100)

    @staticmethod
    def render_project_metrics(project_name: str, metrics: Dict[str, Union[int, float, str]]) -> None:
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
            st.metric("Commits", metrics['commits'])
        with cols[2]:
            st.metric("GitHub Stars", metrics['stars'])
        with cols[3]:
            st.metric("Status", metrics['status'])

    def render_projects_section(self) -> None:
        """Render projects section with filtering and metrics."""
        st.title("Personal Projects")

        projects = PortfolioData.get_projects_data()
        all_techs = sorted(list(set(tech for proj in projects for tech in proj.get("tech_stack", []))))

        tech_filter = st.multiselect(
            "Filter by Technology",
            all_techs,
        )

        for project in projects:
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
                    st.write(f"**Live Version:** [{repo['homepage']}]({repo['homepage']})")
                
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
                    st.experimental_rerun()

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
