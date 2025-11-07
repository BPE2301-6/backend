FROM python:3.12-slim AS builder

WORKDIR /app

RUN pip install --no-cache-dir uv alembic

COPY pyproject.toml uv.lock ./

RUN uv venv /opt/venv && \
    uv sync --locked --no-dev

RUN rm -rf ~/.cache

FROM python:3.12-slim AS final

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /app

COPY config.toml alembic.ini run.sh ./

COPY alembic ./alembic

COPY src ./src

RUN chmod +x run.sh

CMD ["./run.sh"]