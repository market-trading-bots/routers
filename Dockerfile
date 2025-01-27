FROM python:3.10-slim-bookworm AS base

ENV TZ="UTC"

WORKDIR /app

RUN pip install uv

FROM base AS build

COPY pyproject.toml uv.lock ./

RUN uv sync