import argparse
from src.report import generate_and_send_report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", help="Data source (csv, sqlite, mysql, postgres, gsheet)")
    parser.add_argument(
        "--sheet_name", help="Google Sheet name (for gsheet source)")
    parser.add_argument("--worksheet_name",
                        help="Worksheet name (for gsheet source)")

    args = parser.parse_args()

    generate_and_send_report(
        source_type=args.source,
        sheet_name=args.sheet_name,
        worksheet_name=args.worksheet_name
    )
