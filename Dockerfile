FROM python:3.11-slim

# Install uv directly into the container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy configuration files first to cache dependencies
COPY pyproject.toml uv.lock ./

# Force uv to install packages directly into the container's global Python 3.11 stack
RUN uv pip install --system \
    "autogen-ext[magentic-one]" \
    autogen-core \
    autogen-agentchat \
    fastapi \
    uvicorn \
    pydantic \
    pydantic-settings \
    openapi-spec-validator \
    aiofiles \
    openai \
    tiktoken

# Copy your actual application code
COPY app /app/app

EXPOSE 8080

# Execute natively using the system runtime directly
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]