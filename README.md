# 🧪 Customer Data ETL Testing Project

## 📌 Objective
To validate customer data across an ETL pipeline using Python and SQLite. This includes:
- Extracting customer data from a CSV file
- Transforming the data (e.g., cleaning date formats)
- Loading it into a SQLite database
- Performing automated validation using Python

---

## 🛠️ Tools Used
- **Python 3.x**
- **pandas** – data transformation and validation
- **openpyxl** – handling Excel files
- **sqlite3** – lightweight database for loading and testing
- **SQLAlchemy** – Python DB toolkit

---

## 🧱 Project Structure
```
etl_customer_validation/
├── data/
│ ├── customer_source.csv # Raw input data
│ └── customer_target.csv # Cleaned data after transformation
├── scripts/
│ ├── extract.py # Script to extract data from CSV
│ ├── transform.py # Script to clean and format data
│ ├── load.py # Load cleaned data into SQLite DB
│ ├── validate.py # Compare DB data with source data
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

---