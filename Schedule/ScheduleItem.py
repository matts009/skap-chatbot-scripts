from datetime import datetime
import pytz

est_tz = pytz.timezone('US/Eastern')

class ScheduleItem:
    def __init__(self, sheet_row):
        date = sheet_row[0]
        start_time = sheet_row[1]
        end_time = sheet_row[2]

        self._set_start_end_ts(date, start_time, end_time)
        
        self.dj = sheet_row[3]
        self.location = sheet_row[4]
        self.genre = sheet_row[5]

    def _set_start_end_ts(self, date, start_time, end_time):
        ts_fmt = '%m/%d/%y %H%M'

        self.start_ts = est_tz.localize(datetime.strptime('{0} {1}'.format(date, start_time), ts_fmt))
        self.end_ts = est_tz.localize(datetime.strptime('{0} {1}'.format(date, end_time), ts_fmt))

        