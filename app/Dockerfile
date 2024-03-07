FROM python:3.11-slim

WORKDIR /app

ENV PYTHONBUFFERED 1

COPY requirements_web.txt /app/

RUN python3 -m pip install --upgrade pip \
pip install -r requirements_web.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]