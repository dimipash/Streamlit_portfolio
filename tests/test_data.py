"""
Tests for data.py module.
"""

from data import PortfolioData


class TestSkillsData:
    """Test skills data structure and content."""

    def test_skills_data_returns_dict(self):
        """Test that skills data returns a dictionary."""
        skills = PortfolioData.get_skills_data()
        assert isinstance(skills, dict)
        assert len(skills) > 0

    def test_skills_data_structure(self):
        """Test each skill has required fields with correct types."""
        skills = PortfolioData.get_skills_data()

        for skill_name, skill_data in skills.items():
            assert isinstance(skill_name, str)
            assert isinstance(skill_data, dict)

            assert "proficiency" in skill_data
            assert "category" in skill_data
            assert "experience_years" in skill_data

            assert isinstance(skill_data["proficiency"], (int, float))
            assert isinstance(skill_data["category"], str)
            assert isinstance(skill_data["experience_years"], (int, float))

    def test_skills_proficiency_range(self):
        """Test proficiency levels are between 0 and 100."""
        skills = PortfolioData.get_skills_data()

        for skill_name, skill_data in skills.items():
            proficiency = skill_data["proficiency"]
            assert 0 <= proficiency <= 100, f"{skill_name} proficiency out of range: {proficiency}"

    def test_skills_categories_valid(self):
        """Test all skills have valid categories."""
        skills = PortfolioData.get_skills_data()
        valid_categories = {
            "Languages",
            "Frameworks",
            "Frontend",
            "Backend",
            "Databases",
            "Tools",
        }

        categories = {skill["category"] for skill in skills.values()}
        assert categories.issubset(valid_categories)

    def test_experience_years_positive(self):
        """Test experience years are positive numbers."""
        skills = PortfolioData.get_skills_data()

        for skill_name, skill_data in skills.items():
            experience = skill_data["experience_years"]
            assert experience > 0, f"{skill_name} has invalid experience years: {experience}"


class TestProjectsData:
    """Test projects data structure and content."""

    def test_projects_data_returns_list(self):
        """Test that projects data returns a list."""
        projects = PortfolioData.get_projects_data()
        assert isinstance(projects, list)
        assert len(projects) > 0

    def test_projects_have_required_fields(self):
        """Test each project has required fields."""
        projects = PortfolioData.get_projects_data()
        required_fields = {"name", "date", "description"}

        for project in projects:
            assert isinstance(project, dict)
            for field in required_fields:
                assert field in project, f"Project missing required field: {field}"
                assert isinstance(project[field], str)
                assert len(project[field]) > 0

    def test_projects_tech_stack_valid(self):
        """Test tech stack is a list of strings when present."""
        projects = PortfolioData.get_projects_data()

        for project in projects:
            if "tech_stack" in project:
                assert isinstance(project["tech_stack"], list)
                assert len(project["tech_stack"]) > 0
                for tech in project["tech_stack"]:
                    assert isinstance(tech, str)
                    assert len(tech) > 0

    def test_projects_links_valid_format(self):
        """Test project links are valid URLs when present."""
        projects = PortfolioData.get_projects_data()

        for project in projects:
            if "github_link" in project:
                assert project["github_link"].startswith("http")
            if "live_demo" in project:
                assert project["live_demo"].startswith("http")


class TestProjectMetrics:
    """Test project metrics data."""

    def test_project_metrics_returns_dict(self):
        """Test that project metrics returns a dictionary."""
        metrics = PortfolioData.get_project_metrics()
        assert isinstance(metrics, dict)
        assert len(metrics) > 0

    def test_metrics_structure(self):
        """Test each metric has required fields."""
        metrics = PortfolioData.get_project_metrics()
        required_fields = {"code_coverage", "commits", "stars", "status"}

        for project_name, project_metrics in metrics.items():
            assert isinstance(project_name, str)
            for field in required_fields:
                assert field in project_metrics

    def test_metrics_values_valid(self):
        """Test metric values are in valid ranges."""
        metrics = PortfolioData.get_project_metrics()

        for _, project_metrics in metrics.items():
            assert 0 <= project_metrics["code_coverage"] <= 100
            assert project_metrics["commits"] > 0
            assert project_metrics["stars"] >= 0


class TestSoftSkills:
    """Test soft skills data."""

    def test_soft_skills_returns_list(self):
        """Test that soft skills returns a list."""
        soft_skills = PortfolioData.get_soft_skills()
        assert isinstance(soft_skills, list)
        assert len(soft_skills) > 0

    def test_soft_skills_are_strings(self):
        """Test all soft skills are non-empty strings."""
        soft_skills = PortfolioData.get_soft_skills()

        for skill in soft_skills:
            assert isinstance(skill, str)
            assert len(skill) > 0


class TestEmploymentHistory:
    """Test employment history data."""

    def test_employment_history_returns_list(self):
        """Test that employment history returns a list."""
        jobs = PortfolioData.get_employment_history()
        assert isinstance(jobs, list)
        assert len(jobs) > 0

    def test_jobs_have_required_fields(self):
        """Test each job has required fields."""
        jobs = PortfolioData.get_employment_history()
        required_fields = {"title", "company", "location", "date", "responsibilities"}

        for job in jobs:
            assert isinstance(job, dict)
            for field in required_fields:
                assert field in job, f"Job missing required field: {field}"

    def test_responsibilities_is_list(self):
        """Test responsibilities are lists of strings."""
        jobs = PortfolioData.get_employment_history()

        for job in jobs:
            assert isinstance(job["responsibilities"], list)
            assert len(job["responsibilities"]) > 0
            for responsibility in job["responsibilities"]:
                assert isinstance(responsibility, str)
                assert len(responsibility) > 0


class TestEducationData:
    """Test education data."""

    def test_education_data_returns_list(self):
        """Test that education data returns a list."""
        education = PortfolioData.get_education_data()
        assert isinstance(education, list)
        assert len(education) > 0

    def test_education_has_required_fields(self):
        """Test each education entry has required fields."""
        education = PortfolioData.get_education_data()
        required_fields = {"degree", "school", "date", "details"}

        for edu in education:
            assert isinstance(edu, dict)
            for field in required_fields:
                assert field in edu, f"Education entry missing required field: {field}"

    def test_education_details_is_list(self):
        """Test education details are lists of strings."""
        education = PortfolioData.get_education_data()

        for edu in education:
            assert isinstance(edu["details"], list)
            assert len(edu["details"]) > 0
            for detail in edu["details"]:
                assert isinstance(detail, str)
                assert len(detail) > 0
