FROM alpine@sha256:e7d88de73db3d3fd9b2d63aa7f447a10fd0220b7cbf39803c803f2af9ba256b3 as builder
LABEL maintainer="John Doe, example@email.com"

COPY . /sb-fastapi

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_HOME=/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apk --no-cache add gcc clang build-base libffi-dev python3 python3-dev curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 - && \
    cd /sb-fastapi && \
    poetry install --no-dev --no-interaction

FROM alpine@sha256:e7d88de73db3d3fd9b2d63aa7f447a10fd0220b7cbf39803c803f2af9ba256b3
LABEL maintainer="John Doe, example@email.com"

RUN apk --no-cache add python3

COPY --from=builder /sb-fastapi /sb-fastapi

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/sb-fastapi/.venv/bin:$PATH"

EXPOSE 8000/tcp

STOPSIGNAL SIGINT

CMD ["/sb-fastapi/.venv/bin/sb-fastapi", "serve", "--host", "0.0.0.0"]
