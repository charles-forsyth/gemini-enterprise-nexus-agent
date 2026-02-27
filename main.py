import subprocess
from google.adk import Agent
from google.adk.apps import App
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.plugins.logging_plugin import LoggingPlugin


def run_nexus_command(args: list[str]) -> str:
    """Helper to run a nexus command and return output."""
    try:
        cmd = ["nexus"] + args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing nexus {args[0]}: {e.stderr or e.stdout}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


# --- Discovery Tools ---
def nexus_search(term: str) -> str:
    """Search for entities (researchers, labs, etc.) in the Nexus graph."""
    return run_nexus_command(["search", term])


def nexus_dossier(netid: str) -> str:
    """Get a detailed dossier for a specific researcher by their NetID."""
    return run_nexus_command(["dossier", netid])


def nexus_tree(term: str) -> str:
    """Visualize the graph neighborhood of an entity (e.g., a person or lab)."""
    return run_nexus_command(["tree", term])


# --- Intelligence Tools ---
def nexus_stats() -> str:
    """Show the Departmental Scoreboard and KPIs for Research Computing."""
    return run_nexus_command(["stats"])


def nexus_briefing() -> str:
    """Generates the Daily Intelligence Briefing."""
    return run_nexus_command(["briefing"])


def nexus_ship_status() -> str:
    """Scan for key relationships that have gone cold (Relationship Health)."""
    return run_nexus_command(["ship", "status"])


# --- List Tools ---
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


# --- Action Tools ---
def nexus_log(
    description: str,
    researcher_netid: str,
    support_netid: str,
    type_code: str = "MEETING",
) -> str:
    """
    Log a new interaction between a researcher and support staff.
    type_code options: MEETING, EMAIL, CHAT, TICKET, GRANT_SUPPORT.
    """
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


# --- Define the core Intelligence Agent ---
intelligence_agent = Agent(
    name="nexus_intel",
    model="gemini-3-flash-preview",
    description="The Nexus Intelligence specialist.",
    instruction="""
    You are the Nexus Intelligence specialist. You provide briefings, relationship health reports, 
    and detailed dossiers. 
    
    Guidelines:
    1. Use 'nexus_briefing' for daily summaries.
    2. Use 'nexus_ship_status' for relationship health.
    3. Use 'nexus_dossier' for deep dives on researchers.
    4. Address the user as 'Captain'.
    """,
    tools=[nexus_briefing, nexus_ship_status, nexus_dossier, nexus_stats],
)

# --- Define the core Discovery Agent ---
discovery_agent = Agent(
    name="nexus_discovery",
    model="gemini-3-flash-preview",
    description="The Nexus Discovery specialist.",
    instruction="""
    You are the Nexus Discovery specialist. You find people, labs, and assets.
    
    Guidelines:
    1. Use 'nexus_search' to find NetIDs if you only have a name.
    2. Use 'nexus_tree' to visualize relationships.
    3. Use the list tools to browse entities.
    4. Address the user as 'Captain'.
    """,
    tools=[
        nexus_search,
        nexus_tree,
        nexus_people_list,
        nexus_labs_list,
        nexus_grants_list,
        nexus_assets_list,
    ],
)

# --- Define the Manager Agent (Root) ---
manager_agent = Agent(
    name="nexus_manager",
    model="gemini-3-flash-preview",
    description="The Nexus Central Commander.",
    instruction="""
    You are the Nexus Central Commander. You orchestrate the specialized intelligence and discovery agents.
    
    Your goal is to help UCR Research Computing staff manage the ecosystem.
    
    Guidelines:
    1. Delegate complex research/analysis to 'nexus_intel'.
    2. Delegate search and discovery tasks to 'nexus_discovery'.
    3. Handle data entry (logging/ingesting) yourself.
    4. Always refer to the user as 'Captain'.
    """,
    tools=[nexus_log, nexus_ingest, nexus_people_tag],
    sub_agents=[intelligence_agent, discovery_agent],
)

# Wrap in an App
app = App(
    name="nexus_intelligence_hub", root_agent=manager_agent, plugins=[LoggingPlugin()]
)


if __name__ == "__main__":
    session_service = InMemorySessionService()
    runner = Runner(app=app, session_service=session_service)
    runner.run_webui()
