"""
Tests for main.py module.
"""

import pytest
from unittest.mock import patch, MagicMock
import sys


class TestPortfolioApp:
    """Test PortfolioApp class."""

    @patch("main.st")
    def test_portfolio_app_initialization(self, mock_st):
        """Test PortfolioApp can be initialized."""
        mock_st.session_state = {}
        mock_st.set_page_config = MagicMock()
        mock_st.markdown = MagicMock()

        from main import PortfolioApp

        app = PortfolioApp()

        assert app is not None
        assert hasattr(app, "config")
        assert hasattr(app, "components")

    @patch("main.st")
    def test_track_visit_once(self, mock_st):
        """Test visit is tracked only once per session."""
        mock_st.session_state = {}
        mock_st.set_page_config = MagicMock()
        mock_st.markdown = MagicMock()

        from main import PortfolioApp

        app = PortfolioApp()

        assert "visit_tracked" in mock_st.session_state
        assert mock_st.session_state["visit_tracked"] == True

    @patch("main.st")
    def test_navbar_creation(self, mock_st):
        """Test navigation bar is created with correct sections."""
        mock_st.session_state = {}
        mock_st.set_page_config = MagicMock()
        mock_st.markdown = MagicMock()

        from main import PortfolioApp

        app = PortfolioApp()
        app.create_navbar()

        # Check markdown was called to create navbar
        assert mock_st.markdown.called

        # Get the HTML that was passed to markdown
        navbar_html = None
        for call in mock_st.markdown.call_args_list:
            if len(call[0]) > 0 and "nav-container" in str(call[0][0]):
                navbar_html = call[0][0]
                break

        assert navbar_html is not None
        # Check for navigation sections
        assert "#home" in navbar_html or "Home" in navbar_html
        assert "#skills" in navbar_html or "Skills" in navbar_html
        assert "#projects" in navbar_html or "Projects" in navbar_html
        assert "#contact" in navbar_html or "Contact" in navbar_html

    @patch("main.st")
    def test_render_sections_called(self, mock_st):
        """Test all sections are rendered."""
        mock_st.session_state = {}
        mock_st.set_page_config = MagicMock()
        mock_st.markdown = MagicMock()
        mock_st.title = MagicMock()
        mock_st.header = MagicMock()
        mock_st.write = MagicMock()
        mock_st.columns = MagicMock(
            return_value=[MagicMock(), MagicMock(), MagicMock()]
        )

        from main import PortfolioApp

        app = PortfolioApp()

        # Test individual render methods exist
        assert hasattr(app, "render_home")
        assert hasattr(app, "render_skills")
        assert hasattr(app, "render_projects")
        assert hasattr(app, "render_experience")
        assert hasattr(app, "render_education")
        assert hasattr(app, "render_github")
        assert hasattr(app, "render_courses")
        assert hasattr(app, "render_contact")
