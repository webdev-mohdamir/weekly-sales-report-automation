# 🧾 Weekly Customer Spend Report Automation

This project automates the process of generating a **weekly customer spend report** using sales data in CSV format. It filters the last 7 days, summarizes total spending per customer, and emails the result as a PDF.

---

## 📁 Project Structure

```

01_project_weekly_report/
│
├── data/
│ └── sales_data.csv # Raw sales data (input)
│
├── output/
│ └── weekly_customer_spend.csv # Auto-generated summary (CSV)
│
├── src/
│ ├── report.py # Main logic (load, transform, export)
│ └── email_report.py # Email sending module
│
├── config/
│ └── settings.py # Email credentials and config (excluded from GitHub)
│
├── run_report.py # Script to generate & email report
├── requirements.txt # Python package dependencies
├── log.txt # Logs of report runs
└── README.md # You're reading it!

```

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 2. Add Your Email Config

> ⚠️ Do NOT upload real credentials to GitHub.

Edit `config/settings.py` with your SMTP details:

```python
EMAIL_CONFIG = {
    "sender_email": "your_email@example.com",
    "app_password": "your_app_password",
    "receiver_email": "target_email@example.com",
    "smtp_host": "smtp.yourhost.com",
    "smtp_port": 465
}
```

---

### 3. Run the Script Manually

```bash
python run_report.py
```

---

### 4. Schedule Automation (Windows Task Scheduler)

This project can be automated to run weekly using Windows Task Scheduler.
Refer to your `run_report.py` as the script to execute.

---

## 📬 What It Does

- ✅ Loads data from `data/sales_data.csv`
- ✅ Filters last 7 days from a fixed or current date
- ✅ Summarizes spending by customer
- ✅ Saves to `output/weekly_customer_spend.csv`
- ✅ Emails report as attachment using SMTP

---

## ✅ Sample Output

```csv
customer_id,sale_amount
CUST001,2500
CUST002,1950
...
```

You’ll receive this report as an email attachment weekly.

---

## 🤝 License

MIT License

---

Made with 💻 by Mohd Amir (Webdev Amir)
