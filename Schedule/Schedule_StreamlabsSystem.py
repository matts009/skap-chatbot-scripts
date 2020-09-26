#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

#from ScheduleManager import ScheduleManager # pylint: disable=import-error

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
global sm

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    #sm = ScheduleManager()
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data): 
    # if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and Parent.IsOnUserCooldown(ScriptName,ScriptSettings.Command,data.User):
    #     Parent.SendStreamMessage("Time Remaining " + str(Parent.GetUserCooldownDuration(ScriptName,ScriptSettings.Command,data.User)))

    #   Check if the propper command is used, the command is not on cooldown and the user has permission to use the command
    # if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and not Parent.IsOnUserCooldown(ScriptName,ScriptSettings.Command,data.User) and Parent.HasPermission(data.User,ScriptSettings.Permission,ScriptSettings.Info):
    #     Parent.BroadcastWsEvent("EVENT_MINE","{'show':false}")
    #     Parent.SendStreamMessage(ScriptSettings.Response)    # Send your message to chat
    #     Parent.AddUserCooldown(ScriptName,ScriptSettings.Command,data.User,ScriptSettings.Cooldown)  # Put the command on cooldown

    Parent.Log(ScriptName, repr(data))
    
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

if __name__ == '__main__':
    Init()
    Execute(None)