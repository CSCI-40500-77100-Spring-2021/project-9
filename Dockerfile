FROM python:3.9.1

WORKDIR /vl
COPY requirements.txt ./
COPY tests ./tests
COPY votelib ./votelib

RUN pip install --upgrade pip && \
        pip install --no-cache-dir -r requirements.txt

CMD ["pytest"]
