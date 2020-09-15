FROM python:3.8

RUN apt-get -y update
RUN apt-get install -y ffmpeg

WORKDIR /usr/src/JB2020AudioAnomaly

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

ADD src/ ./src/

ADD samples/ ./samples/

# RUN ls -la /src/*

# COPY . /app

# RUN cd /app

CMD ["python3", "src/view.py"]