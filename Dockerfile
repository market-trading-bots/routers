FROM python:3.10-slim-bookworm AS base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PATH="/app/.venv/bin:/root/.local/bin/:$PATH"
ENV TZ="UTC"

ADD . /app

WORKDIR /app

RUN uv sync --frozen
