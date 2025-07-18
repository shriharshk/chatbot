"""Utility to append rows to the configured Google Sheet."""

import json
import os
from typing import List

try:
    import gspread
    from google.oauth2.service_account import Credentials
except Exception:  # pragma: no cover - library may not be installed
    gspread = None
    Credentials = None

SHEET_ID = "1L3BfrzE7ekUcWbXrOVv5LcfBMz5kyo2O5xA8UubCB_4"


def append_row(row: List[str]) -> None:
    """Append a row of data to the Google Sheet if possible."""
    if gspread is None or Credentials is None:
        print("gspread not available; cannot append row to sheet:", row)
        return

    creds_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not creds_json:
        print("Service account credentials not provided; cannot update sheet")
        return

    creds_info = json.loads(creds_json)
    creds = Credentials.from_service_account_info(
        creds_info,
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).sheet1
    sheet.append_row(row)
