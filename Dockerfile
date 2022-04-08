FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["uwsgi", "uwsgi.ini"]