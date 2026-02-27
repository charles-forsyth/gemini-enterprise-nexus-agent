# Release Notes: v0.1.0 (Initial Release)

**Date:** February 26, 2026
**Mission:** Deploy Nexus Agent to Gemini Enterprise Workspace

## Overview
This initial release establishes the **Nexus Intelligence Hub**, a code-first AI agent built with the Google Agent Development Kit (ADK). This agent bridges the gap between the Gemini Enterprise workspace and the local `nexus` CLI, allowing Research Computing staff to manage their ecosystem through natural language.

## 🚀 Features

### Multi-Agent Architecture
Implemented a hierarchical, multi-agent orchestration pattern to handle complex user intents efficiently:
*   **Manager Agent:** Acts as the central command, routing requests to specialists and handling direct data modifications (logging, ingesting, tagging).
*   **Intelligence Agent:** A dedicated specialist for providing daily briefings, departmental stats, researcher dossiers, and relationship health scans.
*   **Discovery Agent:** A dedicated specialist for searching the Nexus graph, visualizing relationship trees, and listing entities (people, labs, grants, assets).

### Secure Tool Layer
*   Developed a secure adapter layer that wraps the `nexus` CLI using Python's `subprocess`.
*   Ensures that all LLM-driven actions are validated by the underlying Nexus CLI "System of Record."
*   Integrated 14 distinct Nexus commands as ADK Tools.

### LLM Integration
*   Configured to exclusively use the `gemini-3-flash-preview` model for optimal performance and reasoning capabilities within the Vertex AI ecosystem.

## 🛠 Engineering & Infrastructure
*   **Skywalker Workflow:** Adopted the rigorous Skywalker Development Workflow, utilizing `uv` for fast dependency management, `ruff` for linting/formatting, `mypy` for static typing, and `pytest` for testing.
*   **CI/CD:** Established GitHub Actions (`ci.yml`) to enforce the "Local Gauntlet" on all pull requests and merges.
*   **Containerization:** Provided a `Dockerfile` optimized for deploying the ADK application to Google Cloud Run (Agent Engine).
*   **100% Test Coverage:** Delivered comprehensive unit tests (`tests/test_tools.py` and `tests/test_agents.py`) verifying tool execution and agent configuration.
