SkillsDict = dict[str, dict[str, int | str | float]]
ProjectDict = dict[str, str]
JobDict = dict[str, str | list[str]]
MetricsDict = dict[str, dict[str, int | float | str]]


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
    def get_soft_skills() -> list[str]:
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
    def get_projects_data() -> list[ProjectDict]:
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
                "live_demo": "https://dimipi.pythonanywhere.com/",
                "github_link": "https://github.com/dimipash/ONLINE_SHOP_DJANGO_PROJECT",
            },
            {
                "name": "SaaS Django Project",
                "date": "05/2025 - 05/2025",
                "description": "A foundational Software as a Service (SaaS) solution built with Django, featuring user authentication, subscription management, and custom commands.",
                "tech_stack": ["Python", "Django", "PostgreSQL", "Docker"],                
                "github_link": "https://github.com/dimipash/SAAS",
            },
            {
                "name": "Python AI Projects",
                "date": "2024 - Present",
                "description": "A collection of small to medium-sized projects focused on exploring various applications of Artificial Intelligence (AI) using Python and related technologies. Projects include AI research agents, voice assistants, coding mentors, web scrapers, and more.",
                "tech_stack": [
                    "Python",
                    "LangChain",
                    "Flask",
                    "Streamlit",
                    "FastAPI",
                    "MongoDB",
                ],
                "github_link": "https://github.com/dimipash/AI-PYTHON-PROJECTS",
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

    @staticmethod
    def get_employment_history() -> list[JobDict]:
        """
        Returns employment history data.

        Returns:
            List[JobDict]: List of job dictionaries
        """
        return [
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

    @staticmethod
    def get_education_data() -> list[dict[str, str | list[str]]]:
        """
        Returns education data.

        Returns:
            List[Dict]: List of education dictionaries
        """
        return [
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
