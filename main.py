import os
import uvicorn
import sys
from google.adk.cli.cli_tools_click import get_fast_api_app

def run():
    # Ensure current directory is in path so tools.py can be imported by the agent
    sys.path.append(os.getcwd())
    
    port = int(os.environ.get("PORT", 8080))
    host = "0.0.0.0"
    
    print(f"Starting Nexus Intelligence Hub on {host}:{port}...")
    
    try:
        fastapi_app = get_fast_api_app(
            agents_dir="agents_registry",
            web=True,
            port=port,
            host=host
        )
        uvicorn.run(fastapi_app, host=host, port=port)
    except Exception as e:
        print(f"Failed to create/run FastAPI app: {e}")
        raise

if __name__ == "__main__":
    run()
