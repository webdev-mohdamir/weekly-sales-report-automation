import pandas as pd
from datetime import datetime as date
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# PDF path
pdf_path = "output/weekly_customer_spend.pdf"

# Chart paths
chart_path = "output/top5_chart.png"


def load_data(path):
    df = pd.read_csv(path)
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], format="%d-%m-%Y")
    return df


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
    plt.savefig(chart_path)
    plt.close()

    # Set up PDF
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # title
    elements.append(
        Paragraph("🧾 Weekly Customer Spend Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # Add chart
    elements.append(Image(chart_path, width=400, height=200))
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
    print("📄 PDF report generated:", pdf_path)

    return summary


def save_report(df, path):
    df.to_csv(path, index=False)
