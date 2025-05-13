FROM jenkins/jenkins:lts

LABEL maintainer="TAQC - Team 3"
LABEL description="Jenkins with Python3, pip and Playwright"
#LABEL version="1.0"
USER root

WORKDIR /var/jenkins_home/workspace

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv venv
