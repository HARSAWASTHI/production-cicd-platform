FROM python:3-slim
WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ ./src
EXPOSE 5000
CMD ["gunicorn","-w","4","-b","0.0.0.0:5000","src.wsgi:app"]