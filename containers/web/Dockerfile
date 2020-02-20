FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y postgresql-client
RUN mkdir -p /usr/source/app
WORKDIR /usr/source/app
COPY requirements.txt /usr/source/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/source/app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]