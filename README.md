# Retail Data Engineering Pipeline using PySpark, SQL & Power BI

An end-to-end ETL and analytics pipeline built using PySpark for large-scale data processing, SQLite for analytics storage, and Power BI for business intelligence dashboards.

## Features
- Processed 500K+ retail transaction records
- Implemented layered ETL architecture (raw → processed → gold)
- Built Spark-based transformation workflows
- Generated SQL-driven business insights
- Created interactive Power BI analytics dashboard
- Added logging for pipeline monitoring

## Overview

This project demonstrates an end-to-end Data Engineering pipeline built using PySpark, SQL, SQLite, and Power BI.

The pipeline processes raw retail transaction data through multiple ETL stages to generate business insights and visual analytics dashboards.

---

## Tech Stack

- Python
- PySpark
- SQL
- SQLite
- Power BI
- Pandas

---

## Project Architecture

Raw Data → Ingestion Layer → Transformation Layer → Gold Layer Analytics → SQLite Database → Power BI Dashboard

---

## Project Workflow

### 1. Data Ingestion
- Loaded raw retail CSV dataset
- Stored dataset in raw data layer

### 2. Data Transformation
Using PySpark:
- Removed null values
- Filtered invalid records
- Created calculated columns
- Cleaned transactional data

### 3. Gold Layer Analytics
Generated:
- Country-wise revenue
- Top-selling products
- Top customers
- Transaction analytics

### 4. SQL Analytics Layer
- Loaded processed data into SQLite
- Executed business SQL queries

### 5. Dashboard Visualization
Created Power BI dashboard with:
- KPI cards
- Revenue analysis
- Product insights
- Customer insights
- Country transaction analysis

---

## Folder Structure

```text
retail-data-engineering-project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── scripts/
│   ├── ingestion.py
│   ├── transformation.py
│   ├── gold_layer.py
│   └── load_to_sql.py
│
├── sql/
│   └── business_queries.sql
│
├── screenshots/
│   └── dashboard.png
│
├── retail_analytics.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dashboard Preview

![Dashboard](screenshots/dashboard.png)

---

## Key Business Insights

- United Kingdom generated the highest revenue
- Top-selling products were identified using sales quantity
- High-value customers were analyzed using total purchase amount
- Country-level transaction distribution was analyzed

---

## How to Run Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Data Transformation Pipeline

```bash
py scripts/transformation.py
```

### 3. Run Gold Layer Analytics

```bash
py scripts/gold_layer.py
```

### 4. Load Data into SQLite

```bash
py scripts/load_to_sql.py
```

---

## Future Improvements

- AWS S3 integration
- Apache Airflow scheduling
- Parquet storage optimization
- Real-time streaming pipeline
- Cloud deployment

---

## Resume Highlights

- Built end-to-end ETL data pipeline using PySpark
- Processed 500K+ retail transaction records
- Implemented layered data architecture (raw → processed → gold)
- Integrated SQL analytics and Power BI dashboarding
- Generated business insights using Spark transformations and SQL queries
- Optimized storage using Parquet format and Spark partitioning