FROM python:3-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/ /app/
EXPOSE 5000
CMD ["gunicorn","-w","4","-b","0.0.0.0:5000","wsgi:app"]