from __future__ import print_function

import pickle
import os
import os.path

from googleapiclient.discovery import build

from Sheet import Sheet
from ScheduleItem import ScheduleItem

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class ScheduleSheet(Sheet):

    def __init__(self):
        super(ScheduleSheet, self).__init__("'Schedule'!A2:G19")

    SCHEDULE_PATH = os.path.join(DIR_PATH, 'schedule.pickle')

    def _retrieve_schedule(self):
        items = []

        for row in self._get_values():
            items.append(ScheduleItem(row)) 

        return items

    def get_schedule(self):
        with open(ScheduleSheet.SCHEDULE_PATH, 'wb') as schedule:
            pickle.dump(self._retrieve_schedule(), schedule)

if __name__ == '__main__':
    ss = ScheduleSheet()
    ss.get_schedule()