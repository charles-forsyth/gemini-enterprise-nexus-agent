# src/gemini_enterprise_nexus_agent/tools/interfaces.pyi

from typing import List

def run_nexus_command(args: List[str]) -> str:
    """Helper to run a nexus command and return output."""
    ...

def nexus_search(term: str) -> str:
    """Search for entities (researchers, labs, etc.) in the Nexus graph."""
    ...

def nexus_dossier(netid: str) -> str:
    """Get a detailed dossier for a specific researcher by their NetID."""
    ...

def nexus_tree(term: str) -> str:
    """Visualize the graph neighborhood of an entity (e.g., a person or lab)."""
    ...

def nexus_stats() -> str:
    """Show the Departmental Scoreboard and KPIs for Research Computing."""
    ...

def nexus_briefing() -> str:
    """Generates the Daily Intelligence Briefing."""
    ...

def nexus_ship_status() -> str:
    """Scan for key relationships that have gone cold (Relationship Health)."""
    ...

def nexus_people_list() -> str:
    """List all researchers in the system."""
    ...

def nexus_labs_list() -> str:
    """List all research labs."""
    ...

def nexus_grants_list() -> str:
    """List all grants and funding records."""
    ...

def nexus_assets_list() -> str:
    """List local hardware assets."""
    ...

def nexus_log(
    description: str,
    researcher_netid: str,
    support_netid: str,
    type_code: str = "MEETING",
) -> str:
    """Log a new interaction between a researcher and support staff."""
    ...

def nexus_ingest(text: str) -> str:
    """Ingest raw notes or text into the Nexus knowledge graph."""
    ...

def nexus_people_tag(netid: str, tag: str) -> str:
    """Add a tag (e.g. #VIP) to a researcher."""
    ...
