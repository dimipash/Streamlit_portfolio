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
            "Python AI Projects": {
                "code_coverage": 85,
                "commits": 150,
                "stars": 30,
                "complexity": "High",
                "status": "Active",
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
    def get_courses_data() -> List[tuple[str, str, str]]:
        """
        Returns list of course information.

        Returns:
            List[tuple[str, str, str]]: List of course tuples
        """
        return [
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
