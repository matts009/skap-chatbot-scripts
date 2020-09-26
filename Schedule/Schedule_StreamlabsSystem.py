#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

from ScheduleDownloader import ScheduleDownloader
from ScheduleManager import ScheduleManager 

# For testing
from DataMock import DataMock 
from ParentMock import ParentMock

#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "SKAP Schedule"
Website = "https://github.com/matts009/skap-chatbot-scripts"
Description = "Schedule information for Slow Kids At Play events"
Creator = "Matt Schaller"
Version = "0.7.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
global Parent
global sm
sm = ScheduleManager()

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    schedule = ScheduleDownloader.download_schedule()
    sm.load_schedule(schedule)
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data): 
    if data.IsChatMessage() and len(data.Message) > 0 and data.Message[0] == "!":
        response = sm.process_request(data.Message[1:])

        if response and len(response) > 0:    
            Parent.SendStreamMessage(response)
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

if __name__ == '__main__':
    Init()

    data = DataMock()
    data.Message = "!dj"

    Parent = ParentMock()

    Execute(data)