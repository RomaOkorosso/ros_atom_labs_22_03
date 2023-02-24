FROM python:3.10

ARG PORT


WORKDIR /app

RUN apt update && apt install netcat postgresql-client dnsutils -y
RUN pip install --upgrade pip
COPY ./requirements.txt "/app"

RUN pip install --no-cache-dir -r requirements.txt
COPY . "/app"
EXPOSE $PORT

COPY ./entrypoint.sh /app/
RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]

CMD python3 main.py