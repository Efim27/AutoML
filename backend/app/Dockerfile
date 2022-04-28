FROM python:3.9-buster

WORKDIR /

RUN mkdir /code && mkdir /code/app

COPY ./requirements.txt /code/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/app/requirements.txt

RUN pip install catboost

RUN pip install uvicorn

COPY . /code/app

EXPOSE 8000

WORKDIR /code

CMD ["uvicorn", "app.main:app",  "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]