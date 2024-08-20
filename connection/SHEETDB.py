import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Google Sheets API setup
def setup_google_sheet(work_sheet_number):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Replace with the path to your downloaded JSON key file
    creds = ServiceAccountCredentials.from_json_keyfile_name('eloquent-surge-425220-q6-68988a48d003.json', scope)

    client = gspread.authorize(creds)

    # Open the sheet by name
    sheet = client.open("pyhton_etiquetas_app").get_worksheet(work_sheet_number)

    return sheet














