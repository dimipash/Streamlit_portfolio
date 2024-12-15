from typing import List, Dict, Union

SkillsDict = Dict[str, Dict[str, Union[int, str, float]]]
ProjectDict = Dict[str, str]
JobDict = Dict[str, Union[str, List[str]]]
MetricsDict = Dict[str, Dict[str, Union[int, float, str]]]


class PortfolioData:
    """Data container for portfolio content."""

    @staticmethod
    def get_skills_data() -> SkillsDict:
        """
        Returns technical skills with proficiency levels and categories.

        Returns:
            SkillsDict: Dictionary of skills with their details
        """
        return {
            "Python": {
                "proficiency": 90,
                "category": "Languages",
                "experience_years": 2,
            },
            "Django": {
                "proficiency": 85,
                "category": "Frameworks",
                "experience_years": 1.5,
            },
            "ReactJS": {
                "proficiency": 75,
                "category": "Frontend",
                "experience_years": 1,
            },
            "JavaScript": {
                "proficiency": 70,
                "category": "Languages",
                "experience_years": 1,
            },
            "CSS": {"proficiency": 75, "category": "Frontend", "experience_years": 1.5},
            "HTML": {
                "proficiency": 80,
                "category": "Frontend",
                "experience_years": 1.5,
            },
            "Linux": {"proficiency": 70, "category": "Tools", "experience_years": 2},
            "API Development": {
                "proficiency": 80,
                "category": "Backend",
                "experience_years": 1.5,
            },
            "PostgreSQL": {
                "proficiency": 75,
                "category": "Databases",
                "experience_years": 1,
            },
            "Version Control": {
                "proficiency": 85,
                "category": "Tools",
                "experience_years": 2,
            },
            "Bash": {"proficiency": 70, "category": "Tools", "experience_years": 1},
            "Database Management": {
                "proficiency": 80,
                "category": "Databases",
                "experience_years": 1.5,
            },
        }

    @staticmethod
    def get_project_metrics() -> MetricsDict:
        """
        Returns project metrics and statistics.

        Returns:
            MetricsDict: Dictionary of project metrics
        """
        return {
            "Online Shop": {
                "code_coverage": 85,
                "commits": 120,
                "stars": 15,
                "complexity": "Medium",
                "status": "Active",
            },
            "SaaS Platform": {
                "code_coverage": 90,
                "commits": 200,
                "stars": 25,
                "complexity": "High",
                "status": "Active",
            },
            "Notes App": {
                "code_coverage": 75,
                "commits": 50,
                "stars": 8,
                "complexity": "Low",
                "status": "Completed",
            },
        }

    @staticmethod
    def get_soft_skills() -> List[str]:
        """
        Returns list of soft skills.

        Returns:
            List[str]: List of soft skills
        """
        return [
            "Communication",
            "Team Player",
            "Problem-Solving",
            "Adaptability",
            "Attention To Detail",
        ]

    @staticmethod
    def get_projects_data() -> List[ProjectDict]:
        """
        Returns list of project information.

        Returns:
            List[ProjectDict]: List of project dictionaries
        """
        return [
            {
                "name": "Online Shop Django Project",
                "date": "03/2024 - 04/2024",
                "description": "[Online Shop](https://dimipi.pythonanywhere.com/) - a comprehensive set of features for managing an online shopping platform. Custom user model, categories and products, shopping cart, orders, inventory, user account management, PayPal payments.",
                "tech_stack": [
                    "Python",
                    "Django",
                    "PostgreSQL",
                    "JavaScript",
                    "Bootstrap",
                ],
                "live_demo": "https://dimipi.pythonanywhere.com/",
                "github_link": "https://github.com/dimipash/OnlineShop",
            },
            {
                "name": "SaaS Django Project",
                "date": "08/2024 - 10/2024",
                "description": "[SaaS](https://saas-dlp.up.railway.app/) - a foundational Software as a Service (SaaS) solution built with Django, featuring user authentication, subscription management, and custom commands.",
                "tech_stack": ["Python", "Django", "PostgreSQL"],
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
