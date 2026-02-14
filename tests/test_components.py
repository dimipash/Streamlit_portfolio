"""
Tests for components.py module.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from components import is_valid_email, PortfolioComponents


class TestEmailValidation:
    """Test email validation function."""

    def test_valid_email_basic(self):
        """Test basic valid email format."""
        assert is_valid_email("test@example.com") == True
        assert is_valid_email("user@domain.org") == True
        assert is_valid_email("name@company.co.uk") == True

    def test_valid_email_with_special_chars(self):
        """Test valid emails with special characters."""
        assert is_valid_email("user.name@example.com") == True
        assert is_valid_email("user+tag@example.com") == True
        assert is_valid_email("user_name@example.com") == True
        assert is_valid_email("user-name@example.com") == True

    def test_invalid_email_no_at_symbol(self):
        """Test invalid emails without @ symbol."""
        assert is_valid_email("invalidemail.com") == False
        assert is_valid_email("user") == False

    def test_invalid_email_multiple_at_symbols(self):
        """Test invalid emails with multiple @ symbols."""
        assert is_valid_email("@@@@") == False
        assert is_valid_email("user@@example.com") == False
        assert is_valid_email("user@domain@com") == False

    def test_invalid_email_missing_parts(self):
        """Test invalid emails missing username or domain."""
        assert is_valid_email("@example.com") == False
        assert is_valid_email("user@") == False
        assert is_valid_email("@") == False

    def test_invalid_email_no_tld(self):
        """Test invalid emails without top-level domain."""
        assert is_valid_email("user@domain") == False
        assert is_valid_email("user@localhost") == False

    def test_invalid_email_spaces(self):
        """Test invalid emails with spaces."""
        assert is_valid_email("user @example.com") == False
        assert is_valid_email("user@ example.com") == False
        assert is_valid_email("user@example .com") == False

    def test_empty_or_none_email(self):
        """Test empty or None email."""
        assert is_valid_email("") == False
        with pytest.raises((TypeError, AttributeError)):
            is_valid_email(None)


class TestPortfolioComponents:
    """Test PortfolioComponents class."""

    def test_components_initialization(self):
        """Test PortfolioComponents can be initialized."""
        components = PortfolioComponents()
        assert components is not None
        assert hasattr(components, "config")

    @patch("components.Image.open")
    def test_load_image_success(self, mock_image_open):
        """Test successful image loading."""
        mock_image = Mock()
        mock_image_open.return_value = mock_image

        image = PortfolioComponents.load_image("test.jpg")

        mock_image_open.assert_called_once_with("test.jpg")
        assert image == mock_image

    @patch("components.Image.open")
    def test_load_image_failure(self, mock_image_open):
        """Test image loading failure handling."""
        mock_image_open.side_effect = FileNotFoundError("File not found")

        image = PortfolioComponents.load_image("nonexistent.jpg")

        assert image is None

    @patch("components.requests.get")
    def test_fetch_github_data_success(self, mock_get):
        """Test successful GitHub data fetching."""
        mock_response = Mock()
        mock_response.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        data = PortfolioComponents.fetch_github_data("testuser")

        assert isinstance(data, list)
        assert len(data) == 2
        mock_get.assert_called_once()

    @patch("components.requests.get")
    def test_fetch_github_data_with_token(self, mock_get):
        """Test GitHub data fetching with authentication token."""
        mock_response = Mock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        with patch.dict("os.environ", {"GITHUB_TOKEN": "test_token"}):
            PortfolioComponents.fetch_github_data("testuser")

            # Check that Authorization header was included
            call_kwargs = mock_get.call_args[1]
            assert "headers" in call_kwargs
            assert "Authorization" in call_kwargs["headers"]
            assert call_kwargs["headers"]["Authorization"] == "token test_token"

    @patch("components.requests.get")
    def test_fetch_github_data_failure(self, mock_get):
        """Test GitHub data fetching failure handling."""
        mock_get.side_effect = Exception("Network error")

        data = PortfolioComponents.fetch_github_data("testuser")

        assert data == {}

    def test_render_project_metrics_structure(self):
        """Test project metrics rendering with valid data."""
        metrics = {"code_coverage": 85, "commits": 120, "stars": 15, "status": "Active"}

        # This should not raise any exceptions
        try:
            PortfolioComponents.render_project_metrics("Test Project", metrics)
        except KeyError as e:
            pytest.fail(f"Missing required metric: {e}")
