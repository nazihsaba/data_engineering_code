This repository contains a Django-based web application designed as part of a data engineering challenge. The project includes the following features:

- Secure user authentication and registration system.
- A materialized view to summarize client transactions efficiently.
- A Dockerized environment for easy deployment and development.
- PostgreSQL database integration.
- REST API endpoints and web-based interfaces for managing data.

---

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [Project Setup](#project-setup)
3. [Environment Variables](#environment-variables)
4. [Usage](#usage)

---

## **Getting Started**

These instructions will help you set up the project on your local machine for development and testing.

### **Prerequisites**
Make sure you have the following installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## **Project Setup**

### **1. Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/<your-username>/data_engineering_challenge.git
cd data_engineering_challenge
```
## **2. Configure Environment Variables**
POSTGRES_DB=data_engineering
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5433
DEBUG=True

## **3. Build and start the containers**
docker-compose build
docker-compose up


# USAGE
Once the containers are up, apply database migrations:
docker-compose exec web python manage.py migrate

Create an admin user to access the Django admin panel:
docker-compose exec web python manage.py createsuperuser


Access the Application
Web Application: Visit http://localhost:8000 in your browser.
Admin Panel: Visit http://localhost:8000/admin/ to manage the application.



