import subprocess
from typing import List


def run_nexus_command(args: List[str]) -> str:
    """Helper to run a nexus command and return output."""
    try:
        cmd = ["nexus"] + args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing nexus {args[0]}: {e.stderr or e.stdout}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


def nexus_search(term: str) -> str:
    """Search for entities (researchers, labs, etc.) in the Nexus graph."""
    return run_nexus_command(["search", term])


def nexus_dossier(netid: str) -> str:
    """Get a detailed dossier for a specific researcher by their NetID."""
    return run_nexus_command(["dossier", netid])


def nexus_tree(term: str) -> str:
    """Visualize the graph neighborhood of an entity (e.g., a person or lab)."""
    return run_nexus_command(["tree", term])


def nexus_stats() -> str:
    """Show the Departmental Scoreboard and KPIs for Research Computing."""
    return run_nexus_command(["stats"])


def nexus_briefing() -> str:
    """Generates the Daily Intelligence Briefing."""
    return run_nexus_command(["briefing"])


def nexus_ship_status() -> str:
    """Scan for key relationships that have gone cold (Relationship Health)."""
    return run_nexus_command(["ship", "status"])


def nexus_people_list() -> str:
    """List all researchers in the system."""
    return run_nexus_command(["people", "list"])


def nexus_labs_list() -> str:
    """List all research labs."""
    return run_nexus_command(["labs", "list"])


def nexus_grants_list() -> str:
    """List all grants and funding records."""
    return run_nexus_command(["grants", "list"])


def nexus_assets_list() -> str:
    """List local hardware assets."""
    return run_nexus_command(["assets", "list"])


def nexus_log(
    description: str,
    researcher_netid: str,
    support_netid: str,
    type_code: str = "MEETING",
) -> str:
    """Log a new interaction between a researcher and support staff."""
    return run_nexus_command(
        [
            "log",
            description,
            "--researcher",
            researcher_netid,
            "--staff",
            support_netid,
            "--type",
            type_code,
        ]
    )


def nexus_ingest(text: str) -> str:
    """Ingest raw notes or text into the Nexus knowledge graph."""
    return run_nexus_command(["ingest", text])


def nexus_people_tag(netid: str, tag: str) -> str:
    """Add a tag (e.g. #VIP) to a researcher."""
    return run_nexus_command(["people", "tag", netid, tag])
