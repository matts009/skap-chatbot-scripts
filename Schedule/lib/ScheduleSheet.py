from __future__ import print_function

import pickle
import os
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from ScheduleItem import ScheduleItem

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCHEDULE_PATH = os.path.join(DIR_PATH, 'schedule.pickle')

class ScheduleSheet:
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet
    SPREADSHEET_ID = '1WG7QDkulWYW8vlP0UvTqBXOGRchPr_uzETyjPKSDAL0'
    RANGE_NAME = 'A2:F4'

    CRED_PATH = os.path.join(DIR_PATH, 'credentials.json')
    TOKEN_PATH = os.path.join(DIR_PATH, 'token.pickle')
    SCHEDULE_PATH = os.path.join(DIR_PATH, 'schedule.pickle')

    def __init__(self):
        self._load_creds()
           
    def _load_creds(self):
        creds = None
        
        # use a token.pickle file if it exists
        if os.path.exists(ScheduleSheet.TOKEN_PATH):
            with open(ScheduleSheet.TOKEN_PATH, 'rb') as token:
                    creds = pickle.load(token)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(ScheduleSheet.CRED_PATH, ScheduleSheet.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(ScheduleSheet.TOKEN_PATH, 'wb') as token:
                pickle.dump(creds, token)
        
        self._creds = creds

    def _retrieve_schedule(self):
        service = build('sheets', 'v4', credentials=self._creds)
        sheet = service.spreadsheets() # pylint: disable=no-member
        result = sheet.values().get(spreadsheetId=ScheduleSheet.SPREADSHEET_ID, range=ScheduleSheet.RANGE_NAME).execute()
        values = result.get('values', [])

        items = []

        for row in values:
            items.append(ScheduleItem(row)) 

        return items

    def get_schedule(self):
        with open(ScheduleSheet.SCHEDULE_PATH, 'wb') as schedule:
            pickle.dump(self._retrieve_schedule(), schedule)

if __name__ == '__main__':
    ss = ScheduleSheet()
    ss.get_schedule()