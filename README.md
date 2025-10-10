Project Overview

This project demonstrates a Microservices Architecture using Docker, PostgreSQL, and Flask. It consists of multiple services, each handling a specific responsibility:

User Service – Manages user authentication and profiles.

Task Service – Handles user tasks (CRUD operations).

Gateway Service – Routes requests to the respective microservices.

The project also demonstrates DevOps best practices like containerization, orchestration with Docker Compose, and optional CI/CD integration.



🧩 Features
Service	Description
User Service	Signup, login, user management
Task Service	Create, Read, Update, Delete tasks
Gateway Service	API routing and aggregation
PostgreSQL	Database for each microservice
Docker & Docker Compose	Containerization and orchestration
CI/CD Pipeline	Automated build, test, and deployment (optional)
🛠️ Prerequisites

Docker

Docker Compose

Python 3.10+

Git

🔧 Setup & Run

Clone the repository

git clone <repository_url>
cd microservices-devops


Build and start containers

docker-compose up --build


Access the services

Gateway: http://localhost:8000

User Service: http://localhost:8001

Task Service: http://localhost:8002

🔎 API Usage Examples

User Signup:

curl -X POST http://localhost:8001/signup \
 -H "Content-Type: application/json" \
 -d '{"username":"john","password":"pass123"}'


Create Task:

curl -X POST http://localhost:8002/tasks \
 -H "Content-Type: application/json" \
 -d '{"user_id":1,"title":"Complete Project"}'


Access via Gateway:

curl http://localhost:8000/users
curl http://localhost:8000/tasks

🤖 CI/CD Pipeline (Optional)

Automated testing using pytest

Docker image build and push to Docker Hub

GitHub Actions workflow triggers on push to main branch

🧠 Key Learnings
Area	Skills Learned
Microservices Architecture	Modular, scalable service design
Containerization	Docker for each microservice
Orchestration	Docker Compose multi-container setup
API Gateway	Centralized routing for microservices
Database Management	PostgreSQL integration per service
DevOps Automation	CI/CD, testing, version control
💡 Optional Enhancements

Add JWT authentication at Gateway level

Integrate logging and monitoring with Prometheus/Grafana

Deploy using Kubernetes instead of Docker Compose

Add Redis caching for Task Service
