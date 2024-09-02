FROM python:3.11.5-bookworm
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y --fix-missing \
    python3-pip \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    gettext \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y upgrade

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy





