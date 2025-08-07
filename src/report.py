import traceback
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as date
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from config.settings import PDF_PATH, CHART_PATH
from src.data_source import load_data
from src.email_report import send_email_report


def log(msg):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{date.now()}] {msg}\n")


def log_exception():
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{date.now()}] ERROR:\n")
        f.write(traceback.format_exc())
        print(traceback.format_exc())


def generate_and_send_report(
    source_type=None, **kwargs
):
    try:
        log(f"📦 Loading data from {source_type} source...")
        df = load_data(source_type=source_type, **kwargs)

        recent = filter_last_7_days(df)
        recent = add_sale_amount(recent)
        summary = summarize_sales(recent)

        log("📦 Saving report to CSV...")
        save_report(summary, "output/weekly_customer_spend.csv")

        log("📦 Sending email report...")

        # Change the subject and body as per your needs
        send_email_report(
            subject="Weekly Customer Spend Report",
            body="Attached is the latest customer spend summary.",
            attachment_path="output/weekly_customer_spend.csv",
        )

    except Exception:
        log_exception()


def filter_last_7_days(df, current_date=None):
    if current_date is None:
        current_date = pd.to_datetime(date.today())
    else:
        current_date = pd.to_datetime(current_date)

    seven_days_ago = current_date - pd.Timedelta(days=7)
    return df[(df["invoice_date"] >= seven_days_ago) & (df["invoice_date"] <= current_date)].copy()


def add_sale_amount(df):
    df["sale_amount"] = (df["quantity"] * df["price"]).round(2)
    return df


def summarize_sales(df):
    summary = df.groupby("customer_id")["sale_amount"].sum().reset_index()
    summary.sort_values("sale_amount", ascending=False, inplace=True)

    top5_df = summary.head(5)

    # Create the chart
    plt.figure(figsize=(8, 4))
    plt.bar(top5_df["customer_id"], top5_df["sale_amount"])
    plt.xlabel("Customer ID")
    plt.ylabel("Total Spend")
    plt.title("Top 5 Customers - Weekly Spend")
    plt.tight_layout()

    # Save the image
    plt.savefig(CHART_PATH)
    plt.close()

    # Set up PDF
    doc = SimpleDocTemplate(PDF_PATH, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # title
    elements.append(
        Paragraph("🧾 Weekly Customer Spend Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # Add chart
    elements.append(Image(CHART_PATH, width=400, height=200))
    elements.append(Spacer(1, 12))

    # Table: Top 5 customers
    top5_table_data = [["Customer ID", "Total Spend (₹)"]]
    for _, row in top5_df.iterrows():
        top5_table_data.append(
            [row["customer_id"], f"{row['sale_amount']:.2f}"])

    table = Table(top5_table_data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Build the PDF
    doc.build(elements)
    print("📄 PDF report generated:", PDF_PATH)

    return summary


def save_report(df, path):
    df.to_csv(path, index=False)
