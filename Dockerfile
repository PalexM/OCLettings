
FROM python:3.8


ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/


CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:9000"]
