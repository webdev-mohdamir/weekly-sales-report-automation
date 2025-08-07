import pandas as pd
import sqlite3
import pymysql
import psycopg2
from config.settings import SQLITE_DB_PATH, MYSQL_CONFIG, POSTGRES_CONFIG


def load_data_from_sql(source=None):
    if source == "sqlite":
        return load_from_sqlite(SQLITE_DB_PATH)
    elif source == "mysql":
        return load_from_mysql()
    elif source == "postgres":
        return load_from_postgres()
    else:
        raise ValueError(f"Unsupported SQL data source: {source}")


def load_from_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], format="%d-%m-%Y")
    return df


def load_from_mysql():
    conn = pymysql.connect(**MYSQL_CONFIG)
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], format="%d-%m-%Y")
    return df


def load_from_postgres():
    conn = psycopg2.connect(**POSTGRES_CONFIG)
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], format="%d-%m-%Y")
    return df
