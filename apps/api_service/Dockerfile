FROM python:3.10

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./src /opt/code

WORKDIR /opt/code

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
