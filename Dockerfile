FROM jenkins/jenkins:lts

LABEL maintainer="TAQC - Team 3"
LABEL description="Jenkins with Python3, pip and Playwright"

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
