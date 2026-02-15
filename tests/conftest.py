"""
Pytest configuration and shared fixtures.
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(autouse=True)
def mock_streamlit():
    """Mock Streamlit for all tests to avoid UI dependencies."""
    mock_st = MagicMock()

    # Create a session state that supports both dict and attribute access
    class MockSessionState(dict):
        def __getattr__(self, key):
            try:
                return self[key]
            except KeyError:
                raise AttributeError(key)

        def __setattr__(self, key, value):
            self[key] = value

    mock_st.session_state = MockSessionState()
    mock_st.cache_data = lambda ttl=None: lambda func: func
    sys.modules["streamlit"] = mock_st
    yield mock_st
    # Cleanup
    if "streamlit" in sys.modules:
        del sys.modules["streamlit"]


@pytest.fixture
def reset_session_state(mock_streamlit):
    """Reset Streamlit session state between tests."""
    mock_streamlit.session_state.clear()
    yield
    mock_streamlit.session_state.clear()
