FROM python:3.11-slim

WORKDIR /app

ARG TOKEN
ENV TOKEN=$TOKEN

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && python -m playwright install --with-deps

VOLUME ["/app/login/report"]

CMD ["pytest", "--html=ecomus/report/report.html", "--self-contained-html"]
