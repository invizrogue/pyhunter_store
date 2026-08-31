FROM python:3.14-slim-bookworm AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE
    UV_COMPILE_CACHE=1

RUN uvx install --upgrade pip

RUN pip install -r requirements.txt

FROM python:3.14-slim-bookworm

COPY --from=builder /uvx /bin/

ENTRYPOINT ["top", "-b"]