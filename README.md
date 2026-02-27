# Nexus Agent for Gemini Enterprise

A code-first AI agent built with the Google Agent Development Kit (ADK) to provide a natural language interface for the Nexus Research Computing system. This agent acts as a bridge, allowing users in the Gemini Enterprise workspace to securely query and manage the Nexus graph.

## 🌟 Key Features

### Multi-Agent Orchestration
The system employs a hierarchical Multi-Agent Topology for specialized processing:
- 🧠 **Manager Agent (Root):** Orchestrates the conversation, handles data entry (`log`, `ingest`, `tag`), and delegates tasks.
- 🕵️ **Intelligence Agent:** Specializes in situational awareness (`briefing`, `stats`, `ship_status`, `dossier`).
- 🔍 **Discovery Agent:** Specializes in finding entities and visualizing relationships (`search`, `tree`, `people_list`, `labs_list`, `grants_list`, `assets_list`).

### Secure Tool Layer
The agent utilizes a read-only adapter pattern, securely wrapping the local `nexus` CLI using Python `subprocess`. This ensures that all actions respect the underlying system's validation logic and maintains the integrity of the Nexus "System of Record."

## 🚀 Quick Start

### 1. Installation
This project uses `uv` for dependency management. Ensure you have Python 3.12+ installed.
```bash
uv sync
```

### 2. Local Testing (Web UI)
Run the agent locally to interact with it via a chat interface and test tool integrations:
```bash
uv run python main.py
```

### 3. Development Workflow (The Local Gauntlet)
Before submitting changes, run the Skywalker Gauntlet to ensure code quality:
```bash
uv run ruff check . --fix
uv run ruff format .
uv run mypy src
uv run pytest
```

## ☁️ Gemini Enterprise Deployment

To move from local development to the Gemini Enterprise workspace:

1. **Push to Container Registry:**
   ```bash
   gcloud builds submit --tag gcr.io/[PROJECT_ID]/nexus-agent .
   ```

2. **Deploy to Cloud Run (Agent Engine):**
   - Deploy as a service on port `8080`.
   - Set up OAuth 2.0 credentials in the GCP Console.
   - Ensure the service has access to the necessary Nexus database environment.

3. **Register in Workspace:**
   - Go to the [Gemini Enterprise Console](https://vertexaisearch.cloud.google.com/us/home/cid/74934e12-7960-462b-a548-72a31a17e03b).
   - Add an External Agent using your Cloud Run URL and OAuth Client ID.

## 🛠 Tech Stack
- **Language:** Python 3.12+
- **Framework:** Google ADK
- **Model:** `gemini-3-flash-preview`
- **CI/CD:** GitHub Actions (Skywalker Workflow)
