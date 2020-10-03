from __future__ import print_function

import pickle
import os
import os.path

from googleapiclient.discovery import build

from Sheet import Sheet
from ScheduleItem import ScheduleItem

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class MessagesSheet(Sheet):

    MESSAGES_PATH = os.path.join(DIR_PATH, 'messages.pickle')

    def __init__(self):
        super(MessagesSheet, self).__init__('Messages!A:A')

    def _retrieve_messages(self):
        items = []

        for row in self._get_values():
            items.append(row[0])

        return items

    def get_messages(self):
        with open(MessagesSheet.MESSAGES_PATH, 'wb') as messages:
            pickle.dump(self._retrieve_messages(), messages)

if __name__ == '__main__':
    ms = MessagesSheet()
    ms.get_messages()