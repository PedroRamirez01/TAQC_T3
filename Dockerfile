FROM python:3.11-slim

WORKDIR /app

ARG TOKEN
ENV TOKEN=$TOKEN

COPY install_docker.sh /tmp/install_docker.sh
RUN chmod +x /tmp/install_docker.sh && /tmp/install_docker.sh

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && python -m playwright install --with-deps

VOLUME ["/app/ecomus/report"]

CMD ["sleep", "infinity"]