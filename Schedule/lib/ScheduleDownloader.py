import os
import pickle

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCHEDULE_PATH = os.path.join(DIR_PATH, 'schedule.pickle')
MESSAGES_PATH = os.path.join(DIR_PATH, 'messages.pickle')

class ScheduleDownloader:
    @staticmethod
    def download_schedule():
        if not os.path.exists(SCHEDULE_PATH):
            schedule_sheet_script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ScheduleSheet.py')

            # Interacting with the Google Sheets API (using old 2.7 libs, mind you) must be spawned 
            # in a separate process, because Streamlabs Chatbot's mechanism for ingesting a custom
            # script apparently has issues with the dependencies Google has for its API implementation
            # namely, the six module.
            #
            # So, the authentication against Google Sheets API and eventual download of sheet data must
            # be run in an process outside of the Chatbot's software environment. This is unfortunate,
            # but the only known workaround until they can finally support later version of Python.
            schedule = os.spawnl(os.P_WAIT, 'C:\Python27\python.exe', 'python.exe', schedule_sheet_script)
        
        with open(SCHEDULE_PATH, 'rb') as schedule:
            return pickle.load(schedule)