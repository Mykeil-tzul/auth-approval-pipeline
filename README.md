# 🧮 Daily Approval Rate Data Pipeline

This project simulates a real-world **daily transaction approval pipeline** using **Python**, **Apache Airflow**, and **Tableau** to generate insights into approval trends and operational performance.

---

## 🔧 Project Overview

**Goal:** Automatically calculate and track the **daily approval rate** across transactions, then visualize it in Tableau.

- 💻 Python for ETL and data processing
- 📅 Airflow for scheduled pipeline orchestration
- 📊 Tableau for dashboard insights

---

## 🛠️ Tech Stack

| Tool      | Purpose                        |
|-----------|--------------------------------|
| Python    | ETL & summary calculations     |
| Pandas    | Data manipulation              |
| Airflow   | DAG scheduling & automation    |
| Tableau   | Business KPI dashboard         |
| CSV       | Local data output              |

---

## 📁 Folder Structure

auth-approval-pipeline/
│
├── airflow_dags/
│ └── auth_pipeline_dag.py
│ └── images/ → screenshots
│
├── dashboard/
│ └── Tableau_Screenshots/
│
├── data/
│ ├── daily_transactions.csv
│ └── daily_approval_summary.csv
│
├── notebooks/
├── sql/
├── .gitignore
├── README.md
└── requirements.txt

---

## 📊 Pipeline Output

### ✅ Sample Output Summary (Python)

```plaintext
  transaction_date  total_transactions  declined_transactions  approval_rate_pct
  2025-07-30        11                  3                      72.73
  2025-07-31        100                 12                     88.00
  2025-08-01        100                 17                     83.00
  2025-08-02        89                  16                     82.02

---
## 📸 Screenshots

### 🔁 Daily DAG in Airflow
<img src="airflow_dags/images/Screenshot 2025-08-03 at 8.31.49 PM.png" width="600"/>

### 💾 Python Pipeline Output (CSV Generation)
<img src="airflow_dags/images/Screenshot 2025-08-03 at 8.32.34 PM.png" width="600"/>

### 📈 Tableau Dashboard
<img src="airflow_dags/images/Screenshot 2025-08-03 at 8.32.57 PM.png" width="600"/>

---

## ✅ What I Learned

- How to orchestrate a basic pipeline in Airflow  
- Writing custom Python ETL scripts  
- Generating and saving daily metrics with Pandas  
- Visual storytelling through Tableau dashboards  
- GitHub version control and clean documentation  

---

## 📌 Challenges Faced

- Simulating realistic transaction data for decline/approval rates  
- Dynamically calculating metrics from raw CSV  
- Proper image path linking and rendering in GitHub  
- Balancing simplicity with dashboard clarity  

---

## 🚀 Next Steps

- Add email alert in Airflow on failure  
- Upload to Streamlit for stakeholder access  
- Add database or cloud storage layer (e.g. Snowflake or BigQuery)  

-----

### ✅ Final Steps

1. Paste the above into `README.md` in VS Code.
2. Save the file.
3. In terminal:

```bash
git add README.md
git commit -m "📝 Final README with screenshots and structure"
git push

