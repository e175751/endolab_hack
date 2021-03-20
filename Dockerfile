FROM python:3.6

WORKDIR /usr/src/app

COPY src ./

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "bot.py"]