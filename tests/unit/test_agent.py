"""Legal Research Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_search_case_law():
    """Test Search case law databases for relevant precedents."""
    tools = AgentTools()
    result = await tools.search_case_law(query="test", jurisdiction="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_precedent():
    """Test Analyze a legal precedent for applicability to current matter."""
    tools = AgentTools()
    result = await tools.analyze_precedent(case_citation="test", legal_issue="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_search_statutes():
    """Test Search statutes and regulations for applicable provisions."""
    tools = AgentTools()
    result = await tools.search_statutes(topic="test", jurisdiction="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_summarize_decision():
    """Test Summarize a court decision with key holdings and reasoning."""
    tools = AgentTools()
    result = await tools.summarize_decision(case_citation="test", focus_issues="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.legal_research_agent_agent import LegalResearchAgentAgent
    agent = LegalResearchAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
