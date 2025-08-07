import pandas as pd
import sqlite3


def create_db_from_csv(csv_path="data/sales_data.csv", db_path="data/sales_data.db"):
    df = pd.read_csv(csv_path)

    conn = sqlite3.connect(db_path)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

    print("✅ Database created successfully.")


if __name__ == "__main__":
    create_db_from_csv()
