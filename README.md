# week7_sales_analyzing
Aravind Sales Data Analysis Dashboard

A Python-based sales data analysis project that loads sales data, cleans and processes it, performs exploratory data analysis, generates business insights, and creates visual reports.  
This project demonstrates real-world **data analysis using pandas and matplotlib**.

---

## 🚀 Features

- Load sales data from CSV files  
- Clean and preprocess data (handle missing values & duplicates)  
- Calculate key metrics (total sales, average order value, top products)  
- Analyze monthly sales trends  
- Generate formatted console reports  
- Create visualizations (line, bar, pie charts)  
- Export analysis results to Excel  
- Modular and testable project structure  

---

## 🛠️ Technologies Used

- Python 3  
- pandas  
- matplotlib  
- numpy  
- pytest  

---

## 📂 Project Structure
week7-sales-analysis/
│── sales_analyzer/
│ ├── init.py
│ ├── data_loader.py
│ ├── data_cleaner.py
│ ├── analyzer.py
│ ├── visualizer.py
│ └── main.py
│
│── data/
│ └── sales_data.csv
│
│── tests/
│ ├── test_loader.py
│ ├── test_cleaner.py
│ └── test_analyzer.py
│
│── requirements.txt
│── README.md
│── .gitignore


---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Run the analysis
python -m sales_analyzer.main

