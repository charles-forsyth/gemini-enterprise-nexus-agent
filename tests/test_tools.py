# tests/test_tools.py

import subprocess
from unittest.mock import patch, MagicMock
from gemini_enterprise_nexus_agent.tools.interfaces import (
    run_nexus_command,
    nexus_search,
    nexus_dossier,
    nexus_tree,
    nexus_stats,
    nexus_briefing,
    nexus_ship_status,
    nexus_people_list,
    nexus_labs_list,
    nexus_grants_list,
    nexus_assets_list,
    nexus_log,
    nexus_ingest,
    nexus_people_tag,
)


@patch("subprocess.run")
def test_run_nexus_command_success(mock_run):
    mock_run.return_value = MagicMock(stdout="Success", stderr="", returncode=0)
    result = run_nexus_command(["test"])
    assert result == "Success"
    mock_run.assert_called_once_with(
        ["nexus", "test"], capture_output=True, text=True, check=True
    )


@patch("subprocess.run")
def test_run_nexus_command_failure(mock_run):
    mock_run.side_effect = subprocess.CalledProcessError(
        1, ["nexus", "test"], stderr="Error Output"
    )
    result = run_nexus_command(["test"])
    assert "Error Output" in result
    assert "Error executing nexus test" in result


def test_nexus_search():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Search Results"
        result = nexus_search("query")
        assert result == "Search Results"
        mock_run_cmd.assert_called_with(["search", "query"])


def test_nexus_dossier():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Dossier Content"
        result = nexus_dossier("netid")
        assert result == "Dossier Content"
        mock_run_cmd.assert_called_with(["dossier", "netid"])


def test_nexus_tree():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Tree Viz"
        result = nexus_tree("term")
        assert result == "Tree Viz"
        mock_run_cmd.assert_called_with(["tree", "term"])


def test_nexus_stats():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Stats"
        result = nexus_stats()
        assert result == "Stats"
        mock_run_cmd.assert_called_with(["stats"])


def test_nexus_briefing():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Briefing"
        result = nexus_briefing()
        assert result == "Briefing"
        mock_run_cmd.assert_called_with(["briefing"])


def test_nexus_ship_status():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Health"
        result = nexus_ship_status()
        assert result == "Health"
        mock_run_cmd.assert_called_with(["ship", "status"])


def test_nexus_people_list():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "People"
        result = nexus_people_list()
        assert result == "People"
        mock_run_cmd.assert_called_with(["people", "list"])


def test_nexus_labs_list():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Labs"
        result = nexus_labs_list()
        assert result == "Labs"
        mock_run_cmd.assert_called_with(["labs", "list"])


def test_nexus_grants_list():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Grants"
        result = nexus_grants_list()
        assert result == "Grants"
        mock_run_cmd.assert_called_with(["grants", "list"])


def test_nexus_assets_list():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Assets"
        result = nexus_assets_list()
        assert result == "Assets"
        mock_run_cmd.assert_called_with(["assets", "list"])


def test_nexus_log():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Log success"
        result = nexus_log("description", "res_netid", "sup_netid", "CHAT")
        assert result == "Log success"
        mock_run_cmd.assert_called_with(
            [
                "log",
                "description",
                "--researcher",
                "res_netid",
                "--staff",
                "sup_netid",
                "--type",
                "CHAT",
            ]
        )


def test_nexus_ingest():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Ingest success"
        result = nexus_ingest("raw text")
        assert result == "Ingest success"
        mock_run_cmd.assert_called_with(["ingest", "raw text"])


def test_nexus_people_tag():
    with patch(
        "gemini_enterprise_nexus_agent.tools.interfaces.run_nexus_command"
    ) as mock_run_cmd:
        mock_run_cmd.return_value = "Tag success"
        result = nexus_people_tag("netid", "#VIP")
        assert result == "Tag success"
        mock_run_cmd.assert_called_with(["people", "tag", "netid", "#VIP"])
