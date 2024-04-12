FROM python:3.7-slim

WORKDIR /opt

COPY . /opt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./app.py"]