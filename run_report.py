import traceback
from datetime import datetime
from src.report import load_data, filter_last_7_days, summarize_sales, add_sale_amount, save_report
from src.email_report import send_email_report
from config.settings import EMAIL_CONFIG


def log(msg):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")


def log_exception():
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] ERROR:\n")
        f.write(traceback.format_exc())


def main():
    try:
        log("Starting report generation...")

        df = load_data("data/sales_data.csv")
        log("✅ Loaded data")

        recent = filter_last_7_days(df, current_date="2022-08-10")
        log("✅ Filtered last 7 days")

        recent = add_sale_amount(recent)
        summary = summarize_sales(recent)

        save_report(summary, "output/weekly_customer_spend.csv")
        log("✅ Report saved successfully")

        # Double check the file you're attaching (it's .csv, not .pdf!)
        attachment_path = "output/weekly_customer_spend.csv"

        send_email_report(
            sender_email=EMAIL_CONFIG["sender_email"],
            app_password=EMAIL_CONFIG["app_password"],
            receiver_email=EMAIL_CONFIG["receiver_email"],
            subject="Weekly Customer Spend Report",
            body="Attached is the latest customer spend summary.",
            attachment_path="output/weekly_customer_spend.pdf",
            host=EMAIL_CONFIG["smtp_host"],
            port=EMAIL_CONFIG["smtp_port"]
        )
        log("📧 Email sent successfully.")

    except Exception:
        log_exception()


if __name__ == "__main__":
    main()
