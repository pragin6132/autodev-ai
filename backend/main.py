from fastapi import FastAPI
from backend.app.agents.orchestrator.orchestrator import Orchestrator

app = FastAPI(
    title="AutoDev AI",
    description="Autonomous Multi-Agent Software Engineering Platform",
    version="1.0.0"
)

orchestrator = Orchestrator()


@app.get("/")
def root():
    return {
        "message": "Welcome to AutoDev AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/project/{request}")
def process_project(request: str):
    return orchestrator.process_request(request)