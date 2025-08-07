import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def load_data_from_gsheet(sheet_name, worksheet_name):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "config/credentials.json", scope)
    client = gspread.authorize(creds)

    print("📥 Fetching data from Google Sheets...")
    sheet = client.open(sheet_name)
    worksheet = sheet.worksheet(worksheet_name)

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], format="%d-%m-%Y")

    print(f"✅ Loaded {len(df)} rows from {sheet_name}/{worksheet_name}")
    return df
