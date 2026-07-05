"""Test configuration for Legal Research Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "legal-research-agent", "category": "Legal"}
