FROM python:3.10

WORKDIR /app

RUN apt-get update
RUN apt-get clean

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app ./app
COPY models ./models/
EXPOSE 8080
CMD uvicorn app.qa_chain:app --workers 1 --host 0.0.0.0 --port 8080 --log-level 'info'
