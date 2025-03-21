"""
Configuration module for the portfolio website.
Contains settings and environment configurations.
"""

import os
from typing import Dict, Union
from dataclasses import dataclass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import streamlit as st
from dotenv import load_dotenv


@dataclass
class Config:
    """Configuration settings for the portfolio website."""

    PROFILE_IMAGE: str = "photo.jpeg"
    RESUME_PATH: str = "resume.pdf"
    PAGE_TITLE: str = "Dimitar Pashev - Portfolio"
    GITHUB_USERNAME: str = "dimipash"
    CONTACT_EMAIL: str = "dim.pashev@gmail.com"
    EMAIL_RATE_LIMIT: int = 5  # Maximum emails per hour

    @staticmethod
    def load_email_config() -> Dict[str, Union[str, int]]:
        """
        Load email configuration from environment variables.

        Returns:
            Dict[str, Union[str, int]]: Email configuration settings

        Raises:
            ValueError: If required environment variables are missing
        """
        load_dotenv()
        required_vars = ["EMAIL_HOST", "EMAIL_PORT", "EMAIL_USERNAME", "EMAIL_PASSWORD"]
        
        config = {
            "host": os.getenv("EMAIL_HOST", "smtp.gmail.com"),
            "port": int(os.getenv("EMAIL_PORT", "587")),
            "username": os.getenv("EMAIL_USERNAME"),
            "password": os.getenv("EMAIL_PASSWORD"),
        }

        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

        return config

    @staticmethod
    def send_email(subject: str, body: str, from_email: str) -> bool:
        """
        Send email using SMTP configuration with rate limiting.

        Args:
            subject (str): Email subject
            body (str): Email body content
            from_email (str): Sender's email address

        Returns:
            bool: True if email sent successfully, False otherwise

        Raises:
            Exception: If email sending fails
        """
        # Rate limiting check
        hour = st.session_state.get('current_hour', 0)
        current_hour = datetime.now().hour
        
        if hour != current_hour:
            st.session_state.current_hour = current_hour
            st.session_state.email_count = 0
        
        if st.session_state.get('email_count', 0) >= Config.EMAIL_RATE_LIMIT:
            st.error("Email rate limit exceeded. Please try again later.")
            return False

        try:
            email_config = Config.load_email_config()

            msg = MIMEMultipart()
            msg["From"] = from_email
            msg["To"] = Config.CONTACT_EMAIL
            msg["Subject"] = f"Portfolio Contact: {subject}"

            full_body = f"From: {from_email}\n\n{body}"
            msg.attach(MIMEText(full_body, "plain"))

            with smtplib.SMTP(email_config["host"], email_config["port"]) as server:
                server.starttls()
                server.login(email_config["username"], email_config["password"])
                server.send_message(msg)

            # Increment email counter
            st.session_state.email_count = st.session_state.get('email_count', 0) + 1
            return True

        except Exception as e:
            st.error(f"Failed to send email: {str(e)}")
            return False
