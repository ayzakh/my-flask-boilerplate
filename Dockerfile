FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY config.py /usr/src/app/config.py

CMD [ "gunicorn", "-b", ":5000", "uwsgi:app" ]
