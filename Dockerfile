FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN flask db init
RUN flask db migrate
RUN flask db upgrade
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]