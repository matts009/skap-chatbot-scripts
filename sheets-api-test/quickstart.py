from __future__ import print_function
import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet
SPREADSHEET_ID = '1WG7QDkulWYW8vlP0UvTqBXOGRchPr_uzETyjPKSDAL0'
RANGE_NAME = 'A1:F4'

CRED_PATH = 'sheets-api-test\\credentials.json'
TOKEN_PATH = 'sheets-api-test\\token.pickle'

def main():
    creds = None
    
    # use a token.pickle file if it exists
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
                creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CRED_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save teh credentials for the next run
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets() # pylint: disable=no-member
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('DJ, Location:')
        for row in values:
            print('%s, %s' % (row[2], row[3]))

if __name__ == '__main__':
    main()