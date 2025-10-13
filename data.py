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
            "Google News Clone": {
                "code_coverage": 80,
                "commits": 80,
                "stars": 10,
                "complexity": "Medium",
                "status": "Completed",
            },
            "AI Web Scraper": {
                "code_coverage": 85,
                "commits": 60,
                "stars": 20,
                "complexity": "Medium",
                "status": "Completed",
            },
            "Llama3.1 Flask Chatbot": {
                "code_coverage": 90,
                "commits": 40,
                "stars": 30,
                "complexity": "Medium",
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
                "date": "09/2024 - 10/2024",
                "description": "A comprehensive Django-based online shopping platform with features like custom user models, product and category management, shopping cart, order processing, inventory control, user account management, and PayPal integration.",
                "tech_stack": [
                    "Python",
                    "Django",
                    "PostgreSQL",
                    "JavaScript",
                    "Bootstrap",
                ],
                "live_demo": "https://online-shop-django-project-production.up.railway.app/",
                "github_link": "https://github.com/dimipash/ONLINE_SHOP_DJANGO_PROJECT",
            },
            {
                "name": "SaaS Django Project",
                "date": "05/2025 - 05/2025",
                "description": "A foundational Software as a Service (SaaS) solution built with Django, featuring user authentication, subscription management, and custom commands.",
                "tech_stack": ["Python", "Django", "PostgreSQL", "Docker"],
                "live_demo": "https://saas-dlp.up.railway.app/",
                "github_link": "https://github.com/dimipash/SAAS",
            },
            {
                "name": "Google News Clone",
                "date": "05/2025 - 05/2025",
                "description": "A clone of Google News built with React, utilizing Firebase for backend services and Tailwind CSS for styling.",
                "tech_stack": ["React", "Firebase", "Tailwind CSS", "TypeScript"],
                "github_link": "https://github.com/dimipash/GOOGLE-NEWS-CLONE-REACTJS",
            },
            {
                "name": "AI Web Scraper",
                "date": "08/2024 - 08/2024",
                "description": "An intelligent web scraper that uses AI to extract data from websites. Built with Streamlit and Selenium.",
                "tech_stack": ["Python", "Streamlit", "Selenium", "LLM"],
                "github_link": "https://github.com/dimipash/AI_WEB_SCRAPER",
            },
            {
                "name": "Llama3.1 Flask Chatbot",
                "date": "08/2024 - 08/2024",
                "description": "A chatbot powered by Llama3.1, built with Flask. The chatbot can engage in natural conversations and answer user queries.",
                "tech_stack": ["Python", "Flask", "Llama3.1"],
                "github_link": "https://github.com/dimipash/LLAMA3.1_FLASK_CHATBOT",
            },
        ]