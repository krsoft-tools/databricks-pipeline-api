# Databricks Data Pipeline API (FastAPI + Docker)

Production-ready REST API built with **FastAPI**, **Pandas**, and **Docker** to serve structured outputs and aggregations from cleaned Databricks pipeline data (`sales_summary.csv`).

## 🚀 Overview

This repository demonstrates a containerized backend layer designed to bridge Big Data pipelines with downstream web services and analytical tools. It processes raw and aggregated sales data, applies business logic, and exposes clean, validated endpoints for integration.

- **Framework**: FastAPI (Python 3.11)
- **Data Engine**: Pandas
- **Validation**: Pydantic v2
- **Containerization**: Docker
- **Server**: Uvicorn

---

## 🏗 Project Architecture

databricks/
├── app/
│   ├── main.py          # FastAPI application & endpoints
│   ├── schemas.py       # Pydantic data validation
│   └── services.py      # Pandas data processing logic
├── data/
│   ├── data.csv          # Raw data export
│   └── sales_summary.csv # Aggregated Databricks pipeline output
├── Dockerfile           # Container build file
├── .dockerignore        # Excluded environments & caches
└── requirements.txt

---

## 🛠 Local Setup & Running

### Option 1: Native Python Environment

1. Create and activate virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Start server:
   uvicorn app.main:app --reload

Access Swagger UI at http://127.0.0.1:8000/docs.

---

### Option 2: Docker Container (Production Deployment)

1. Build Docker image:
   docker build -t databricks-pipeline-api .

2. Run container:
   docker run -d -p 8000:8000 --name pipeline-api-container databricks-pipeline-api

Access the containerized API documentation at http://127.0.0.1:8000/docs.

---

## 👤 Author
**Róbert Krečmer**  
Freelance Backend & Data Developer (Python / FastAPI / AI Workflows)
