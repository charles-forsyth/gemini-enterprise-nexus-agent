# Project Mission: Nexus Agent for Gemini Enterprise

## Vision
To provide a seamless, AI-driven natural language interface for the **Nexus Research Computing System** directly within the **Gemini Enterprise (GE)** workspace. This enables UCR staff to manage researchers, labs, and relationship health through intuitive conversation while maintaining the integrity of the Nexus "System of Record."

## User Stories
1. **As a Research Computing Staff member**, I want to interact with Nexus through the Gemini Enterprise chat interface so that I can manage my ecosystem without context-switching.
2. **As the "Captain"**, I want the agent to provide a daily intelligence briefing so that I am always aware of my team's priorities and relationship health.
3. **As a Technical Lead**, I want the agent to handle identity through OAuth 2.0 so that all interactions are secure and audited correctly.

## Acceptance Criteria (AC)

### 1. Functional Requirements
*   **AC 1.1:** The agent MUST wrap and execute the following `nexus` CLI commands:
    *   `search`, `dossier`, `tree`, `stats`, `briefing`, `tasks list`, `ship status`, `log`, and `ingest`.
*   **AC 1.2:** The agent MUST use the `gemini-3-flash-preview` model for all LLM-driven reasoning.
*   **AC 1.3:** The agent MUST implement the Google ADK (Agent Development Kit) framework correctly, including the `App` and `Agent` classes.
*   **AC 1.4:** The agent MUST use the Multi-Agent Orchestration pattern (Manager -> Intelligence/Discovery Specialists) as defined in the plan.

### 2. Deployment & Integration Requirements
*   **AC 2.1:** The agent MUST be containerized using a `Dockerfile` and be deployable to **Google Cloud Run**.
*   **AC 2.2:** The agent MUST implement the **OAuth 2.0** handshake required for integration with Gemini Enterprise.
*   **AC 2.3:** The agent MUST be registered and functional within the target Gemini Enterprise workspace: [GE Console](https://vertexaisearch.cloud.google.com/us/home/cid/74934e12-7960-462b-a548-72a31a17e03b).
*   **AC 2.4:** The agent MUST listen on port `8080` and pass Google Cloud Run health checks.

### 3. Security & Integrity Requirements
*   **AC 3.1:** All tool executions MUST be non-destructive to the Nexus database, relying on established CLI validation logic.
*   **AC 3.2:** Sensitive credentials (like OAuth secrets) MUST NOT be hardcoded and MUST be managed via environment variables or Secret Manager.

## Edge Cases
*   **Large CLI Output:** How the agent handles very long search results or dossier data that exceeds context limits.
*   **CLI Failures:** Graceful handling of `subprocess.CalledProcessError` (e.g., when the database is locked or a NetID is not found).
*   **OAuth Lifecycle:** Handling token refresh and invalid session states within the GE environment.
*   **Concurrency:** Managing simultaneous requests from multiple users in the GE workspace.
