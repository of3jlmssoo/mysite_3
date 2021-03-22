FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /mycode
WORKDIR mycode
RUN apt-get update
COPY requirements.txt /mycode/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /mycode/
COPY . /mycode/
#COPY nginx.conf /etc/nginx/
#COPY nginx/conf/mysite_nginx.conf /etc/nginx/
COPY uwsgi_params /etc/nginx/
COPY uwsgi.ini  /mycode/mysite_3/
# CMD ["uwsgi", "--ini", "/code/src/mysite/uwsgi.ini"]
