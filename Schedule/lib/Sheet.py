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

class Sheet(object):
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet
    SPREADSHEET_ID = '1WG7QDkulWYW8vlP0UvTqBXOGRchPr_uzETyjPKSDAL0'
    RANGE_NAME = None

    CRED_PATH = os.path.join(DIR_PATH, 'credentials.json')
    TOKEN_PATH = os.path.join(DIR_PATH, 'token.pickle')

    def __init__(self, range_name):
        self._load_creds()
        self.RANGE_NAME = range_name
           
    def _load_creds(self):
        creds = None
        
        # use a token.pickle file if it exists
        if os.path.exists(self.TOKEN_PATH):
            with open(self.TOKEN_PATH, 'rb') as token:
                    creds = pickle.load(token)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CRED_PATH, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.TOKEN_PATH, 'wb') as token:
                pickle.dump(creds, token)
        
        self._creds = creds
    
    def _get_values(self):
        service = build('sheets', 'v4', credentials=self._creds)
        sheet = service.spreadsheets() # pylint: disable=no-member
        result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID, range=self.RANGE_NAME).execute()
        return result.get('values', [])
