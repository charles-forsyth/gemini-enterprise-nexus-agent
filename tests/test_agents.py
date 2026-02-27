# tests/test_agents.py

from gemini_enterprise_nexus_agent.agents.interfaces import (
    intelligence_agent,
    discovery_agent,
    manager_agent,
    app,
)


def test_intelligence_agent_config():
    assert intelligence_agent.name == "nexus_intel"
    assert "nexus_briefing" in [t.__name__ for t in intelligence_agent.tools]
    assert intelligence_agent.model == "gemini-3-flash-preview"


def test_discovery_agent_config():
    assert discovery_agent.name == "nexus_discovery"
    assert "nexus_search" in [t.__name__ for t in discovery_agent.tools]
    assert discovery_agent.model == "gemini-3-flash-preview"


def test_manager_agent_config():
    assert manager_agent.name == "nexus_manager"
    assert "nexus_log" in [t.__name__ for t in manager_agent.tools]
    assert "nexus_intel" in [a.name for a in manager_agent.sub_agents]
    assert "nexus_discovery" in [a.name for a in manager_agent.sub_agents]
    assert manager_agent.model == "gemini-3-flash-preview"


def test_app_config():
    assert app.name == "nexus_intelligence_hub"
    assert app.root_agent == manager_agent
