from ScheduleSheet import ScheduleSheet
from ScheduleItem import ScheduleItem

class ScheduleManager:
    def __init__(self):
        self._sheet = ScheduleSheet()
        self._items = self._sheet.get_schedule()