FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY . /app

EXPOSE 8001

CMD ["python3", "-m" , "flask", "run"]
