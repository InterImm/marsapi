FROM python:3.6
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
RUN python setup.py install
RUN pip3 install uwsgi
ENTRYPOINT ["python", "marsapi/app.py"]