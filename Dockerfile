FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.lock.txt ./
RUN pip install --no-cache-dir -r requirements.lock.txt

CMD [ "python", "app.py" ]