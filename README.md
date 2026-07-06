# maf-agent-project

A lightweight FastAPI service that orchestrates Microsoft Agent Framework (MAF) Magentic-One multi-agent workflows using OpenAI-compatible LLM clients.

## Key features

- Exposes a single REST endpoint to submit tasks for agentic orchestration
- Uses `autogen-ext[magentic-one]` and `autogen-core` to launch a Magentic-One team
- Supports containerized deployment with Docker Compose
- Uses environment-based configuration for OpenAI-compatible API access

## Project structure

- `app/main.py` - FastAPI application and request handler
- `app/agents.py` - MAF team runner using `MagenticOne`
- `app/config.py` - environment-backed LLM client configuration
- `pyproject.toml` - Python package metadata and dependencies
- `Dockerfile` - container image build definition
- `docker-compose.yml` - local container orchestration for the API

## Prerequisites

- Python 3.14+ for local execution
- Docker and Docker Compose for containerized deployment
- `OPENAI_API_KEY` set in your environment

## Local setup

1. Clone the repository.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

> Note: This repository uses `pyproject.toml` for dependency metadata. If you do not have a `requirements.txt`, install packages listed in `pyproject.toml` with `pip`.

3. Set the API key environment variable:

```powershell
$env:OPENAI_API_KEY = "your_openai_api_key"
```

4. Start the app locally with Uvicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Docker setup

Build and run via Docker Compose:

```bash
docker compose up --build
```

This starts the API at `http://localhost:8080`.

## API usage

Send a POST request to `/api/v1/orchestrate` with a JSON payload:

```bash
curl -X POST http://localhost:8080/api/v1/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"task":"Write a short plan to build a chatbot."}'
```

Response example:

```json
{
  "status": "success",
  "task": "Write a short plan to build a chatbot.",
  "turns_executed": 5
}
```

## Environment variables

- `OPENAI_API_KEY` - required API key for the OpenAI-compatible client
- `MODEL_NAME` - optional override for the model name if you want something different than `gpt-4o`

## Configuration

`app/config.py` loads settings from environment variables and returns an `OpenAIChatCompletionClient` configured for MAF.

## Notes

- The service currently returns only basic execution metadata and does not persist conversation history.
- `app/agents.py` streams team messages and aggregates them into a list.
- If you want to inspect or extend the returned content, modify `run_agentic_team` to return richer conversation details.

## License

Add your license information here.
