from google.adk.agents import Agent
from tools import (
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

# --- Intelligence Agent ---
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

# --- Discovery Agent ---
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

# --- Root Manager Agent ---
root_agent = Agent(
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
