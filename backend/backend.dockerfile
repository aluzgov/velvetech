FROM python:3.8

RUN apt update

WORKDIR /code

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./filter_bad_words ./filter_bad_words

CMD ["python", "-m", "uvicorn", "filter_bad_words.main:app", "--host", "0.0.0.0", "--port", "80"]
