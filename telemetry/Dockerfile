FROM python:3.9.1
EXPOSE 5000

WORKDIR /tele
COPY requirements.txt ./
COPY app.py ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
