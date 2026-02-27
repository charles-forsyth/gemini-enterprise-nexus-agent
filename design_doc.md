# System Design Document: Nexus Agent for Gemini Enterprise

## 1. Architecture Overview
The Nexus Agent is an AI-driven natural language interface that bridges Gemini Enterprise and the local `nexus` CLI system of record. It is built using the Google Agent Development Kit (ADK) and follows a Multi-Agent Orchestration pattern.

### 1.1 Multi-Agent Topology
*   **Manager Agent (Root):** Orchestrates the overall conversation, handles direct actions (e.g., logging, ingesting), and delegates complex tasks.
*   **Intelligence Agent:** Specializes in situational awareness, providing briefings, stats, and relationship health reports.
*   **Discovery Agent:** Specializes in finding entities (people, labs, grants) and visualizing relationships.

### 1.2 Tool Layer
The tool layer acts as an adapter, securely wrapping the `nexus` CLI using Python's `subprocess`. All tools return `str` outputs representing the CLI results, ensuring the agent remains read-only and relies on the underlying CLI's validation logic.

## 2. Technical Stack
*   **Language:** Python 3.12+
*   **Package Manager:** `uv`
*   **Agent Framework:** `google-adk`
*   **LLM Model:** `gemini-3-flash-preview`
*   **Containerization:** Docker (for Cloud Run)

## 3. Toolchain & Development Workflow
We adhere to the **Skywalker Development Workflow**:
*   **Linter & Formatter:** `ruff`
*   **Type Checker:** `mypy`
*   **Testing:** `pytest`
*   **CI/CD:** GitHub Actions (`.github/workflows/ci.yml`)

### 3.1 The Local Gauntlet
Before pushing any code, developers MUST pass the following checks:
```bash
uv run ruff check . --fix
uv run ruff format .
uv run mypy src
uv run pytest
```

## 4. Deployment Strategy
*   **Target Environment:** Google Cloud Run (Agent Engine).
*   **Port:** The ADK application will listen on port `8080` to comply with Cloud Run constraints.
*   **Authentication:** The service will be configured to handle OAuth 2.0 handshakes originating from the Gemini Enterprise Workspace.
*   **Health Checks:** The ADK application MUST expose a health check endpoint (managed via ADK plugins if necessary) to ensure Cloud Run stability.

## 5. Security & Edge Case Mitigation
*   **Non-Destructive Operations:** Tools wrap existing CLI logic; no raw SQL or direct DB connections are made from the agent.
*   **Error Handling:** `subprocess.CalledProcessError` will be caught and formatted into agent-readable strings so the LLM can recover gracefully.
*   **Context Window Limits:** Large outputs (like full dossiers or large trees) may need to be truncated or paginated within the tool implementation if they exceed the context limits of the Gemini model.
