FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY marks.txt .

ENV APP_NAME="Student Marks Analyzer"
ENV PASS_PERCENTAGE=40

CMD ["python", "app.py"]
