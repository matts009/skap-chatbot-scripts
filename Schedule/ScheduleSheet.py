from __future__ import print_function
import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from ScheduleItem import ScheduleItem

class ScheduleSheet:
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet
    SPREADSHEET_ID = '1WG7QDkulWYW8vlP0UvTqBXOGRchPr_uzETyjPKSDAL0'
    RANGE_NAME = 'A1:F4'

    CRED_PATH = 'Schedule\\credentials.json'
    TOKEN_PATH = 'Schedule\\token.pickle'
    SCHEDULE_PATH = 'Schedule\\schedule.pickle'

    def __init__(self):
        self._load_creds()
        self._service = build('sheets', 'v4', credentials=self._creds)
        self._sheet = self._service.spreadsheets() # pylint: disable=no-member

        if os.path.exists(ScheduleSheet.SCHEDULE_PATH):
            with open(ScheduleSheet.SCHEDULE_PATH, 'rb') as schedule:
                self._schedule = pickle.load(schedule)
        else:
            self._schedule = None
           
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
        result = self._sheet.values().get(spreadsheetId=ScheduleSheet.SPREADSHEET_ID, range=ScheduleSheet.RANGE_NAME).execute()
        values = result.get('values', [])

        items = []

        for row in values:
            items.append(ScheduleItem(row))

        with open(ScheduleSheet.SCHEDULE_PATH, 'wb') as schedule:
            pickle.dump(items, schedule)

        return items

    def get_schedule(self):
        if not self._schedule:
            self._schedule = self._retrieve_schedule()
        return self._schedule