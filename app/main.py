from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agents import run_agentic_team

app = FastAPI(
    title="maf-agent-project",
    description="Microsoft Agentic Framework Orchestration Layer",
    version="1.0.0",
)


class TaskRequest(BaseModel):
    task: str


@app.post("/api/v1/orchestrate")
async def orchestrate_task(request: TaskRequest):
    try:
        # Hands the incoming task directly to the Magentic-One multi-agent engine
        conversation_history = await run_agentic_team(request.task)
        return {
            "status": "success",
            "task": request.task,
            "turns_executed": len(conversation_history),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
