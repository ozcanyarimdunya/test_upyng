FROM ozcanyarimdunya/upyng:1.0.0

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY upyng.conf /etc/nginx/conf.d

COPY . .
