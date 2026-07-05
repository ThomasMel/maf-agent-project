from autogen_ext.teams.magentic_one import MagenticOne

from .config import get_llm_client


async def run_agentic_team(task_prompt: str):
    """Initializes Microsoft Agent Framework's Magentic-One team to solve a task."""
    model_client = get_llm_client()

    # In MAF, the MagenticOne class natively spawns the whole team out-of-the-box
    team = MagenticOne(client=model_client)

    results = []
    # Stream the message turns asynchronously across the team runtime
    async for message in team.run_stream(task=task_prompt):
        results.append(message)

    return results
