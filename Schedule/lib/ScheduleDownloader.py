import os
import pickle

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCHEDULE_PATH = os.path.join(DIR_PATH, 'schedule.pickle')

class ScheduleDownloader:
    @staticmethod
    def download_schedule():
        if not os.path.exists(SCHEDULE_PATH):
            schedule_sheet_script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ScheduleSheet.py')
            schedule = os.spawnl(os.P_WAIT, 'C:\Python27\python.exe', 'python.exe', schedule_sheet_script)
        
        with open(SCHEDULE_PATH, 'rb') as schedule:
            return pickle.load(schedule)