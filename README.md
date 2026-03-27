# production-cicd-platform
Code → GitHub → CI (build + push) → Docker Hub → CD (deploy to EC2) → Live App
# DevOps App Service

## Overview

This project is a containerized Flask application with integrated Prometheus metrics and CI/CD pipeline.

## Features

* REST API with health and metrics endpoints
* Dockerized application
* GitHub Actions CI pipeline
* Prometheus metrics integration

## Endpoints

* `/` → Main app
* `/health` → Health check
* `/metrics` → Prometheus metrics

## CI/CD Workflow

* Build Docker image
* Push to Docker Hub
* Deploy app to ec2

## Tech Stack

* Python (Flask)
* Docker
* GitHub Actions
* Prometheus Client

## How to Run

* Pushing code to master branch will trigger pipeline

```bash
docker build -t app .
docker run -p 5000:5000 app
```

## Screenshots

<img width="1536" height="1024" alt="ChatGPT Image Mar 28, 2026 at 12_21_41 AM" src="https://github.com/user-attachments/assets/83461964-3022-464a-ab5f-aa4cc765710a" />



## Future Improvements

* Kubernetes deployment
* Autoscaling
