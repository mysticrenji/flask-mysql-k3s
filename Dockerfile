FROM python:3.9-slim
COPY src/requirements.txt .
RUN apt-get update \
 #   && apt-get install -y mysql-client \
    && pip install -r requirements.txt
    
RUN mkdir /code
COPY src /code
WORKDIR /code
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]



     
