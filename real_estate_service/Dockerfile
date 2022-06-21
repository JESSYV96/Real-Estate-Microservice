FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY . /app

EXPOSE 8000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]