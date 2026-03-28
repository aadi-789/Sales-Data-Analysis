#  Sales Data Analysis Project

##  Overview

The **Sales Data Analysis** project is an end-to-end data analytics solution designed to extract meaningful business insights from raw sales data using **SQL and Python-based visualization techniques**.

This project focuses on analyzing customer behavior, product performance, regional trends, delivery efficiency, and profitability to support **data-driven decision-making**.

![Python](https://img.shields.io/badge/Python-3.12.7-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![VS Code](https://img.shields.io/badge/VS%20Code-SQLTools-007ACC?logo=visualstudiocode)

---

##  Objectives

* Analyze sales data to uncover key business insights
* Identify high-performing products and regions
* Understand customer purchasing patterns
* Evaluate the impact of discounts on profit
* Track delivery performance and operational efficiency
* Perform RFM (Recency, Frequency, Monetary) segmentation

---

##  Tech Stack

* **Database:** PostgreSQL
* **Query Tool:** SQLTools (VS Code Extension)
* **Programming Language:** Python (for visualization)
* **Libraries:**
  * Pandas
  * Matplotlib
  * Seaborn

---

## 📁 Project Structure
```
Sales_Data_Analysis/
│
├── .venv/                         # Virtual environment (ignored in Git)
├── .vscode/                       # VS Code settings
│
├── DATA/                          # Raw and cleaned datasets
│   ├── archive.zip
│   ├── FINAL_cleaned.csv
│   └── Sample - Superstore.csv
│
├── docs/                          # Project documentation (reports, notes)
│
├── Notebooks/                     # Jupyter notebooks for analysis
│   ├── eda_analysis.ipynb
│   └── sales_analysis.ipynb
│
├── outputs/                       # Generated outputs
│   ├── charts/                    # Visualizations (PNG files)
│   └── processed/                 # Processed datasets / query outputs
│
├── sql/                           # SQL queries for analysis
│   └── (All analysis queries)
│
├── src/                           # Core Python scripts
│   ├── data_loader.py             # Loads data from DB/CSV
│   ├── visualization.py           # Generates charts
│   └── main.py                    # Entry point to run analysis
│
├── README.md
```

---

## 📦 Dataset

* **Source:** [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
* **Original File:** `Sample - Superstore.csv`
* **Cleaned File:** `FINAL_cleaned.csv` (after handling missing values, formatting issues, and outliers)
* The cleaned dataset is what gets imported into PostgreSQL for all SQL-based analysis.

---

## 🔄 Workflow / Roadmap

### 1️⃣ Data Cleaning & Preparation

* Cleaned raw dataset (handled missing values, formatting issues, outliers)
* Exported cleaned data into CSV format

### 2️⃣ Database Integration

* Imported dataset into PostgreSQL
* Structured tables for efficient querying

### 3️⃣ SQL Analysis

Performed structured queries to extract insights:

* Customer segmentation
* Product profitability
* Regional performance
* Discount impact
* Delivery efficiency
* Monthly & yearly trends

### 4️⃣ Visualization

The project generates **multiple analytical outputs (10+)** from SQL queries and processed data.
To maintain clarity and focus, **4 key visualizations** are highlighted below.

---

## 📊 Key Insights & Visualizations

### Sales Trend Over Time
![Sales Trend](outputs\charts\yearly_sales.png)
* Seasonal patterns are visible with peaks in Q4
* Year-over-year growth is consistently positive

### Profit by Region
![Profit by Region](outputs\charts\region_sales.png)
* The West region leads in profitability
* The Central region shows high sales but lower margins

### Top Performing Products by category
![Top Products](outputs\charts\category_profit.png)
* A small set of products drives the majority of revenue
* Technology products dominate the top 10 list

### Discount vs Profit
![Discount vs Profit](outputs\charts\discount_vs_profit.png)
* Discounts above 30% consistently result in negative profit
* Most loss-making transactions are concentrated in the high-discount range

> **Note:** Replace the image paths above with your actual filenames from `outputs/charts/`. For example if your file is named `monthly_sales.png`, update the path accordingly.

---

## ⚙️ How to Run the Project

### 1. Setup Database

* Install PostgreSQL
* Import the dataset into your database

### 2. Configure Connection

Update `db_config.json` with your credentials:
```json
{
  "host": "localhost",
  "port": 5432,
  "database": "SalesDB",
  "user": "your_username",
  "password": "your_password"
}
```

### 3. Run SQL Queries

* Use SQLTools in VS Code
* Execute queries from `/sql` folder

### 4. Generate Visuals
```bash
python main.py
```

---

## 📌 Important Notes

* SQL queries are executed directly via **VS Code SQLTools** (not through Python)
* Python is only used for visualization
* The project emphasizes **quality insights over excessive charts**

---

## 🧠 Learning Outcomes

* Strong understanding of SQL-based data analysis
* Hands-on experience with PostgreSQL integration
* Practical exposure to business analytics workflows
* Data visualization and storytelling skills

---

## 🔮 Future Improvements

* Integrate dashboard tools (Power BI / Tableau)
* Automate pipeline (ETL process)
* Add real-time data analysis
* Enhance visualization interactivity

---

## 👨‍💻 Author

**Aditya Singh**
Sales Data Analysis Project

---

## ⭐ Conclusion

This project demonstrates how structured SQL analysis combined with Python visualization can transform raw data into actionable business insights.
It highlights opportunities for optimization in sales strategy, customer targeting, and operational efficiency.
