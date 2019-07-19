FROM python:3

COPY ./requirements.txt /app/requirments.txt
WORKDIR /app
COPY ./api /app/api
RUN pip install --no-cache-dir -r /app/requirments.txt
CMD flask run -h 0.0.0.0
CMD pytest