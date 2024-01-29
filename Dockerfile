
FROM python:latest

ENV DJANGO_SETTINGS_MODULE=oc_lettings.settings
ENV DEBUG=False

RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]