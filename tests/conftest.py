"""
Pytest configuration and shared fixtures.
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


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


mock_st = MagicMock()
mock_st.session_state = MockSessionState()
mock_st.cache_data = mock_cache_data
mock_st.empty = MagicMock()

sys.modules["streamlit"] = mock_st


@pytest.fixture(autouse=True)
def reset_streamlit_mock():
    """Reset the global mock state before each test."""
    mock_st.reset_mock()
    mock_st.session_state.clear()

    mock_st.cache_data = mock_cache_data

    if not isinstance(mock_st.session_state, MockSessionState):
        mock_st.session_state = MockSessionState()

    yield mock_st


@pytest.fixture
def reset_session_state(reset_streamlit_mock):
    """Reset Streamlit session state between tests."""
    mock_st.session_state.clear()
    yield
    mock_st.session_state.clear()
