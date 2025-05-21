FROM jenkins/jenkins:lts

LABEL maintainer="TAQC - Team 3"
LABEL description="Jenkins with Python3, pip and Playwright"

USER root

WORKDIR /var/jenkins_home/workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gnupg \
    git \
    && dpkg --configure -a \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv venv

COPY requirements.txt /var/jenkins_home/workspace/

RUN venv/bin/pip install --upgrade pip \
    && venv/bin/pip install -r requirements.txt

RUN venv/bin/pip install playwright \
    && venv/bin/playwright install --with-deps chromium
