# DJANGO APP WITH DOCKER CONTAINER

Docker Installation

Inside the Project Directory or Project Folder

## Step 1
        Create Dockerfile

Inside Dockerfile
        FROM python:3
        ENV PYTHONUNBUFFERED 1
        RUN mkdir /app
        WORKDIR /app
        COPY requirements.txt /app/
        RUN pip install -r requirements.txt
        COPY . /app/

## STEP 2
        Create docker-compose.yml

Inside docker-compose.yml
        version: '3'


        services:
                web:
                        build: .
                        command: python manage.py runserver 0.0.0.0:8000
                        volumes:
                                - .:/app
                        ports:
                                - "8000:8000"

In terminal 
        docker-compose run web django-admin startproject projectname .

if you are using docker with sudo 
        try sudo chown -R $USER:$USER .


## RUN DOCKER
        docker-compose up

        docker ps
                running process
        
        docker exec containername python manage.py startapp appname
        


