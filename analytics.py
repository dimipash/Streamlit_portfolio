"""
Analytics module for tracking portfolio interactions.
Implements caching and session state management for analytics data.
"""

from datetime import datetime
from functools import lru_cache

import streamlit as st


class Analytics:
    """Analytics tracking for portfolio interactions with caching."""

    @staticmethod
    def _get_analytics_state() -> dict:
        """
        Initialize or get analytics state.

        Returns:
            Dict: Current analytics state
        """
        if "analytics" not in st.session_state:
            st.session_state.analytics = {
                "project_views": {},
                "contact_submissions": 0,
                "last_interaction": None,
                "total_visits": 0,
            }
        return st.session_state.analytics

    @staticmethod
    @lru_cache(maxsize=100)
    def _get_cached_project_views(project_name: str) -> int:
        """
        Get cached view count for a project.

        Args:
            project_name (str): Name of the project

        Returns:
            int: Number of views for the project
        """
        analytics = Analytics._get_analytics_state()
        return analytics["project_views"].get(project_name, 0)

    @staticmethod
    def track_project_view(project_name: str) -> None:
        """
        Track when a project is viewed with caching.

        Args:
            project_name (str): Name of the viewed project
        """
        analytics = Analytics._get_analytics_state()

        if project_name not in analytics["project_views"]:
            analytics["project_views"][project_name] = 0
        analytics["project_views"][project_name] += 1

        # Clear cache for this project
        Analytics._get_cached_project_views.cache_clear()

    @staticmethod
    def track_contact_submission() -> None:
        """Track when contact form is submitted."""
        analytics = Analytics._get_analytics_state()
        analytics["contact_submissions"] += 1
        analytics["last_interaction"] = datetime.now().isoformat()

    @staticmethod
    def track_visit() -> None:
        """Track website visit."""
        analytics = Analytics._get_analytics_state()
        analytics["total_visits"] += 1

    @staticmethod
    def get_project_views(project_name: str) -> int:
        """
        Get number of views for a project.

        Args:
            project_name (str): Name of the project

        Returns:
            int: Number of views
        """
        return Analytics._get_cached_project_views(project_name)

    @staticmethod
    def get_total_contact_submissions() -> int:
        """
        Get total number of contact form submissions.

        Returns:
            int: Number of submissions
        """
        analytics = Analytics._get_analytics_state()
        return analytics["contact_submissions"]

    @staticmethod
    def get_last_interaction() -> str | None:
        """
        Get timestamp of last interaction.

        Returns:
            Optional[str]: ISO format timestamp of last interaction
        """
        analytics = Analytics._get_analytics_state()
        return analytics["last_interaction"]

    @staticmethod
    def get_total_visits() -> int:
        """
        Get total number of website visits.

        Returns:
            int: Number of visits
        """
        analytics = Analytics._get_analytics_state()
        return analytics["total_visits"]

    @staticmethod
    def get_analytics_summary() -> dict:
        """
        Get summary of all analytics data.

        Returns:
            Dict: Summary of analytics data
        """
        analytics = Analytics._get_analytics_state()
        return {
            "total_visits": analytics["total_visits"],
            "total_contact_submissions": analytics["contact_submissions"],
            "total_project_views": sum(analytics["project_views"].values()),
            "most_viewed_project": max(
                analytics["project_views"].items(), key=lambda x: x[1], default=("None", 0)
            ),
            "last_interaction": analytics["last_interaction"],
        }
