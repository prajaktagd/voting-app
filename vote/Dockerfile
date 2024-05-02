FROM python:3.11-slim AS base

RUN adduser --disabled-password myuser
USER myuser
WORKDIR /home/myuser/vote

RUN pip3 install flask redis

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY . .

EXPOSE 80

ENTRYPOINT ["python3", "app.py"]

