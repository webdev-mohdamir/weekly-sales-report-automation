from .data_source_csv import load_data_from_csv
from .data_source_sql import load_data_from_sql
from .data_source_gsheet import load_data_from_gsheet
from config.settings import DATA_SOURCE as DEFAULT_SOURCE, GSHEET_SHEET_NAME, GSHEET_WORKSHEET_NAME


def load_data(source_type=None, **kwargs):
    source = source_type or DEFAULT_SOURCE

    if source == "csv":
        return load_data_from_csv(kwargs.get("filepath", "data/sales_data.csv"))

    elif source in ("sqlite", "mysql", "postgres"):
        return load_data_from_sql(source)

    elif source == "gsheet":
        return load_data_from_gsheet(
            sheet_name=kwargs.get("sheet_name") or GSHEET_SHEET_NAME,
            worksheet_name=kwargs.get(
                "worksheet_name") or GSHEET_WORKSHEET_NAME
        )

    else:
        raise ValueError(f"Unsupported data source: {source}")
