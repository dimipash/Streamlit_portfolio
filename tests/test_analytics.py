"""
Tests for analytics.py module.
"""

from analytics import Analytics


class TestAnalytics:
    """Test Analytics class functionality."""

    def test_track_project_view(self, reset_session_state):
        """Test tracking a project view."""
        Analytics.track_project_view("Test Project")

        views = Analytics.get_project_views("Test Project")
        assert views >= 1

    def test_track_multiple_project_views(self, reset_session_state):
        """Test tracking multiple views of the same project."""
        project_name = "Test Project"

        Analytics.track_project_view(project_name)
        Analytics.track_project_view(project_name)
        Analytics.track_project_view(project_name)

        views = Analytics.get_project_views(project_name)
        assert views >= 3

    def test_track_different_projects(self, reset_session_state):
        """Test tracking views for different projects."""
        Analytics.track_project_view("Project A")
        Analytics.track_project_view("Project B")
        Analytics.track_project_view("Project A")

        assert Analytics.get_project_views("Project A") >= 2
        assert Analytics.get_project_views("Project B") >= 1

    def test_track_contact_submission(self, reset_session_state):
        """Test tracking contact form submissions."""
        initial_count = Analytics.get_total_contact_submissions()

        Analytics.track_contact_submission()

        new_count = Analytics.get_total_contact_submissions()
        assert new_count == initial_count + 1

    def test_track_visit(self, reset_session_state):
        """Test tracking website visits."""
        initial_visits = Analytics.get_total_visits()

        Analytics.track_visit()

        new_visits = Analytics.get_total_visits()
        assert new_visits == initial_visits + 1

    def test_get_last_interaction(self, reset_session_state):
        """Test getting last interaction timestamp."""
        initial_interaction = Analytics.get_last_interaction()

        Analytics.track_contact_submission()

        new_interaction = Analytics.get_last_interaction()
        assert new_interaction is not None
        assert new_interaction != initial_interaction

    def test_get_analytics_summary(self, reset_session_state):
        """Test getting analytics summary."""
        Analytics.track_visit()
        Analytics.track_project_view("Test Project")
        Analytics.track_contact_submission()

        summary = Analytics.get_analytics_summary()

        assert isinstance(summary, dict)
        assert "total_visits" in summary
        assert "total_contact_submissions" in summary
        assert "total_project_views" in summary
        assert "most_viewed_project" in summary
        assert "last_interaction" in summary

    def test_analytics_summary_structure(self, reset_session_state):
        """Test analytics summary has correct structure."""
        summary = Analytics.get_analytics_summary()

        assert isinstance(summary["total_visits"], int)
        assert isinstance(summary["total_contact_submissions"], int)
        assert isinstance(summary["total_project_views"], int)
        assert isinstance(summary["most_viewed_project"], tuple)

    def test_get_project_views_nonexistent(self, reset_session_state):
        """Test getting views for a project that hasn't been viewed."""
        views = Analytics.get_project_views("Nonexistent Project")
        assert views == 0

    def test_most_viewed_project(self, reset_session_state):
        """Test getting the most viewed project."""
        Analytics.track_project_view("Project A")
        Analytics.track_project_view("Project B")
        Analytics.track_project_view("Project B")
        Analytics.track_project_view("Project B")

        summary = Analytics.get_analytics_summary()
        most_viewed = summary["most_viewed_project"]

        assert most_viewed[0] == "Project B"
        assert most_viewed[1] >= 3
