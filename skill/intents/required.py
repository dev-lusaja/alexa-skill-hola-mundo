from skill.responses import *

##############################
# Required Intents
##############################


def cancel_intent():
    return statement("CancelIntent", "You want to cancel")	#don't use CancelIntent as title it causes code reference error during certification 


def help_intent():
    return statement("CancelIntent", "You want help")		#same here don't use CancelIntent


def stop_intent():
    return statement("StopIntent", "You want to stop")		#here also don't use StopIntent