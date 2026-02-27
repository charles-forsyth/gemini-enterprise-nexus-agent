# Building AI Agents with Google ADK: Presentation Details

**Presenter:** Brandon Ayers (Associate Director, Integrations and Architecture)  
**Main Theme:** A Code-First Framework for AI Agents

---

## 1. Overview of Google ADK
The **Agent Development Kit (ADK)** is designed for developers who want full control. It allows defining agents, tools, and workflows directly in code without complex configuration files.

### Key Characteristics
*   **Modular & Extensible:** Supports multi-agent orchestration, custom tool integration, and flexible memory management.
*   **Model-Agnostic:** Works with Gemini, Claude, and other LLMs.
*   **Code-First:** Define everything in standard Python patterns (functions, classes).

---

## 2. Anatomy of an Agent
*   **The Model:** The "Brain" (e.g., Gemini 2.0 Flash) that processes instructions and decides which tools to call.
*   **Tools:** Python functions the agent can execute. ADK automatically generates the schema based on type hints and docstrings.
*   **Memory:** Manages conversation history and state.

---

## 3. Workflow Agents
For tasks that don't always need LLM reasoning, ADK provides deterministic workflow agents:
*   **SequentialAgent:** Strict, linear order (Fetch -> Process -> Save).
*   **ParallelAgent:** Runs multiple sub-agents simultaneously.
*   **LoopAgent:** Repeats tasks until a condition is met (e.g., polling APIs).

---

## 4. Multi-Agent Orchestration
*   **Hierarchical Delegation:** Complex systems can be composed by nesting agents.
*   **Manager Pattern:** A Parent agent treats Children (e.g., Researcher, Writer) like advanced tools, delegating tasks and receiving outputs.

---

## 5. Sessions, State, and Memory
*   **Session:** The container for a specific chat thread, holding chronological history (Events).
*   **State (`session.state`):** Key-value pairs for information the agent needs to recall within a thread (e.g., user flags).
*   **Memory:** Long-term knowledge/searchable archive for learning from past interactions.

---

## 6. Development and Setup
*   **Requirements:** Python 3.9+, virtual environment (uv or venv recommended).
*   **Installation:** Available via PIP.
*   **API Access:** Requires Google AI Studio API Key or GCP Google Account permissions.

### Testing Options
*   **CLI:** Test agents in the terminal.
*   **Web UI:** Local web server with a chat interface.
*   **Python SDK:** Programmatic execution using the `Runner` class.

---

## 7. Production and Deployment
*   **Cloud Run:** Framework is container-ready for deployment to Google Cloud Agent Engine.
*   **A2A Protocol:** Allows agents to communicate with other agents on different servers.
*   **Gemini Enterprise (GE):** Register an agent from Agent Engine in GE to interact with it directly within the GE interface.
*   **Authorization:** Supports OAuth authorization so the agent knows who the user is when called by GE.

---

## 8. Key Takeaways
1. **Native Code:** Build agents using standard Python patterns.
2. **Tool First:** Seamless integration of local functions and external APIs.
3. **Flexible Control:** Mix LLM-driven reasoning with deterministic workflows.
4. **Scalable:** From simple scripts to complex, multi-agent hierarchies.
