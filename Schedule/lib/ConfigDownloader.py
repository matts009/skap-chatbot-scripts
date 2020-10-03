import os
import pickle

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SCHEDULE_PATH = os.path.join(DIR_PATH, 'schedule.pickle')
MESSAGES_PATH = os.path.join(DIR_PATH, 'messages.pickle')

class ConfigDownloader:
    @staticmethod
    def download_schedule():
        return ConfigDownloader._download_data_with_script('ScheduleSheet.py', SCHEDULE_PATH)

    @staticmethod
    def download_messages():
        return ConfigDownloader._download_data_with_script('MessagesSheet.py', MESSAGES_PATH)

    @staticmethod
    def _download_data_with_script(script_path, data_file_path):
        if not os.path.exists(data_file_path):
            script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), script_path)

            # Interacting with the Google Sheets API (using old 2.7 libs, mind you) must be spawned 
            # in a separate process, because Streamlabs Chatbot's mechanism for ingesting a custom
            # script apparently has issues with the dependencies Google has for its API implementation
            # namely, the six module.
            #
            # So, the authentication against Google Sheets API and eventual download of sheet data must
            # be run in an process outside of the Chatbot's software environment. This is unfortunate,
            # but the only known workaround until they can finally support later version of Python.
            data = os.spawnl(os.P_WAIT, 'C:\Python27\python.exe', 'python.exe', script_path)
        
        with open(data_file_path, 'rb') as data:
            return pickle.load(data)