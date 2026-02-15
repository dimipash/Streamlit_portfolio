"""
Pytest configuration and shared fixtures.
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


# Create a session state that supports both dict and attribute access
class MockSessionState(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key) from None

    def __setattr__(self, key, value):
        self[key] = value


def mock_cache_data(ttl=None):
    def decorator(func):
        func.clear = MagicMock()
        return func

    return decorator


# Global mock for streamlit to ensure it's used during import time
mock_st = MagicMock()
mock_st.session_state = MockSessionState()
mock_st.cache_data = mock_cache_data
mock_st.empty = MagicMock()  # For loading spinner

# Patch sys.modules immediately so that any subsequent imports use the mock
sys.modules["streamlit"] = mock_st


@pytest.fixture(autouse=True)
def reset_streamlit_mock():
    """Reset the global mock state before each test."""
    mock_st.reset_mock()
    mock_st.session_state.clear()

    # Re-apply the mock helpers that might have been cleared
    mock_st.cache_data = mock_cache_data

    # Ensure session_state is still our custom class
    if not isinstance(mock_st.session_state, MockSessionState):
        mock_st.session_state = MockSessionState()

    yield mock_st


@pytest.fixture
def reset_session_state(reset_streamlit_mock):
    """Reset Streamlit session state between tests."""
    mock_st.session_state.clear()
    yield
    mock_st.session_state.clear()
