# production-cicd-platform
Code → GitHub → CI (build + push) → Docker Hub → CD (deploy to EC2) → Live App

# Flask CI/CD Deployment with Observability

## Overview

End-to-end DevOps pipeline for deploying a containerized Flask application on AWS EC2 using GitHub Actions, with integrated monitoring using Prometheus, Grafana, and Node Exporter.

---

## Key Highlights

- Containerized Flask app served via **Gunicorn + Nginx**
- Automated CI/CD pipeline using **GitHub Actions**
- Image versioning and storage via **Docker Hub**
- Deployment on **AWS EC2 using Docker Compose**
- Full observability with **Prometheus + Grafana + Node Exporter**

---

## Architecture
<img width="1536" height="1024" alt="ChatGPT Image Apr 1, 2026 at 10_05_54 PM" src="https://github.com/user-attachments/assets/e067a329-9cbd-4d96-8326-f8224d73064b" />


---

## System Flow

**CI/CD Pipeline**  
GitHub → GitHub Actions → Docker Hub → EC2  

**Request Flow**  
User → Nginx → Gunicorn → Flask  

**Monitoring Flow**  
Flask (/metrics) + Node Exporter → Prometheus → Grafana  

---

## Tech Stack

Flask • Gunicorn • Nginx • Docker • Docker Compose • GitHub Actions • AWS EC2 • Prometheus • Grafana  

---

## Project Structure
- infra/          # docker-compose + nginx config
- src/            # flask application
- Dockerfile


## How to Run

* Pushing code to master branch will trigger pipeline

```bash
docker-compose pull
docker-compose up -d
```


## Future Improvements

* Kubernetes deployment
* Autoscaling
