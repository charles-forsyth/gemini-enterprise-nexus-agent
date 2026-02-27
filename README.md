# Nexus Intelligence Agent

A code-first AI agent built with Google ADK to provide a natural language interface for the Nexus Research Computing system.

## 🚀 Quick Start

### 1. Installation
Ensure you have `uv` installed, then:
```bash
uv sync
```

### 2. Local Testing (Web UI)
Run the agent locally to interact with it via a chat interface:
```bash
uv run python main.py
```

### 3. Integrated Tools
The agent provides direct access to the following Nexus capabilities:
- **Search:** Find researchers and labs (`nexus_search`).
- **Dossier:** Pull deep context on a PI (`nexus_dossier`).
- **Intelligence:** Daily briefings and relationship health scans (`nexus_briefing`, `nexus_ship_status`).
- **Data Ingestion:** Log meetings and ingest notes (`nexus_log`, `nexus_ingest`).

## ☁️ Gemini Enterprise Deployment

1. **Push to Container Registry:**
   ```bash
   gcloud builds submit --tag gcr.io/[PROJECT_ID]/nexus-agent .
   ```

2. **Deploy to Cloud Run:**
   - Deploy as a service on port 8080.
   - Set up OAuth 2.0 credentials in GCP Console.

3. **Register in Workspace:**
   - Go to [Gemini Enterprise Console](https://vertexaisearch.cloud.google.com/us/home/cid/74934e12-7960-462b-a548-72a31a17e03b).
   - Add the External Agent using your Cloud Run URL and OAuth Client ID.

## 🛠 Tech Stack
- **Framework:** Google ADK (Python)
- **Model:** `gemini-3-flash-preview`
- **Infrastructure:** `nexus` CLI wrapper
