FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . /app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements/local.txt \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove gcc build-essential

ENTRYPOINT ["sh", "docker/production/entrypoint.sh"]
