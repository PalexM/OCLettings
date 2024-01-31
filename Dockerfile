FROM python:3.8


ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/


RUN python manage.py migrate && \
    python manage.py collectstatic --noinput


CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]