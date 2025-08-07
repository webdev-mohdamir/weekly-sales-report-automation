# 🧾 Weekly Customer Spend Report Automation

This project automates the generation of **weekly customer spend reports** using flexible data sources (CSV, Google Sheets, or SQL databases). It filters the last 7 days of sales data, summarizes customer spending, and emails the result as a CSV or PDF attachment.

> 🔄 Modular, extensible, and production-ready.

---

## 📁 Project Structure

```

weekly-sales-report-automation/
│
├── data/
│ ├── sales_data.csv # Sample input data
│ └── sales_data.db # SQLite database (optional)
│
├── output/
│ └── weekly_customer_spend.csv # Auto-generated weekly report
│
├── src/
│ ├── data_source.py # Central loader dispatch
│ ├── data_source_csv.py
│ ├── data_source_sql.py
│ ├── data_source_gsheet.py
│ ├── report.py # Report logic (filtering, grouping)
| ├── db_setup.py # Optional: Create SQLite from CSV
│ └── email_report.py # Email sending logic
│
├── config/
│ ├── credentials.json # Google API credentials for Google Sheets
│ ├── settings.py # Main config (Why Should I Add In GIT Baka?)
│ └── settings_template.py # Template for your own settings
│
├── run_report.py # CLI entry point
├── requirements.txt # Python dependencies
├── log.txt # Execution logs
├── LICENSE # License information
├── .gitignore # Git ignore file
└── README.md # You're reading it!

```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/webdev-mohdamir/weekly-sales-report-automation.git
cd weekly-sales-report-automation
```

---

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Configure Your Settings

Copy the template and edit with your credentials and default values:

```bash
cp config/settings_template.py config/settings.py
```

Customize these settings:

- Data source (CSV, SQLite, MySQL, PostgreSQL, Google Sheets)
- Google Sheet names (if used)
- Database credentials
- Email SMTP configuration

---

## 🚀 Usage

### Run Manually

```bash
python run_report.py --source csv
python run_report.py --source sqlite
python run_report.py --source gsheet
```

If `--source` is not passed, it defaults to what's set in `settings.py`.

You can also provide additional kwargs like when using `--source gsheet`:

```bash
python run_report.py --source gsheet --sheet_name "My Sheet" --worksheet_name "My Worksheet"
```

---

### Schedule Weekly Execution

Use Windows Task Scheduler, `cron`, or GitHub Actions to run `run_report.py` weekly.

---

## 📬 What It Does

- ✅ Loads data from the selected source (CSV, GSheet, DB)
- ✅ Filters last 7 days of data
- ✅ Summarizes spending by customer
- ✅ Outputs a clean CSV
- ✅ Emails the report automatically

---

## ✅ Sample Output

```csv
customer_id,sale_amount
CUST001,2500
CUST002,1950
...
```

---

## 🧩 Supported Data Sources

- **CSV** (default fallback)
- **Google Sheets** (with `gspread`)
- **SQLite**
- **MySQL**
- **PostgreSQL**

---

## 🤝 License

MIT License

---

Made with 💻 by [Mohd Amir](https://github.com/webdev-mohdamir)
