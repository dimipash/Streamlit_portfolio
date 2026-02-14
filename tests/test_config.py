"""
Tests for config.py module.
"""

import pytest
from unittest.mock import patch, MagicMock
from config import Config


class TestConfig:
    """Test Config class."""

    def test_config_constants_exist(self):
        """Test that Config class has required constants."""
        assert hasattr(Config, "PROFILE_IMAGE")
        assert hasattr(Config, "RESUME_PATH")
        assert hasattr(Config, "PAGE_TITLE")
        assert hasattr(Config, "GITHUB_USERNAME")
        assert hasattr(Config, "CONTACT_EMAIL")
        assert hasattr(Config, "EMAIL_RATE_LIMIT")

    def test_config_constant_types(self):
        """Test that Config constants have correct types."""
        assert isinstance(Config.PROFILE_IMAGE, str)
        assert isinstance(Config.RESUME_PATH, str)
        assert isinstance(Config.PAGE_TITLE, str)
        assert isinstance(Config.GITHUB_USERNAME, str)
        assert isinstance(Config.CONTACT_EMAIL, str)
        assert isinstance(Config.EMAIL_RATE_LIMIT, int)

    def test_config_constant_values(self):
        """Test that Config constants have valid values."""
        assert len(Config.PROFILE_IMAGE) > 0
        assert len(Config.RESUME_PATH) > 0
        assert len(Config.PAGE_TITLE) > 0
        assert len(Config.GITHUB_USERNAME) > 0
        assert "@" in Config.CONTACT_EMAIL
        assert Config.EMAIL_RATE_LIMIT > 0

    @patch.dict(
        "os.environ",
        {
            "EMAIL_HOST": "smtp.gmail.com",
            "EMAIL_PORT": "587",
            "EMAIL_USERNAME": "test@example.com",
            "EMAIL_PASSWORD": "password123",
        },
    )
    def test_load_email_config_success(self):
        """Test successful email configuration loading."""
        config = Config.load_email_config()

        assert isinstance(config, dict)
        assert config["host"] == "smtp.gmail.com"
        assert config["port"] == 587
        assert config["username"] == "test@example.com"
        assert config["password"] == "password123"

    @patch.dict("os.environ", {}, clear=True)
    def test_load_email_config_missing_vars(self):
        """Test email configuration with missing environment variables."""
        with pytest.raises(ValueError) as exc_info:
            Config.load_email_config()

        assert "Missing required environment variables" in str(exc_info.value)

    @patch.dict(
        "os.environ",
        {
            "EMAIL_HOST": "smtp.gmail.com",
            "EMAIL_PORT": "587",
            "EMAIL_USERNAME": "test@example.com",
            # EMAIL_PASSWORD missing
        },
    )
    def test_load_email_config_partial_vars(self):
        """Test email configuration with partial environment variables."""
        with pytest.raises(ValueError) as exc_info:
            Config.load_email_config()

        assert "EMAIL_PASSWORD" in str(exc_info.value)

    def test_email_rate_limit_reasonable(self):
        """Test that email rate limit is set to a reasonable value."""
        assert 1 <= Config.EMAIL_RATE_LIMIT <= 100

    @patch("config.smtplib.SMTP")
    @patch.dict(
        "os.environ",
        {
            "EMAIL_HOST": "smtp.gmail.com",
            "EMAIL_PORT": "587",
            "EMAIL_USERNAME": "test@example.com",
            "EMAIL_PASSWORD": "password123",
        },
    )
    def test_send_email_success(self, mock_smtp):
        """Test successful email sending."""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        # Mock session state
        import streamlit as st

        st.session_state.clear()
        st.session_state.current_hour = 10
        st.session_state.email_count = 0

        result = Config.send_email(
            subject="Test Subject", body="Test Body", from_email="sender@example.com"
        )

        assert result == True
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once()
        mock_server.send_message.assert_called_once()

    @patch.dict(
        "os.environ",
        {
            "EMAIL_HOST": "smtp.gmail.com",
            "EMAIL_PORT": "587",
            "EMAIL_USERNAME": "test@example.com",
            "EMAIL_PASSWORD": "password123",
        },
    )
    def test_send_email_rate_limit(self):
        """Test email rate limiting."""
        import streamlit as st

        st.session_state.clear()
        st.session_state.current_hour = 10
        st.session_state.email_count = Config.EMAIL_RATE_LIMIT

        result = Config.send_email(
            subject="Test Subject", body="Test Body", from_email="sender@example.com"
        )

        assert result == False
