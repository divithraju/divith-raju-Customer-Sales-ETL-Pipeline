# Customer Sales ETL Pipeline

## Project Overview
This project implements an ETL pipeline for analyzing customer sales data. The pipeline extracts sales data from multiple CSV files, transforms it by cleaning and aggregating the data, and loads it into a MySQL database for analysis. The process is automated and scheduled using Apache Airflow.

## Features
- **Data Extraction:** Extracts data from multiple CSV files and consolidates it into a single dataset.
- **Data Transformation:** Cleans the data by handling missing values, Standardize data formats, Feature Engineering, Aggregation, transformed data.
- **Data Loading:** Loads the transformed data into a MySQL database for further analysis.
- **Orchestration:** The ETL process is managed using Apache Airflow.

## Technologies Used
- Python
- Apache Airflow
- Pandas
- MySQL
- Docker (optional for Airflow setup)

## How to Run the Project
1. Clone the repository.
2. Install the required packages: `pip install -r requirements.txt`.
3. Configure your MySQL connection in `load.py`.
4. Run the Airflow DAG to execute the ETL pipeline.

## Project Structure
- `dags/`: Contains the Airflow DAG.
- `scripts/`: Contains Python scripts for extraction, transformation, and loading.
- `data/`: Sample sales data in CSV format.
- `requirements.txt`: List of required Python packages.

## Conclusion
This project showcases an end-to-end ETL process that can be applied to real-world data analysis scenarios.
