import os
import streamlit as st
import pandas as pd
from PIL import Image
import requests
import json
from datetime import datetime
from styles import get_custom_css


# Set page config
st.set_page_config(
    page_title="Dimitar Pashev - Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)


def download_resume():

    resume_path = "resume.pdf"
    with open(resume_path, "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="resume.pdf",
            mime="application/pdf",
        )


# Sidebar navigation
def sidebar():
    with st.sidebar:
        st.title("Navigation")
        page = st.radio(
            "Go to",
            [
                "Home",
                "Skills",
                "Projects",
                "Experience",
                "Education",
                "GitHub",
            ],
        )
    return page


# Home page
def home():
    col1, col2 = st.columns([1, 2])
    with col1:

        image_path = "photo.jpeg"
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=250)
        else:
            st.error(
                "Profile picture not found. Please add 'profile_picture.jpg' to the project root."
            )
    with col2:
        st.title("Dimitar Pashev")
        st.subheader("Junior Developer")
        st.write("Burgas, Bulgaria | dim.pashev@gmail.com | 0876386033")
        st.write(
            "Links: [GitHub](https://github.com/dimipash) | [LinkedIn](https://www.linkedin.com/in/dimitar-pashev-994174274/)"
        )

        download_resume()

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


def skills():
    st.title("Technical Skills")

    skills_data = {
        "Python": 90,
        "Django": 85,
        "ReactJS": 75,
        "JavaScript": 70,
        "CSS": 75,
        "HTML": 80,
        "Linux": 70,
        "API Development": 80,
        "PostgreSQL": 75,
        "Version Control": 85,
        "Bash": 70,
        "Database Management": 80,
    }

    for skill, proficiency in skills_data.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(f"{skill}")
        with col2:
            st.progress(proficiency / 100)

    st.title("Soft Skills")
    soft_skills = [
        "Communication",
        "Team Player",
        "Problem-Solving",
        "Adaptability",
        "Attention To Detail",
    ]
    for skill in soft_skills:
        st.write(f"- {skill}")


def projects():
    st.title("Personal Projects")

    projects_data = [
        {
            "name": "Online Shop Django Project",
            "date": "03/2024 - 04/2024",
            "description": "Comprehensive set of features for managing an online shopping platform. Custom user model, categories and products, shopping cart, orders, inventory, user account management, PayPal payments.",
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

    for project in projects_data:
        with st.expander(f"{project['name']} ({project['date']})"):
            st.markdown(
                f"<div class='project-card'>{project['description']}</div>",
                unsafe_allow_html=True,
            )


def experience():
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
                "Operated machinery to ensure smooth production flow, reducing downtime by maintaining equipment",
                "Collaborated with team to meet daily production targets, improving overall efficiency",
            ],
        },
        {
            "title": "Production Operative",
            "company": "Moypark",
            "location": "Lincoln",
            "date": "JAN 2015 - MAR 2017",
            "responsibilities": [
                "Operated machinery to ensure smooth production flow, reducing downtime by maintaining equipment",
                "Collaborated with team to meet daily production targets, improving overall efficiency",
            ],
        },
        {
            "title": "Phone Agent",
            "company": "Kronos Recovery Management",
            "location": "Sofia",
            "date": "SEP 2012 - DEC 2013",
            "responsibilities": [
                "Managed outbound calls to recover debts",
                "Resolved customer disputes through effective communication, improving client satisfaction",
                "Collaborated with team members to develop strategies for difficult cases, enhancing overall efficiency",
            ],
        },
    ]

    for job in jobs:
        with st.expander(f"{job['title']} at {job['company']} ({job['date']})"):
            st.write(f"**Location:** {job['location']}")
            st.write("**Responsibilities:**")
            for resp in job["responsibilities"]:
                st.write(f"- {resp}")


# Education page
def education():
    st.title("Education")

    educations = [
        {
            "degree": "Software Engineering",
            "institution": "SoftUni",
            "location": "Sofia, Bulgaria",
            "date": "SEP 2021 - DEC 2023",
        },
        {
            "degree": "Economics of Defence and Security",
            "institution": "University Of National And World Economy",
            "location": "Sofia",
            "date": "SEP 2006 - JUN 2010",
        },
        {
            "degree": "Mathematics with English",
            "institution": "Gymnasium of Natural Sciences and Mathematics",
            "location": "Sliven",
            "date": "SEP 2001 - MAY 2006",
        },
    ]

    for edu in educations:
        st.markdown(
            f"""
        <div class='project-card'>
            <h3>{edu['degree']}</h3>
            <p>{edu['institution']}, {edu['location']}</p>
            <p>{edu['date']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.header("Courses")
    courses = [
        ("Python OOP at SoftUni", "OCT 2022 - DEC 2022"),
        ("Algorithms with Python at SoftUni", "JUL 2023 - AUG 2023"),
        ("Python Web Basics at SoftUni", "MAY 2023 - JUN 2023"),
        ("Python Web Framework at SoftUni", "JUN 2023 - AUG 2023"),
        ("HTML & CSS at SoftUni", "JAN 2023 - FEB 2023"),
        ("ReactJS at SoftUni", "OCT 2023 - DEC 2023"),
        ("Foundational C# with Microsoft at Microsoft", "DEC 2023 - DEC 2023"),
    ]

    for course, date in courses:
        st.write(f"- **{course}** ({date})")


def github():
    st.title("My GitHub Repositories")
    st.write("Here are some of my recent GitHub repositories:")

    github_username = "dimipash"

    url = f"https://api.github.com/users/dimipash/repos"
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
            with st.expander(repo["name"]):
                st.write(
                    f"**Description:** {repo.get('description', 'No description available')}"
                )
                st.write(f"**Language:** {repo.get('language', 'Not specified')}")
                st.write(f"**Stars:** {repo['stargazers_count']}")
                st.write(f"**Forks:** {repo['forks_count']}")
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


def main():
    page = sidebar()

    if page == "Home":
        home()
    elif page == "Skills":
        skills()
    elif page == "Projects":
        projects()
    elif page == "Experience":
        experience()
    elif page == "Education":
        education()
    elif page == "GitHub":
        github()


if __name__ == "__main__":
    main()
