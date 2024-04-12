FROM python:3.7-slim

WORKDIR /opt

COPY . /opt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python3", "./parser.py"]