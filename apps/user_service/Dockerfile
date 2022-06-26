FROM python:3.9
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . /app

EXPOSE 8001

CMD ["python3", "-m", "flask", "run",  "--host", "0.0.0.0"]

