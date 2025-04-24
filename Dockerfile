FROM python:3.11-slim

WORKDIR /app

ARG TOKEN
ENV TOKEN=$TOKEN

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && python -m playwright install --with-deps && pytest --html=ecomus/report/report.html --self-contained-html || true

EXPOSE 8082

VOLUME ["/app/ecomus/report"]

CMD ["python3", "-m", "http.server", "8082", "--directory", "ecomus/report"]
