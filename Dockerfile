FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && python -m playwright install --with-deps

VOLUME ["/app/login/report"]

CMD ["pytest", "--html=login/report/report.html", "--self-contained-html"]
